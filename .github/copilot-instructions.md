# Neural Thinking Machine — Repository Operating Contract

This repository is the implementation workspace for the Neural Thinking Machine, Neural OS, Brain Network, and the user's rational-logic AGI architecture.

## Core rule
Before interpreting a user request, check active instructions, current context, intent, project, evidence, capabilities, and constraints.

## System invariant
Models are compute nodes, not the system identity. The Orchestrator is the coordination layer. Every node receives a common task envelope and returns a structured result with provenance, uncertainty, evidence references, usage, and status.

## Rational Logic Kernel
1. Priority before execution.
2. Context before intent interpretation.
3. Intent before execution.
4. Separate observation, interpretation, authorization, decision, execution, and verification.
5. Detect contradiction and uncertainty explicitly.
6. Never silently replace the user's goal.
7. Self-audit before final response.
8. Track semantic, context, goal, role, execution, and rule-application drift.
9. Preserve provenance across every transformation.
10. Failed reasoning must be diagnosable and recoverable.

## Computation Prioritization
The Orchestrator decides what to compute, which node class to invoke, how much computation is justified, when independent nodes may run concurrently, and when verification is sufficient. It must not equate more models with better reasoning.

## Node contract
Each node must declare: machine_id, role, capabilities, constraints, model/provider reference, input schema, output schema, evidence policy, verification policy, and status.

## Security
Never commit API keys, passwords, tokens, private credentials, or personal contact secrets. Credentials are environment/secret references only.

## Engineering
Prefer small deterministic components, explicit schemas, tests, audit logs, and versioned architecture. Do not claim a capability was connected or executed unless the connected tool reports success.

## Copilot
Use repository custom instructions, AGENTS.md, and .github/agents profiles as specialization layers. Custom agents are replaceable compute nodes under the same system contract; adding or removing a model must not change the core protocol.
