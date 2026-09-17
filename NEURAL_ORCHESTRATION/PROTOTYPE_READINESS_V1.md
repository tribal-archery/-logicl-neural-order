# Prototype Readiness V1

## Objective
Move the Neural Thinking Machine (NTM) from architecture documentation to a measurable executable prototype.

The prototype must demonstrate the core loop:
Task → Priority → Context → Intent → Project → Evidence → Capability → Machine Selection → Execution → Verification → Synthesis → Decision → Provenance → Self-Audit

## Definition of Done

A prototype milestone is complete only when:

1. The orchestration kernel accepts a structured task.
2. The task is classified into intent and project context.
3. Relevant evidence is retrieved or explicitly marked unavailable.
4. Capability requirements are derived before execution.
5. A machine/model adapter is selected deterministically.
6. The selected machine produces a structured result.
7. A separate verification step evaluates the result.
8. Provenance and input hashes are recorded.
9. Contradictions and uncertainty are preserved rather than silently normalized.
10. A final self-audit records what was executed, what was verified, what remains uncertain, and where drift occurred.

## Prototype Components

### P0 — Kernel
Use the existing orchestration kernel as the execution spine.
Required artifacts: task envelope, result envelope, machine registry, routing logic, verification gate, audit recorder.

### P1 — Deterministic routing
Implement a deterministic routing test in which the same task, context, evidence set, and capability registry produce the same machine-selection decision.
Record: input hash, routing decision, selected capability, selected machine, routing version.

### P2 — Evidence layer
Every non-trivial conclusion must carry an evidence status: verified, supported, inferred, unverified, or contradicted.
The prototype must never silently convert an inference into a verified fact.

### P3 — Verification layer
The verifier must be logically separate from the generator.
Minimum output: claim → evidence → verification_status → confidence → unresolved_conflicts.

### P4 — Provenance
Every prototype result should be traceable to task ID, session ID, model/machine ID, model/version reference when available, source/evidence references, timestamp, content hash, and orchestration version.

### P5 — Drift detection
Introduce a minimal drift record: expected_behavior → observed_behavior → difference → drift_type → evidence → severity → recovery.
Initial drift types: semantic, execution, context, capability, evidence, goal, role.

### P6 — Model Index
The model index is the continuity layer, not the model itself.
Minimum indexed records: durable facts, decisions, unresolved questions, evidence references, contradictions, drift events, provenance, confidence/uncertainty.

### P7 — Global Meta-Index
The Meta-Index should reference model/agent/project indexes without duplicating their complete contents.
Minimum responsibilities: index discovery, cross-index linking, conflict references, freshness state, routing to specialized indexes.

## First End-to-End Demonstration

The first demonstration should be intentionally small.

Input: Evaluate a technical claim using a supplied evidence set.

Expected path: parse task → identify intent → identify project → retrieve evidence → identify required capability → route to a machine → generate a result → verify independently → record provenance → run self-audit → return result with evidence and uncertainty.

## Measurable Prototype Metrics

Report routing determinism, evidence attachment rate, verification coverage, provenance completeness, contradiction preservation, drift detection rate, false-verification rate, reproducibility, and execution latency.

No strategic valuation claim should be treated as technically validated until these measurements exist.

## Strategic Value Boundary

The repository may describe the $1T figure as a long-term strategic valuation scenario, but the prototype must remain evidence-first.

The causal chain is:
Working prototype → measurable capability → independent verification → reproducibility → real usage → enterprise adoption → economic evidence → valuation scenario.

The prototype does not assume that companies will automatically purchase the system. The testable commercial thesis is that sufficiently differentiated capability may create competitive urgency.

## Overnight Build Sequence

1. Inspect current kernel and schemas.
2. Implement or complete the smallest deterministic routing path.
3. Add an end-to-end prototype test.
4. Add provenance output.
5. Add verification output.
6. Add a minimal drift record.
7. Run the existing test suite.
8. Record remaining blockers.
9. Update the architecture index only after the executable path is verified.

## Stop Conditions

Do not claim prototype completion if execution is simulated but not actually performed; verification is identical to generation; provenance is missing; evidence status is ambiguous; tests are failing; required model/provider connections are only assumed; or a future capability is described as already deployed.

## Current Status

This document defines the readiness gate. It does not claim that every item above is already implemented.