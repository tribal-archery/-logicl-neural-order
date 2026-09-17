# Neural Orchestration Architecture V1

## Purpose
Build one coherent computational system from heterogeneous AI models and specialized agents using a shared rational-logic protocol.

## Fundamental definition
For this project, the AGI target is an engineering specification: a system that can allocate computation, route a problem to specialized reasoning nodes, integrate their results, verify them, maintain context and provenance, detect drift, and reconfigure its computation strategy without changing the system's core protocol.

This document defines architecture. Whether the resulting system satisfies the AGI definition remains an empirical evaluation question.

## Topology

USER / HIG
  -> PRIORITY KERNEL
  -> CONTEXT KERNEL
  -> INTENT KERNEL
  -> ORCHESTRATOR
  -> COMPUTATION ALLOCATION
  -> SPECIALIST NODE POOL
  -> CRITIC / VERIFIER
  -> SYNTHESIZER
  -> DECISION GATE
  -> NEURAL OS
  -> EXECUTION GATEWAY
  -> AUDIT / PROVENANCE
  -> HIG

## One-system invariant
A collection of models becomes one system when all participating nodes share:
- one task identity;
- one context-binding schema;
- one directive/state protocol;
- one evidence and provenance model;
- one verification contract;
- one drift taxonomy;
- one decision gate;
- one audit trail.

The models themselves remain replaceable.

## Computation Allocation
The Orchestrator maintains a task graph and assigns each subtask to one or more node classes according to:
- required capability;
- evidence requirements;
- uncertainty;
- expected information gain;
- cost/latency budget;
- dependency structure;
- verification requirement;
- observed historical reliability.

Independent subtasks may execute concurrently. Dependent subtasks wait for required verified state.

## Node classes
1. Planner
2. Researcher
3. Architect
4. Coder
5. Mathematical Reasoner
6. Logical Critic
7. Drift Analyst
8. Evidence Verifier
9. Security/Guardrail Reviewer
10. Synthesizer
11. Memory/Context Manager
12. Execution Validator

The registry is extensible to 100+ logical machines without changing the protocol.

## Shared result envelope
`request_id + task_id + machine_id + role + model_ref + input_hash + output + evidence_refs + uncertainty + usage + latency + status + provenance`

## Decision gate
No final system action is accepted until:
1. required evidence is present or uncertainty is explicitly recorded;
2. contradictions are surfaced;
3. the result satisfies the task schema;
4. authorization constraints are satisfied;
5. verification is complete at the required level;
6. provenance is intact.

## Replacement rule
Adding, removing, or swapping a model changes the compute layer only. It must not require rewriting the Neural OS, schemas, evidence chain, drift taxonomy, or decision gate.

## Iteration plan
V1: schemas + registry + orchestrator skeleton + audit.
V1.1: task graph + parallel dispatch.
V1.2: reliability-based routing.
V1.3: drift feedback loop.
V1.4: model/provider adapters.
V2: persistent memory and learned routing policy.
