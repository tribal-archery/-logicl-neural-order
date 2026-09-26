from NEURAL_ORCHESTRATION.orchestrator import (
    MachineRegistry,
    MachineSpec,
    NeuralThinkingMachine,
    new_task,
)
from NEURAL_ORCHESTRATION.quantum_bridge import QuantumNeuralAdapter, NODE_COUNT


def test_quantum_route_uses_qnn_adapter():
    machine = MachineSpec(
        "QNN001",
        "quantum_neural",
        "local-qnn",
        frozenset({"quantum_neural"}),
        reliability=0.95,
    )
    ntm = NeuralThinkingMachine(
        MachineRegistry([machine]),
        {"QNN001": QuantumNeuralAdapter()},
    )
    task = new_task(
        {"action": "run quantum neural network", "object": "231-node bridge"},
        [0.1] * NODE_COUNT,
    )
    results, verification = ntm.execute(task)
    assert results[0].status == "OK"
    assert len(results[0].output["nodes"]) == 231
    assert len(results[0].output["qubit_probabilities"]) == 8
    assert results[0].output["verification"]["status"] == "VERIFIED"
    assert verification["accepted"] is True
