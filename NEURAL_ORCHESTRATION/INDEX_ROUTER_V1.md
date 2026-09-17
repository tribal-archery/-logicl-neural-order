# Index Router V1

## Role

The Index Router sits between the NTM and model adapters.

It resolves:

1. which agent index is relevant;
2. which project index is relevant;
3. which prior observations are required;
4. which conflicts must be surfaced;
5. which context should be sent to the model;
6. which new result should be written back.

## Runtime

`Task -> Intent -> Project -> Index Selection -> Retrieval -> Model Adapter -> Verification -> Index Write -> Brain of Brain`

## Hard rule

The model is never treated as the system's sole memory.

The index layer is the persistent continuity layer; the model is the reasoning/computation layer.

## Retrieval envelope

`request_id + task_id + index_ids + selected_entries + retrieval_reason + evidence_refs + conflict_refs`

## Write envelope

`request_id + task_id + target_index + entry_type + content + provenance + confidence + status`

## Verification

Index writes that contain claims about project state should pass through the same evidence/provenance and verification rules as ordinary model outputs.

## Scaling

For 1,000 logical agents:

`1,000 agents -> 1,000 role-specific index surfaces -> shared cross-agent index -> Brain-of-Brain index`

The system may physically co-locate indexes in one database or split them across stores. Logical separation is mandatory even when physical storage is shared.
