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
- `CONTACT_AND_COLLABORATION.md` — public route for technical, research, and partnership inquiries.

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

## Strategic value thesis

The project deliberately separates **current technical evidence** from **future strategic value**.

The opening strategic value scenario for a fully demonstrated system is framed at **$1 trillion**. This is a long-term scenario, not a present market valuation.

The $1T figure is therefore treated as a **starting strategic valuation thesis, not a ceiling**. If a working prototype demonstrates a genuinely differentiated architecture, measurable general capability, scientific verification, reliability, provenance, orchestration, and scalable enterprise utility, higher multi-trillion-dollar scenarios can be evaluated.

The commercial thesis is based on **strategic urgency**, not an assumption that every company will automatically sign a contract. If the system creates a material competitive advantage, organizations may have strong incentives to evaluate, integrate, license, partner with, or otherwise obtain access to the capability before competitors do.

Any future valuation must remain evidence-based and should be updated using:
- working-model performance;
- independent evaluation;
- reproducibility;
- enterprise adoption;
- revenue and contract evidence;
- infrastructure/scaling economics;
- defensibility and switching costs;
- measurable competitive advantage.

### Scientific-value layer

A central research objective is to connect AI capability with a rigorous evidence and verification layer. The broader vision includes a digital value mechanism whose basis would be **scientifically measurable and auditable properties**, rather than an unsupported financial claim.

This is a research architecture and future-value thesis. It is not a claim that such a valuation, currency, market position, or scientific superiority has already been established.

## Scope

This repository documents and implements an evolving research architecture. It does not by itself establish that the resulting system is AGI, autonomous, production-ready, or independently validated. Those are empirical and engineering questions.

## Security

Do not commit API keys, passwords, access tokens, recovery codes, session cookies, or private credentials. See [SECURITY.md](SECURITY.md).

## Development status

The current branch contains the V1 orchestration skeleton and supporting documentation. Provider adapters, parallel task execution, persistent audit storage, learned routing, and broader verification remain roadmap work.

## Funding and collaboration

The project is seeking qualified research funding and technical/scientific collaboration. The platform is not being offered for sale as a whole through this repository. See [INVESTOR_BRIEF_V1.md](INVESTOR_BRIEF_V1.md) for the current internal funding position and valuation scenarios.

For organizations interested in technical or research collaboration, use the public contact route in [CONTACT_AND_COLLABORATION.md](CONTACT_AND_COLLABORATION.md).

## Maintainer

The repository is maintained by the `tribal-archery` organization.
