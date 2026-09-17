# Neural Thinking Machine — Organization Orchestration Architecture V1

## Purpose
Build `tribal-archery` as the control plane for a multi-machine Thinking Machine architecture.

## Core pipeline
`INPUT → PRIORITY → CONTEXT → INTENT → SEMANTIC ROUTER → PROJECT ROUTER → EVIDENCE → CAPABILITY → ORCHESTRATOR → MACHINES → CRITIC/VERIFIER → SYNTHESIZER → SELF-AUDIT → RESPONSE`

## Machine roles
- `HIG`: Human Interaction Gateway; receives the user's request.
- `NTM-GATE`: Priority, Context and Intent gate.
- `ROUTER`: selects project, evidence sources and required capabilities.
- `ORCHESTRATOR`: decomposes work and dispatches bounded tasks.
- `ANALYST`: produces structured analysis.
- `CRITIC`: challenges assumptions and detects semantic/context/goal drift.
- `VERIFIER`: checks evidence, provenance and expected state.
- `SYNTHESIZER`: combines verified outputs without erasing disagreement.
- `AUDITOR`: records execution, drift and recovery events.
- `EXECUTION-GATE`: separates proposed actions from authorized actions.

## Existing project domains
1. Neural Thinking Machine
2. Neural OS
3. Brain Network
4. AI Drift Forensics
5. AI²³¹ Research
6. Ontometric Research
7. WANGA Computer / Infrastructure

## Machine contract
Every connected reasoning machine should expose, conceptually:
- machine_id
- provider
- model_id
- role_capabilities
- version
- status
- input_schema
- output_schema
- evidence_support
- uncertainty
- latency
- usage/cost metadata when available

## Execution rule
No machine result is treated as authoritative solely because it came from another model. Results enter the verification layer and retain provenance.

## Drift rule
Every orchestration cycle records:
`rule → interpretation → dispatch → machine output → verification → synthesis → action/result`

## Account/integration boundary
Credentials, API keys and passwords are never stored in repository files. They must remain in the provider's secure authentication mechanism or GitHub/GitHub Actions secrets where appropriate.

## Expansion model
Additional thinking machines are added through adapters, not by changing the core kernel:
`Provider Adapter → Machine Registry → Capability Match → Dispatch → Verification`

## Initial implementation sequence
1. Establish organization index.
2. Establish machine registry.
3. Establish task envelope and result envelope.
4. Establish provider adapters.
5. Establish critic/verifier path.
6. Establish audit record format.
7. Connect additional repositories and external machines only after capability and permission checks.
