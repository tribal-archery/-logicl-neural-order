# 32 x 28 connecting orchestrator

## Purpose
Connect the 32-root linear control plane to the 28-node circular control plane without merging their semantics.

### Contract
1. Linear side emits ordered root events.
2. Circular side receives those events as state transitions.
3. Circular side emits recurrence, boundary and persistence observations.
4. Connecting logic reconciles the two representations.
5. A mismatch is recorded, not silently normalized.
6. Canonicalization and provenance seal the final artifact.

### Matrix
Rows: 32 roots.
Columns: 28 orchestration nodes.
Cell: {root_id, mode_id, input_schema, output_schema, validator, provenance}.

### No hidden claim
The 32-root mapping is the project research mapping. The 28-node side is an implementation architecture derived from the existing NTM orchestration pipeline and Place-aware controls.
