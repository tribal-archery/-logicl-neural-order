"""Minimal executable demo for the 231-node / 8-qubit QNN."""
from __future__ import annotations

from .quantum_bridge import NODE_COUNT, VariationalQuantumNeuralNetwork


def main() -> None:
    network = VariationalQuantumNeuralNetwork()
    inputs = [0.25 if i % 3 == 0 else 0.0 for i in range(NODE_COUNT)]
    result = network.forward(inputs, shots=128)
    print("nodes:", len(result["nodes"]))
    print("qubits:", len(result["qubit_probabilities"]))
    print("shots:", result["measurement"]["shots"])
    print("verification:", result["verification"]["status"])
    print("physical_execution_proven:", result["verification"]["physical_execution_proven"])
    print("evidence:", result["evidence"])


if __name__ == "__main__":
    main()
