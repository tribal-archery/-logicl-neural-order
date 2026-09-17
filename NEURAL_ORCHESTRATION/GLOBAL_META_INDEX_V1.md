# Global Index Engine V1

## Purpose
The Neural Thinking Machine contains a supervisory index whose job is to continuously index the indexes of the system.

It is not a second copy of every conversation. It is a meta-index over distributed memory surfaces.

## Hierarchy
Conversation -> Model Index -> Agent Index -> Project/Cross-Agent Index -> Global Meta-Index -> Brain of Brain

## Continuous lifecycle
INGEST -> CLASSIFY -> HASH -> LINK -> SUMMARIZE -> DETECT_CONFLICT -> UPDATE_META_INDEX -> VERIFY -> REFRESH

A new event does not require rewriting the entire index tree. Only affected paths and summaries are refreshed.

## Meta-index record
- index_id
- parent_index_id
- agent_id
- project_id
- entry_type
- semantic_keys
- temporal_keys
- related_indexes
- evidence_refs
- conflict_refs
- freshness
- content_hash
- last_indexed_at
- status

## Freshness
Each lower-level index exposes a version and last-update marker.

`index_version -> last_indexed_version -> dirty_state`

If a lower-level index changes, the affected meta-index path becomes dirty and is refreshed.

## Consistency
The meta-index never silently resolves contradictions. A conflict produces an explicit linked conflict record and can trigger targeted verification.

## Retrieval
For a task, the Brain of Brain queries the meta-index first:

`task -> relevant projects -> relevant agents -> relevant indexes -> relevant entries`

Only selected context is loaded into the reasoning stage.

## Scale
For 1,000 logical agents:

`1,000 Agent Indexes -> Domain Indexes -> Cross-Agent Index -> Project Indexes -> Global Meta-Index`

## Architectural invariant
The NTM communicates with the memory topology through indexes, not through raw conversation replay.