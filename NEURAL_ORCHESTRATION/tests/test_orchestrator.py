from NEURAL_ORCHESTRATION.orchestrator import (
    MachineRegistry,
    MachineSpec,
    NeuralThinkingMachine,
    new_task,
)


class EchoAdapter:
    def generate(self, request):
        return {
            "modes": request["mode_ids"],
            "mode_names": request["mode_names"],
            "ok": True,
        }


def build_ntm():
    machines = [
        MachineSpec("M004", "coder", "mock-code", frozenset({"code"}), 0.9),
        MachineSpec("M005", "math_reasoner", "mock-math", frozenset({"formal_reasoning"}), 0.9),
        MachineSpec("M008", "verifier", "mock-verifier", frozenset({"verification"}), 0.85),
        MachineSpec("M001", "planner", "mock-general", frozenset({"general_reasoning"}), 0.8),
        MachineSpec("M007", "drift_analyst", "mock-search", frozenset({"search"}), 0.7),
    ]
    registry = MachineRegistry(machines)
    adapters = {machine.machine_id: EchoAdapter() for machine in machines}
    return NeuralThinkingMachine(registry, adapters)


def test_code_routes_to_neuro_symbolic_modes():
    ntm = build_ntm()
    task = new_task({"action": "develop code", "object": "algorithm"}, "x = 1")
    results, verification = ntm.execute(task)
    assert results[0].machine_id == "M004"
    assert 15 in results[0].output["modes"]
    assert verification["accepted"] is True


def test_high_uncertainty_routes_to_verifier():
    ntm = build_ntm()
    task = new_task(
        {"action": "analyze", "object": "uncertain system"},
        "ambiguous",
        uncertainty=0.9,
        dispersion=0.4,
    )
    results, verification = ntm.execute(task)
    assert results[0].machine_id == "M008"
    assert 2 in results[0].output["modes"]
    assert verification["accepted"] is True


def test_missing_adapter_is_blocked():
    registry = MachineRegistry([
        MachineSpec("M001", "planner", "missing", frozenset({"general_reasoning"}), 0.9)
    ])
    ntm = NeuralThinkingMachine(registry, {})
    task = new_task({"action": "analyze", "object": "task"}, "data")
    results, verification = ntm.execute(task)
    assert results[0].status == "BLOCKED"
    assert results[0].provenance["chain_id"]
    assert verification["accepted"] is False


def test_route_and_verification_are_audited():
    ntm = build_ntm()
    task = new_task({"action": "analyze", "object": "task"}, "data")
    ntm.execute(task)
    assert [event["event_type"] for event in ntm.audit.events] == [
        "ROUTE",
        "VERIFY",
        "SELF_AUDIT",
    ]


def test_provenance_chain_is_deterministic_for_same_task():
    ntm = build_ntm()
    task = new_task({"action": "analyze", "object": "task"}, "same-data")
    first, _ = ntm.execute(task)
    second, _ = ntm.execute(task)
    assert first[0].input_hash == second[0].input_hash
    assert first[0].provenance["chain_id"] == second[0].provenance["chain_id"]


def test_evidence_requirement_is_exposed_in_verification():
    ntm = build_ntm()
    task = new_task(
        {"action": "analyze", "object": "claim"},
        "claim-data",
        evidence_requirements=("evidence://source-1",),
    )
    results, verification = ntm.execute(task)
    assert results[0].evidence_status == "unverified"
    assert verification["verification_status"] == "unverified"
    assert verification["accepted"] is False
