# Model Index Architecture V1

## Objective

The Neural Thinking Machine should not depend on repeatedly handing a model its entire conversation history.

Instead, each connected model/agent receives a persistent **Model Index** that organizes its own interaction history into a structured, queryable memory surface.

The NTM communicates with the index layer first:

`NTM -> Agent/Model Index -> Targeted Context -> Model -> Indexed Observation -> NTM`

The model remains a replaceable compute engine. The index is the continuity interface.

## Per-model index

Every model node may maintain:

- model identity and version;
- agent identity;
- project memberships;
- conversation/session identifiers;
- chronological events;
- durable facts;
- decisions;
- unresolved questions;
- evidence references;
- code/repository references;
- previous outputs;
- contradictions;
- drift events;
- confidence/uncertainty;
- provenance hashes.

## Index layers

### L0 — Session index

Immediate conversation state.

### L1 — Project index

All sessions associated with one project.

### L2 — Agent index

The accumulated role-specific knowledge of one logical agent.

### L3 — Cross-agent index

Links relevant observations between specialist agents.

### L4 — Brain-of-Brain index

The supervisory index containing synthesized state, unresolved conflicts, verification status, and task history.

## Retrieval rule

The NTM should retrieve the **smallest sufficient context** rather than inject the entire history.

Retrieval is based on:

`intent + project + agent_id + entities + time + evidence_need + unresolved_conflicts`

## Write rule

A conversation turn is not automatically promoted to durable memory.

The write path classifies content into:

- transient context;
- reusable knowledge;
- decision;
- evidence;
- unresolved issue;
- contradiction;
- drift event.

Only material worth retaining is promoted to the appropriate index layer.

## Conflict rule

New information is compared with existing indexed information before promotion.

A contradiction must create an explicit conflict record rather than silently overwriting the previous state.

## Provenance rule

Every durable index entry carries:

`source_session + source_message + timestamp + agent_id + model_ref + content_hash`

## Privacy and access

Indexes are logically scoped. An agent may access only indexes authorized for its role and task.

Do not store credentials, secrets, or unnecessary private personal data in model indexes.

## Why this matters

This architecture creates the direct relationship the NTM needs:

**NTM does not ask every model to remember everything. NTM asks the model's index what is relevant, retrieves the required state, then invokes the model.**

Recent memory research similarly emphasizes structured, selective retrieval and conflict-aware long-term memory rather than indiscriminate full-history replay. citeturn0search0turn0search1turn0academia14
