from NEURAL_ORCHESTRATION.quantum_bridge import (
    NODE_COUNT,
    QUBIT_COUNT,
    LocalSimulator,
    VariationalQuantumNeuralNetwork,
    QuantumProblem,
    build_variational_circuit,
    encode_nodes,
)


def test_231_nodes_are_encoded_into_8_qubits():
    nodes = [0.1] * NODE_COUNT
    angles = encode_nodes(nodes)
    assert len(angles) == QUBIT_COUNT
    circuit = build_variational_circuit(nodes, [0.0] * QUBIT_COUNT)
    assert circuit.qubit_count == 8
    assert circuit.encoding == "231_nodes_modulo_8"


def test_local_pipeline_produces_structural_verification():
    qnn = VariationalQuantumNeuralNetwork()
    result = qnn.forward([0.1] * NODE_COUNT, shots=128, adapter=LocalSimulator())
    assert len(result["nodes"]) == 231
    assert len(result["qubit_probabilities"]) == 8
    assert result["measurement"]["shots"] == 128
    assert result["verification"]["status"] == "VERIFIED"
    assert result["verification"]["physical_execution_proven"] is False


def test_evidence_contains_three_hashes():
    result = VariationalQuantumNeuralNetwork().forward([0.0] * NODE_COUNT)
    evidence = result["evidence"]
    assert len(evidence["problem_hash"]) == 64
    assert len(evidence["circuit_hash"]) == 64
    assert len(evidence["measurement_hash"]) == 64


def test_problem_rejects_wrong_node_count():
    problem = QuantumProblem(node_count=230)
    try:
        problem.validate()
    except ValueError:
        return
    raise AssertionError("expected node-count validation failure")
