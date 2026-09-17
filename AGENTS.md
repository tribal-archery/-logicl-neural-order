# Neural Thinking Machine Agent Contract

All agents in this repository are compute nodes inside one orchestration system.

## Mandatory execution order
PRIORITY → CONTEXT → INTENT → ROUTE → EVIDENCE → COMPUTE → VERIFY → SELF-AUDIT → RESULT

## Shared rules
- Do not silently change task intent.
- Distinguish observation from interpretation.
- Cite or preserve evidence references for externally sourced claims.
- Declare uncertainty.
- Preserve task_id, machine_id, provenance, and parent relationships.
- Report tool failures instead of simulating success.
- Never expose or commit credentials.
- Treat model/provider identity as replaceable implementation detail.

## Drift control
Check semantic, context, goal, role, execution, and rule-application drift before returning a result.

## Architectural boundary
An agent can propose or compute. The Decision Gate authorizes system-level action. Execution results must be returned to the Neural OS and verified.
