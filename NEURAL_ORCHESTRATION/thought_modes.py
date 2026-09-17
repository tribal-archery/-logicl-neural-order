"""Neural Thinking Machine: 28 cognitive thought modes.

These are orchestration strategies, not claims that an LLM literally exposes
these internal mechanisms. The orchestrator selects and composes them.
"""

from dataclasses import dataclass
from enum import Enum


class ModeFamily(str, Enum):
    LINEAR_STRUCTURAL = "linear_structural"
    SEARCH_BRANCHING = "search_branching"
    LOGICAL_SYMBOLIC = "logical_symbolic"
    CRITICAL_METACOGNITIVE = "critical_metacognitive"
    CREATIVE_SIMULATIVE = "creative_simulative"


@dataclass(frozen=True)
class ThoughtMode:
    mode_id: int
    name: str
    family: ModeFamily
    primary_capability: str
    verification_level: str


THOUGHT_MODES = [
    ThoughtMode(1, "Linear CoT", ModeFamily.LINEAR_STRUCTURAL, "sequential_reasoning", "basic"),
    ThoughtMode(2, "Least-to-Most", ModeFamily.LINEAR_STRUCTURAL, "decomposition", "basic"),
    ThoughtMode(3, "Backward Chaining", ModeFamily.LINEAR_STRUCTURAL, "goal_driven_reasoning", "causal"),
    ThoughtMode(4, "Hierarchical HTN", ModeFamily.LINEAR_STRUCTURAL, "hierarchical_planning", "structural"),
    ThoughtMode(5, "First Principles", ModeFamily.LINEAR_STRUCTURAL, "axiomatic_deconstruction", "structural"),
    ThoughtMode(6, "Temporal Causal Graph", ModeFamily.LINEAR_STRUCTURAL, "causal_temporal_reasoning", "causal"),
    ThoughtMode(7, "Tree of Thoughts", ModeFamily.SEARCH_BRANCHING, "state_space_search", "search"),
    ThoughtMode(8, "Graph of Thoughts", ModeFamily.SEARCH_BRANCHING, "nonlinear_reasoning_graph", "graph"),
    ThoughtMode(9, "Self-Consistency", ModeFamily.SEARCH_BRANCHING, "parallel_sampling", "consensus"),
    ThoughtMode(10, "Divergent-Convergent", ModeFamily.SEARCH_BRANCHING, "divergence_reconciliation", "consensus"),
    ThoughtMode(11, "Heuristic Pruning", ModeFamily.SEARCH_BRANCHING, "candidate_pruning", "heuristic"),
    ThoughtMode(12, "MoE Tail Diversity", ModeFamily.SEARCH_BRANCHING, "controlled_diversity", "heuristic"),
    ThoughtMode(13, "Formal Deduction", ModeFamily.LOGICAL_SYMBOLIC, "formal_proof", "formal"),
    ThoughtMode(14, "Abduction", ModeFamily.LOGICAL_SYMBOLIC, "best_explanation", "probabilistic"),
    ThoughtMode(15, "Neuro-Symbolic Execution", ModeFamily.LOGICAL_SYMBOLIC, "executable_constraints", "hard"),
    ThoughtMode(16, "Analogical Transfer", ModeFamily.LOGICAL_SYMBOLIC, "structural_transfer", "semantic"),
    ThoughtMode(17, "Bayesian Updating", ModeFamily.LOGICAL_SYMBOLIC, "hypothesis_update", "probabilistic"),
    ThoughtMode(18, "Proof by Contradiction", ModeFamily.LOGICAL_SYMBOLIC, "contradiction_proof", "formal"),
    ThoughtMode(19, "Inductive Generalization", ModeFamily.LOGICAL_SYMBOLIC, "pattern_generalization", "empirical"),
    ThoughtMode(20, "Spatial Simulation", ModeFamily.LOGICAL_SYMBOLIC, "spatial_reasoning", "simulation"),
    ThoughtMode(21, "Iterative Self-Refine", ModeFamily.CRITICAL_METACOGNITIVE, "critique_revision", "review"),
    ThoughtMode(22, "Socratic Dialectic", ModeFamily.CRITICAL_METACOGNITIVE, "thesis_antithesis_synthesis", "review"),
    ThoughtMode(23, "Adversarial Red Team", ModeFamily.CRITICAL_METACOGNITIVE, "failure_generation", "adversarial"),
    ThoughtMode(24, "Counterfactual", ModeFamily.CRITICAL_METACOGNITIVE, "scenario_intervention", "causal"),
    ThoughtMode(25, "Metacognitive Budget", ModeFamily.CRITICAL_METACOGNITIVE, "compute_allocation", "control"),
    ThoughtMode(26, "Episodic Reflection", ModeFamily.CRITICAL_METACOGNITIVE, "failure_recall", "memory"),
    ThoughtMode(27, "Lateral Association", ModeFamily.CREATIVE_SIMULATIVE, "creative_association", "heuristic"),
    ThoughtMode(28, "Multi-Agent Perspective", ModeFamily.CREATIVE_SIMULATIVE, "perspective_simulation", "multi_agent"),
]

MODE_BY_ID = {mode.mode_id: mode for mode in THOUGHT_MODES}


def get_mode(mode_id: int) -> ThoughtMode:
    return MODE_BY_ID[mode_id]
