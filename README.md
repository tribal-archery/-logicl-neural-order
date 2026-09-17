# Neural Thinking Machine / WANGA

A research and engineering workspace for a provider-neutral Neural Thinking Machine (NTM) architecture.

## What this repository contains

The project is building a coordination layer above individual AI models. Models are treated as replaceable compute nodes; the system identity lives in the shared protocol, orchestration, verification, provenance, and audit layers.

Core pipeline:

`Priority → Context → Intent → Semantic Routing → Project → Evidence → Capability → Orchestrator → Machines → Critic/Verifier → Synthesizer → Decision Gate → Neural OS → Execution → Audit/Provenance → Self-Audit`

## Current implementation

- 28 explicit reasoning/orchestration modes.
- Deterministic V1 computation allocation.
- Task and result envelopes.
- Machine registry with capability-based routing.
- Provider-neutral model adapter interface.
- Verification gate.
- Audit recorder.
- Provenance and input hashing.
- Automated orchestration tests.
- Architecture and onboarding documentation.

The M100+ registry is a scaling target for logical machines. It does **not** mean that 100 live model connections are currently deployed.

## Repository map

- `NEURAL_ORCHESTRATION/` — executable orchestration kernel, schemas, registry, tests, and architecture.
- `AGENTS.md` — agent execution contract.
- `.github/copilot-instructions.md` — repository operating contract.
- `.github/agents/` — specialized agent profiles.
- `ORGANIZATION_INDEX.md` — organization-level architecture index.
- `INVESTOR_BRIEF_V1.md` — research/funding positioning and internal valuation scenarios.

## Design principles

1. Priority before execution.
2. Context before intent interpretation.
3. Intent before computation.
4. Observation is distinct from interpretation.
5. Evidence and provenance travel with results.
6. Verification is separate from generation.
7. Model/provider identity is replaceable.
8. Failed computation must be diagnosable.
9. Drift is recorded rather than silently normalized.
10. No capability is claimed as connected unless it has actually been verified.

## Scope

This repository documents and implements an evolving research architecture. It does not by itself establish that the resulting system is AGI, autonomous, production-ready, or independently validated. Those are empirical and engineering questions.

## Security

Do not commit API keys, passwords, access tokens, recovery codes, session cookies, or private credentials. See [SECURITY.md](SECURITY.md).

## Development status

The current branch contains the V1 orchestration skeleton and supporting documentation. Provider adapters, parallel task execution, persistent audit storage, learned routing, and broader verification remain roadmap work.

## Funding and collaboration

The project is seeking qualified research funding and technical/scientific collaboration. The platform is not being offered for sale as a whole through this repository. See [INVESTOR_BRIEF_V1.md](INVESTOR_BRIEF_V1.md) for the current internal funding position and valuation scenarios.

## Maintainer

The repository is maintained by the `tribal-archery` organization.
