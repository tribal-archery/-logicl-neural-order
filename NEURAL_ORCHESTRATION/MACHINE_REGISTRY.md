# Machine Registry V1

This registry is the canonical inventory for connected reasoning machines.

| Machine ID | Provider | Role | Status | Evidence | Notes |
|---|---|---|---|---|---|
| NTM-CORE | Internal | Priority/Context/Intent gate | planned | architecture spec | Core control logic |
| NTM-ORCH | Internal | Orchestrator | planned | architecture spec | Task decomposition and dispatch |
| NTM-CRITIC | Internal | Critic | planned | architecture spec | Drift and assumption challenge |
| NTM-VERIFY | Internal | Verifier | planned | architecture spec | Evidence/provenance validation |
| NTM-SYNTH | Internal | Synthesizer | planned | architecture spec | Verified multi-machine synthesis |
| NTM-AUDIT | Internal | Auditor | planned | architecture spec | Execution and drift records |

## External machine onboarding
An external machine is added only after these fields are known:

- provider/account identifier
- model identifier
- allowed role(s)
- supported input/output schema
- authentication status (never the secret itself)
- permission scope
- rate/usage constraints when available
- verification requirements
- provenance mechanism

## Status values
- `planned`
- `connected`
- `verified`
- `restricted`
- `disabled`

## Security rule
Never place API keys, passwords, session tokens, recovery codes, or private credentials in this registry or any repository file.
