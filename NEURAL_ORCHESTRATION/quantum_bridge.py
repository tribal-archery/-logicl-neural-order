"""Provider-neutral 231-node -> 8-qubit quantum bridge and hybrid QNN.

This module implements the supplied Quantum Bridge specification while
separating logical node count from qubit count and local computation from
physical/cloud execution.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
import hashlib
import json
import math
import random
from typing import Any, Iterable, Protocol, Sequence

NODE_COUNT = 231
QUBIT_COUNT = 8
DEFAULT_SHOTS = 128


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class QuantumProblem:
    node_count: int = NODE_COUNT
    qubit_count: int = QUBIT_COUNT
    shots: int = DEFAULT_SHOTS
    feature_name: str = "activation"

    def validate(self) -> None:
        if self.node_count != NODE_COUNT:
            raise ValueError(f"Quantum Bridge requires {NODE_COUNT} logical nodes")
        if self.qubit_count != QUBIT_COUNT:
            raise ValueError(f"Quantum Bridge requires {QUBIT_COUNT} qubits")
        if self.shots <= 0:
            raise ValueError("shots must be positive")


@dataclass(frozen=True)
class Gate:
    name: str
    targets: tuple[int, ...]
    parameter: float | None = None


@dataclass(frozen=True)
class QuantumCircuitIR:
    qubit_count: int
    gates: tuple[Gate, ...]
    encoding: str = "231_nodes_modulo_8"
    version: str = "0.1.0"

    def validate(self) -> None:
        if self.qubit_count != QUBIT_COUNT:
            raise ValueError("Circuit must contain exactly 8 qubits")
        for gate in self.gates:
            if any(q < 0 or q >= self.qubit_count for q in gate.targets):
                raise ValueError("Gate targets an invalid qubit")


@dataclass(frozen=True)
class EvidenceArtifact:
    problem_hash: str
    circuit_hash: str
    measurement_hash: str
    node_count: int
    qubit_count: int
    shots: int
    execution_domain: str
    verification_status: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class QuantumProviderAdapter(Protocol):
    provider_name: str

    def execute(self, circuit: QuantumCircuitIR, shots: int) -> dict[str, int]:
        ...


def node_to_qubit(node_index: int) -> int:
    if not 0 <= node_index < NODE_COUNT:
        raise IndexError(node_index)
    return node_index % QUBIT_COUNT


def encode_nodes(nodes: Sequence[float]) -> list[float]:
    """Aggregate 231 logical node values into 8 normalized qubit angles."""
    if len(nodes) != NODE_COUNT:
        raise ValueError(f"expected {NODE_COUNT} nodes, got {len(nodes)}")
    buckets = [0.0] * QUBIT_COUNT
    counts = [0] * QUBIT_COUNT
    for i, value in enumerate(nodes):
        q = node_to_qubit(i)
        buckets[q] += float(value)
        counts[q] += 1
    return [math.pi * math.tanh(buckets[q] / max(counts[q], 1)) for q in range(QUBIT_COUNT)]


def build_variational_circuit(nodes: Sequence[float], weights: Sequence[float]) -> QuantumCircuitIR:
    if len(weights) != QUBIT_COUNT:
        raise ValueError(f"expected {QUBIT_COUNT} variational weights")
    angles = encode_nodes(nodes)
    gates: list[Gate] = []
    for q in range(QUBIT_COUNT):
        gates.append(Gate("RY", (q,), angles[q] + float(weights[q])))
    for q in range(QUBIT_COUNT - 1):
        gates.append(Gate("CNOT", (q, q + 1)))
    gates.append(Gate("CNOT", (QUBIT_COUNT - 1, 0)))
    return QuantumCircuitIR(QUBIT_COUNT, tuple(gates))


def _apply_ry(state: list[complex], q: int, theta: float) -> None:
    c, s = math.cos(theta / 2.0), math.sin(theta / 2.0)
    bit = 1 << q
    for base in range(0, len(state), bit * 2):
        for offset in range(bit):
            i, j = base + offset, base + offset + bit
            a, b = state[i], state[j]
            state[i] = c * a - s * b
            state[j] = s * a + c * b


def _apply_cnot(state: list[complex], control: int, target: int) -> None:
    cbit, tbit = 1 << control, 1 << target
    for i in range(len(state)):
        if (i & cbit) and not (i & tbit):
            j = i | tbit
            state[i], state[j] = state[j], state[i]


def simulate_statevector(circuit: QuantumCircuitIR) -> list[complex]:
    circuit.validate()
    state = [0j] * (1 << circuit.qubit_count)
    state[0] = 1.0 + 0j
    for gate in circuit.gates:
        if gate.name == "RY":
            _apply_ry(state, gate.targets[0], float(gate.parameter or 0.0))
        elif gate.name == "CNOT":
            _apply_cnot(state, gate.targets[0], gate.targets[1])
        else:
            raise ValueError(f"unsupported local gate: {gate.name}")
    return state


def measure(state: Sequence[complex], shots: int, seed: int) -> dict[str, int]:
    probabilities = [abs(a) ** 2 for a in state]
    total = sum(probabilities)
    probabilities = [p / total for p in probabilities]
    rng = random.Random(seed)
    cumulative: list[float] = []
    running = 0.0
    for p in probabilities:
        running += p
        cumulative.append(running)

    counts = [0] * len(state)
    for _ in range(shots):
        x = rng.random()
        lo, hi = 0, len(cumulative) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if cumulative[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        counts[lo] += 1

    return {format(i, f"0{QUBIT_COUNT}b"): n for i, n in enumerate(counts) if n}


class LocalSimulator:
    provider_name = "local-simulator"

    def execute(self, circuit: QuantumCircuitIR, shots: int) -> dict[str, int]:
        state = simulate_statevector(circuit)
        return measure(state, shots, seed=int(digest(asdict(circuit))[:16], 16))


class IBMAdapter:
    provider_name = "ibm"

    def execute(self, circuit: QuantumCircuitIR, shots: int) -> dict[str, int]:
        raise RuntimeError("IBM adapter is declared only; live execution is not configured")


class AzureQuantumAdapter:
    provider_name = "microsoft-azure-quantum"

    def execute(self, circuit: QuantumCircuitIR, shots: int) -> dict[str, int]:
        raise RuntimeError("Azure Quantum adapter is declared only; live execution is not configured")


class CirqAdapter:
    provider_name = "google-cirq"

    def execute(self, circuit: QuantumCircuitIR, shots: int) -> dict[str, int]:
        raise RuntimeError("Google/Cirq adapter is declared only; live execution is not configured")


def normalize_measurements(counts: dict[str, int]) -> dict[str, Any]:
    shots = sum(counts.values())
    return {
        "shots": shots,
        "counts": dict(sorted(counts.items())),
        "probabilities": {
            key: count / shots for key, count in sorted(counts.items())
        } if shots else {},
    }


def verify_bridge(problem: QuantumProblem, circuit: QuantumCircuitIR, measurement: dict[str, Any]) -> dict[str, Any]:
    problem.validate()
    circuit.validate()
    observed_shots = int(measurement.get("shots", 0))
    structural = {
        "node_count_is_231": problem.node_count == NODE_COUNT,
        "qubit_count_is_8": problem.qubit_count == QUBIT_COUNT,
        "circuit_qubit_count_is_8": circuit.qubit_count == QUBIT_COUNT,
        "shots_positive": problem.shots > 0,
        "measurement_shots_match": observed_shots == problem.shots,
        "encoding_explicit": circuit.encoding == "231_nodes_modulo_8",
    }
    return {
        "status": "VERIFIED" if all(structural.values()) else "NOT_VERIFIED",
        "domain": "STRUCTURAL_LOCAL_COMPUTATION",
        "checks": structural,
        "physical_execution_proven": False,
    }


def build_evidence(
    problem: QuantumProblem,
    circuit: QuantumCircuitIR,
    measurement: dict[str, Any],
    verification: dict[str, Any],
    execution_domain: str,
) -> EvidenceArtifact:
    return EvidenceArtifact(
        problem_hash=digest(asdict(problem)),
        circuit_hash=digest(asdict(circuit)),
        measurement_hash=digest(measurement),
        node_count=problem.node_count,
        qubit_count=problem.qubit_count,
        shots=problem.shots,
        execution_domain=execution_domain,
        verification_status=str(verification["status"]),
    )


class VariationalQuantumNeuralNetwork:
    """Hybrid 231-input / 8-qubit variational network.

    Logical nodes are assigned to 8 qubit buckets. Qubit probabilities are
    projected back to all 231 logical nodes. The weights are classical
    trainable parameters.
    """

    def __init__(self, weights: Sequence[float] | None = None) -> None:
        self.weights = list(weights) if weights is not None else [0.0] * QUBIT_COUNT
        if len(self.weights) != QUBIT_COUNT:
            raise ValueError("QNN requires exactly 8 weights")

    def forward(
        self,
        nodes: Sequence[float],
        *,
        shots: int = DEFAULT_SHOTS,
        adapter: QuantumProviderAdapter | None = None,
    ) -> dict[str, Any]:
        problem = QuantumProblem(shots=shots)
        problem.validate()
        circuit = build_variational_circuit(nodes, self.weights)
        provider = adapter or LocalSimulator()
        counts = provider.execute(circuit, shots)
        measurement = normalize_measurements(counts)
        verification = verify_bridge(problem, circuit, measurement)
        evidence = build_evidence(
            problem, circuit, measurement, verification, provider.provider_name
        )

        qubit_prob = [0.0] * QUBIT_COUNT
        for bitstring, count in counts.items():
            for q in range(QUBIT_COUNT):
                if bitstring[-1 - q] == "1":
                    qubit_prob[q] += count / max(shots, 1)

        node_output = [qubit_prob[node_to_qubit(i)] for i in range(NODE_COUNT)]
        return {
            "nodes": node_output,
            "qubit_probabilities": qubit_prob,
            "measurement": measurement,
            "verification": verification,
            "evidence": evidence.to_dict(),
            "circuit": asdict(circuit),
        }

    def train_step(
        self,
        nodes: Sequence[float],
        targets: Sequence[float],
        *,
        learning_rate: float = 0.1,
        epsilon: float = 1e-3,
    ) -> dict[str, Any]:
        if len(targets) != NODE_COUNT:
            raise ValueError(f"expected {NODE_COUNT} targets")

        base = self.forward(nodes, shots=DEFAULT_SHOTS)
        base_loss = _mse(base["nodes"], targets)
        gradients: list[float] = []

        for q in range(QUBIT_COUNT):
            original = self.weights[q]
            self.weights[q] = original + epsilon
            perturbed = self.forward(nodes, shots=DEFAULT_SHOTS)
            loss = _mse(perturbed["nodes"], targets)
            gradients.append((loss - base_loss) / epsilon)
            self.weights[q] = original

        for q, gradient in enumerate(gradients):
            self.weights[q] -= learning_rate * gradient

        return {
            "loss_before": base_loss,
            "gradients": gradients,
            "weights": list(self.weights),
            "verification": base["verification"],
        }


def _mse(values: Iterable[float], targets: Iterable[float]) -> float:
    pairs = list(zip(values, targets))
    return sum((float(a) - float(b)) ** 2 for a, b in pairs) / max(len(pairs), 1)


__all__ = [
    "NODE_COUNT",
    "QUBIT_COUNT",
    "QuantumProblem",
    "QuantumCircuitIR",
    "EvidenceArtifact",
    "LocalSimulator",
    "IBMAdapter",
    "AzureQuantumAdapter",
    "CirqAdapter",
    "VariationalQuantumNeuralNetwork",
    "build_variational_circuit",
    "encode_nodes",
    "normalize_measurements",
    "verify_bridge",
]
