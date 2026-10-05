# Repository architecture

This repository adopts the estate pattern used by larsbx/langlands-lab.
ESTATE.toml is the machine-readable source of layout and authority.

Ordering:

    authority -> mathematical concern -> implementation language

- kernel/ contains exact executable identities only.
- proof/ is authoritative for claim state.
- tests/ is finite evidence and never promotes a theorem.
- docs/ contains exposition, audits, and roadmap.
- tools/ enforces repository consistency.

The finite-math-kernels discipline applies: exact predicates stay exact,
bounded evidence stays bounded, and claim status must not drift from its record.
