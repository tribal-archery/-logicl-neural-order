# Logic-4 / בכ״ל מ״ם — Four-Network Architecture

## Source-level grammatical layer
ב, כ, ל, מ are treated here as the four inseparable Hebrew prepositions (אותיות בכל״ם).

## Engineering layer
Each letter is assigned an independent deep-neural branch. The four networks share a common fourth-order tensor interface but retain separate parameters and validation state.

| Network | Branch | Current state |
|---|---|---|
| ב | logic4/bet | scaffold |
| כ | logic4/kaf | scaffold |
| ל | logic4/lamed | scaffold |
| מ | logic4/mem | active target |

## Fourth-order contract
All four networks use the same logical tensor signature:

X[b, context, token, feature]

The fourth order is an engineering abstraction: it means the model preserves four explicit axes through the network. It is not a historical grammatical category.

## Routing
1. Tokenizer identifies a בכ״ל מ״ם prefix.
2. Router selects the letter branch.
3. Letter network performs deep representation and validation.
4. Network emits a typed event.
5. Integration layer reconciles events without collapsing letter identity.
6. Provenance records the exact branch and model version.

## M-first execution
For the present phase, only מ is activated for execution. The other three branches are connected at the registry level but remain inactive.

## Interface
prefix_event -> logic4_router -> letter_network(ב|כ|ל|מ) -> validator -> provenance -> 32/28 bridge

## Relation to the existing 32+28 system
The four Logic-4 networks are an additional linguistic micro-architecture. They do not replace the 32-root layer or the 28-node circular orchestration layer. The bridge receives their typed events as external structured inputs.
