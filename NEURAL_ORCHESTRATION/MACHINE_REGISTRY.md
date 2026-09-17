# Machine Registry V1

The registry is the canonical inventory for logical reasoning machines. A machine is a role-bearing compute node, not necessarily a separate account.

| ID | Role | Function | Status |
|---|---|---|---|
| M001 | planner | task decomposition | planned |
| M002 | researcher | source discovery | planned |
| M003 | architect | system design | planned |
| M004 | coder | implementation | planned |
| M005 | math_reasoner | formal reasoning | planned |
| M006 | logic_critic | contradiction detection | planned |
| M007 | drift_analyst | drift detection | planned |
| M008 | verifier | evidence validation | planned |
| M009 | security_guard | guardrail review | planned |
| M010 | synthesizer | verified integration | planned |
| M011 | memory_manager | context/state binding | planned |
| M012 | execution_validator | execution verification | planned |

## Expansion
IDs M013–M100+ may be specialized without changing the protocol. Personality, prompt, model, and provider may vary; the shared machine contract may not.

## Required fields
`machine_id`, `role`, `provider`, `model_ref`, `version`, `capabilities`, `constraints`, `input_schema`, `output_schema`, `verification_policy`, `status`.

## Onboarding
An external machine is `connected` only after its adapter/configuration is installed and a health check succeeds. A registry entry alone is never evidence of a live connection.

## Copilot
GitHub Copilot custom agents are a valid implementation of machine profiles. Repository-level profiles live under `.github/agents/`; organization-level profiles can be provided through the organization's `.github` repository when available. One logical machine does not require one email/account.

## Security
Never place API keys, passwords, session tokens, recovery codes, or private credentials in this registry or repository.

## Status values
`planned`, `connected`, `verified`, `restricted`, `disabled`.
