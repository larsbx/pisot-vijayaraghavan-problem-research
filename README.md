# Pisot–Vijayaraghavan problem research

Research estate for the classical Pisot–Vijayaraghavan problem.

If α>1 and ||λ α^n||→0 for some λ≠0, must α be algebraic (hence Pisot)?

**Current status:** open. This repository does **not** claim a solution.

Start with ESTATE.toml, docs/dossier.md, proof/claims.toml,
docs/audit/THREAD_AUDIT_2026-10-05.md, and docs/roadmap.md.

The layout follows the estate pattern used by larsbx/langlands-lab. The
exact-arithmetic and provenance discipline follows larsbx/finite-math-kernels:
bounded computation stays bounded, imported results stay imported, and failed
proofs are withdrawn rather than silently weakened.

## Current banked mathematics

The audited thread retains the PV-to-defect reduction, the third-Hankel
Dodgson identity, the square-root barrier, exact gcd normalization and
freshness, the transport congruence as a shadow identity, and the exact
two-step-return transplant. Candidate, heuristic, open, and withdrawn claims
are explicit in proof/claims.toml.

## Verification

    python -m pytest
    python tools/check_claims.py
