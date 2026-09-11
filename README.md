# vector-index-ann-engine

Approximate Nearest Neighbor (ANN) vector indexing engine using HNSW graph algorithm in Python.

## Architecture & Design

This project implements a high-reliability distributed architecture designed for production workloads.
### Core Components
- `hnsw_graph`: Core subsystem handling specific domain logic, invariants, and performance guarantees.
- `distance_metrics`: Core subsystem handling specific domain logic, invariants, and performance guarantees.
- `quantization_pq`: Core subsystem handling specific domain logic, invariants, and performance guarantees.
- `index_serializer`: Core subsystem handling specific domain logic, invariants, and performance guarantees.
- `search_router`: Core subsystem handling specific domain logic, invariants, and performance guarantees.
- `dimension_reducer`: Core subsystem handling specific domain logic, invariants, and performance guarantees.

## Testing and Verification

Run the test suite via standard tooling.
