# Data Model

ProducitonLine (1) ---- (N) Machine
Machine (1) ---- (N) MachineStatus
Machine (1) ---- (N) ProductionEvent

## Design Decisions

- Relational database was chosen for data consistency and traceability.
- Status history is stored separately to allow downtime analysis.
- Production events are stored per machine to support KPI calculation.
