"""Executable V1 orchestration kernel for Neural Thinking Machine.

The runtime separates routing/control from model computation. Providers are
adapters; the Neural OS protocol remains stable when models are replaced.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from hashlib import sha256
from time import perf_counter
from typing import Any, Protocol, Sequence
from uuid import uuid4

from .thought_modes import get_mode


@dataclass(frozen=True)
class TaskEnvelope:
    request_id: str
    task_id: str
    intent: dict[str, Any]
    context: dict[str, Any]
    input: Any
    constraints: tuple[str, ...] = ()
    evidence_requirements: tuple[str, ...] = ()
    expected_output_schema: dict[str, Any] = field(default_factory=dict)
    max_steps: int = 8
    max_parallel: int = 4


@dataclass(frozen=True)
class MachineSpec:
    machine_id: str
    role: str
    model_ref: str
    capabilities: frozenset[str]
    reliability: float = 0.5
    enabled: bool = True


@dataclass(frozen=True)
class RouteDecision:
    mode_ids: tuple[int, ...]
    machine_ids: tuple[str, ...]
    regime: str
    capability: str
    reason: str


@dataclass(frozen=True)
class DispatchResult:
    request_id: str
    task_id: str
    machine_id: str
    role: str
    model_ref: str
    output: Any
    uncertainty: float
    status: str
    latency_ms: float
    input_hash: str
    provenance: dict[str, Any]
    evidence_refs: tuple[str, ...] = ()
    evidence_status: str = "unverified"


class ModelAdapter(Protocol):
    def generate(self, request: dict[str, Any]) -> Any:
        ...


class MachineRegistry:
    def __init__(self, machines: Sequence[MachineSpec]) -> None:
        self._machines = {machine.machine_id: machine for machine in machines}

    def by_capability(self, capability: str) -> list[MachineSpec]:
        return [
            machine
            for machine in self._machines.values()
            if machine.enabled and capability in machine.capabilities
        ]

    def get(self, machine_id: str) -> MachineSpec:
        return self._machines[machine_id]


class ComputationAllocator:
    def route(self, task: TaskEnvelope) -> RouteDecision:
        uncertainty = float(task.context.get("uncertainty", 0.0))
        dispersion = float(task.context.get("dispersion", 0.0))
        kind = str(task.intent.get("action", "general"))
        object_name = str(task.intent.get("object", ""))
        text = f"{kind} {object_name}".lower()

        if "quantum" in text or "qubit" in text:
            modes = (8, 15, 25)
            capability = "quantum_neural"
            regime = "hybrid_quantum_variational"
        elif "code" in text or "software" in text:
            modes = (15, 21, 23)
            capability = "code"
            regime = "symbolic_execution"
        elif "proof" in text or "math" in text:
            modes = (7, 13, 18)
            capability = "formal_reasoning"
            regime = "formal_search"
        elif dispersion > 0.3 or uncertainty > 0.7:
            modes = (2, 15, 18)
            capability = "verification"
            regime = "high_uncertainty_recovery"
        elif uncertainty > 0.2 or dispersion > 0.0:
            modes = (7, 9, 10)
            capability = "search"
            regime = "branch_and_converge"
        else:
            modes = (1, 25)
            capability = "general_reasoning"
            regime = "direct"

        return RouteDecision(
            mode_ids=modes,
            machine_ids=(),
            regime=regime,
            capability=capability,
            reason=f"uncertainty={uncertainty:.3f}; dispersion={dispersion:.3f}; capability={capability}",
        )


class VerificationGate:
    def verify(self, results: Sequence[DispatchResult], task: TaskEnvelope) -> dict[str, Any]:
        if not results:
            return {"accepted": False, "reason": "no_results", "verification_status": "unverified"}

        blocked = [result for result in results if result.status in {"ERROR", "BLOCKED"}]
        max_uncertainty = max(result.uncertainty for result in results)
        evidence_ok = not task.evidence_requirements or all(result.evidence_refs for result in results)
        accepted = not blocked and evidence_ok and max_uncertainty <= 0.85
        status = "supported" if accepted else "unverified"

        return {
            "accepted": accepted,
            "verification_status": status,
            "max_uncertainty": max_uncertainty,
            "evidence_ok": evidence_ok,
            "blocked_results": len(blocked),
            "claims": [{
                "claim": "dispatch results satisfy the V1 verification gate",
                "evidence": list(task.evidence_requirements),
                "status": status,
                "confidence": max(0.0, 1.0 - max_uncertainty),
                "unresolved_conflicts": [],
            }],
        }


class AuditRecorder:
    def __init__(self) -> None:
        self.events: list[dict[str, Any]] = []

    def record(self, event_type: str, payload: dict[str, Any]) -> None:
        self.events.append({"event_type": event_type, "payload": payload})


class NeuralThinkingMachine:
    def __init__(self, registry: MachineRegistry, adapters: dict[str, ModelAdapter]) -> None:
        self.registry = registry
        self.adapters = adapters
        self.allocator = ComputationAllocator()
        self.verifier = VerificationGate()
        self.audit = AuditRecorder()

    def plan(self, task: TaskEnvelope) -> RouteDecision:
        decision = self.allocator.route(task)
        candidates = sorted(
            self.registry.by_capability(decision.capability),
            key=lambda machine: (-machine.reliability, machine.machine_id),
        )[: task.max_parallel]
        decision = RouteDecision(
            mode_ids=decision.mode_ids,
            machine_ids=tuple(machine.machine_id for machine in candidates),
            regime=decision.regime,
            capability=decision.capability,
            reason=decision.reason,
        )
        self.audit.record("ROUTE", {"task_id": task.task_id, "decision": decision.__dict__})
        return decision

    def execute(self, task: TaskEnvelope) -> tuple[list[DispatchResult], dict[str, Any]]:
        decision = self.plan(task)
        results: list[DispatchResult] = []
        input_hash = self._input_hash(task.input)
        chain_id = self._chain_id(task, input_hash)

        for machine_id in decision.machine_ids:
            machine = self.registry.get(machine_id)
            adapter = self.adapters.get(machine_id)
            if adapter is None:
                results.append(self._blocked(task, machine, "adapter_missing"))
                continue

            started = perf_counter()
            try:
                output = adapter.generate({
                    "task": task,
                    "mode_ids": decision.mode_ids,
                    "mode_names": [get_mode(mode_id).name for mode_id in decision.mode_ids],
                })
                results.append(DispatchResult(
                    request_id=task.request_id,
                    task_id=task.task_id,
                    machine_id=machine.machine_id,
                    role=machine.role,
                    model_ref=machine.model_ref,
                    output=output,
                    uncertainty=0.5,
                    status="OK",
                    latency_ms=(perf_counter() - started) * 1000,
                    input_hash=input_hash,
                    provenance={
                        "origin": "ntm-orchestrator",
                        "chain_id": chain_id,
                        "orchestration_version": task.context.get("version", "unknown"),
                    },
                    evidence_status="unverified",
                ))
            except Exception as exc:
                results.append(self._blocked(task, machine, str(exc)))

        verification = self.verifier.verify(results, task)
        self.audit.record("VERIFY", {"task_id": task.task_id, "verification": verification})
        self.audit.record("SELF_AUDIT", {
            "task_id": task.task_id,
            "executed_results": len(results),
            "verified": verification["accepted"],
            "uncertainty": verification.get("max_uncertainty"),
            "drift": None,
        })
        return results, verification

    @staticmethod
    def _input_hash(value: Any) -> str:
        return sha256(repr(value).encode("utf-8")).hexdigest()

    @staticmethod
    def _chain_id(task: TaskEnvelope, input_hash: str) -> str:
        seed = f"{task.request_id}:{task.task_id}:{input_hash}:{task.context.get('version', 'unknown')}"
        return sha256(seed.encode("utf-8")).hexdigest()

    @staticmethod
    def _blocked(task: TaskEnvelope, machine: MachineSpec, reason: str) -> DispatchResult:
        input_hash = NeuralThinkingMachine._input_hash(task.input)
        chain_id = NeuralThinkingMachine._chain_id(task, input_hash)
        return DispatchResult(
            request_id=task.request_id,
            task_id=task.task_id,
            machine_id=machine.machine_id,
            role=machine.role,
            model_ref=machine.model_ref,
            output=None,
            uncertainty=1.0,
            status="BLOCKED",
            latency_ms=0.0,
            input_hash=input_hash,
            provenance={
                "origin": "ntm-orchestrator",
                "chain_id": chain_id,
                "reason": reason,
                "orchestration_version": task.context.get("version", "unknown"),
            },
            evidence_status="unverified",
        )


def new_task(
    intent: dict[str, Any],
    input_data: Any,
    *,
    constraints: tuple[str, ...] = (),
    evidence_requirements: tuple[str, ...] = (),
    expected_output_schema: dict[str, Any] | None = None,
    max_steps: int = 8,
    max_parallel: int = 4,
    **context: Any,
) -> TaskEnvelope:
    request_id = str(uuid4())
    return TaskEnvelope(
        request_id=request_id,
        task_id=str(uuid4()),
        intent=intent,
        context={
            "project": "neural-thinking-machine",
            "component": "orchestrator",
            "version": "1.0.0",
            "process": "inference",
            "source": "HIG",
            **context,
        },
        input=input_data,
        constraints=constraints,
        evidence_requirements=evidence_requirements,
        expected_output_schema=expected_output_schema or {},
        max_steps=max_steps,
        max_parallel=max_parallel,
    )
