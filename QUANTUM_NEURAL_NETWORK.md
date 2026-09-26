# Quantum Neural Network Integration

## Status

SPECIFIED / LOCAL-PROTOTYPED

This layer integrates the supplied Quantum Bridge specification into the Neural
Thinking Machine without treating a local simulator as physical evidence.

## Architecture

231 logical nodes
  -> explicit node_to_qubit mapping
  -> 8-qubit encoding
  -> variational RY layer + CNOT ring
  -> local simulator or declared provider adapter
  -> measurement normalization
  -> projection back to 231 logical nodes
  -> Evidence Artifact
  -> structural Verification Gate

The implementation therefore has 231 logical inputs and 8 target/simulated
qubits. It does not assert 231 physical qubits.

## Verification boundary

VERIFIED means the structural and local computational checks passed. It does
not mean that:
- physical quantum execution occurred;
- a cloud provider accepted or executed the circuit;
- the model is experimentally validated;
- the network demonstrates AGI or any other capability beyond the tested computation.

IBM, Microsoft Azure Quantum, and Google/Cirq adapters are explicit and fail
closed until a real provider integration is configured and reports execution.

## Neural layer

VariationalQuantumNeuralNetwork provides:
- 231 logical node inputs;
- 8 classical variational weights;
- an 8-qubit circuit representation;
- measurement-derived qubit probabilities;
- projection back to 231 node outputs;
- an optional finite-difference training step.

## Evidence

Every forward pass produces:
- problem hash;
- circuit hash;
- measurement hash;
- execution domain;
- verification status.

This preserves the repository rule that capabilities are not claimed as
connected unless they have actually been verified.
