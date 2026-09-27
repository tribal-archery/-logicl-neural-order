# Logic-4 / מ — מח

Current implementation target.

The Hebrew-letter layer is the grammatical prefix מ. The engineering network treats the prefix as a typed symbolic operator whose interpretation is conditioned by lexical, syntactic, semantic, and project context.

## Fourth-order neural architecture
Input tensor: X[b, context, token, feature]

1. Symbol encoder — identifies מ and its token boundary.
2. Morphosyntactic encoder — represents attachment and local syntax.
3. Semantic-context encoder — represents the relation contributed by the prefix.
4. Validation/gating block — checks schema, provenance, and compatibility.
5. Deep residual stack — repeated learned transformations while preserving the four-axis representation.
6. Output head — emits a typed mem_event rather than an untyped embedding.

Output contract:
mem_event = { letter: "מ", mode: "logic4", tensor_order: 4, input_ref, output_ref, grammatical_features, semantic_features, confidence, validator_status, provenance }

## Branch rule
Only the מ network is designated as active for the current implementation. ב/כ/ל remain architectural peers until explicitly activated.

## Epistemic boundary
The grammatical fact used here is that ב, כ, ל, מ are inseparable Hebrew prepositions. The neural-network architecture is an engineering construction, not a claim about traditional Hebrew grammar.