# Account and Thinking-Machine Onboarding

## What an email address does
An email can identify an account or receive an invitation. It does not by itself grant this system access to another account.

## Required access path
`ACCOUNT → AUTHENTICATION → PERMISSION → CONNECTOR/APP → CAPABILITY CHECK → MACHINE REGISTRY`

## For GitHub accounts
If an additional GitHub account is granted access to repositories in `tribal-archery`, the account can participate according to the permissions actually granted. GitHub supports repository roles such as Read, Triage, Write, Maintain and Admin.

## For additional AI/reasoning machines
The preferred pattern is a provider connector or API adapter. Each machine receives a bounded task and returns a structured result with provenance and uncertainty metadata.

## Never send credentials through chat
Do not paste API keys, passwords, recovery codes, session cookies or private tokens into conversation messages. Use the provider's secure connection/authentication flow or the appropriate secret store.

## Multi-account principle
Multiple accounts are treated as separate identities. Access is not inferred from an email address. The orchestrator must verify which account, repository, connector and permissions are actually available before dispatching work.

## Onboarding checklist
1. Identify account/provider.
2. Establish the intended role.
3. Grant only the required permission.
4. Connect the account through the supported integration.
5. Verify access without exposing secrets.
6. Register the machine/account capability.
7. Run a non-destructive health/test task.
8. Enable production dispatch only after verification.
9. Record provenance and scope.

## Principle
More machines increase available perspectives; they do not automatically increase truth. Independent verification remains mandatory.
