# Agent Profile Schema V1

Every logical agent receives a private role definition.

## Required profile

```yaml
agent_id: M###
domain: D##
role: specialist
mission: precise domain mission
private_instruction: scope-limited reasoning instruction
capabilities: []
evidence_policy:
  required: true
  minimum_refs: 0
output_schema:
  claim: string
  evidence_refs: array
  reasoning_summary: string
  uncertainty: number
  conflicts: array
  dependencies: array
verification_level: standard
status: planned
```

## Private-instruction boundary
A private instruction may specialize an agent, but it may not override system-level safety, invent evidence, suppress contradictions, bypass authorization, conceal provenance, turn estimates into verified facts, or claim institutional authority.

## Diversity dimensions
1. domain
2. question type
3. evidence source
4. reasoning method
5. criticism style
6. verification depth
7. temporal scope
8. mathematical vs qualitative orientation
9. implementation perspective
10. cross-domain bridge function