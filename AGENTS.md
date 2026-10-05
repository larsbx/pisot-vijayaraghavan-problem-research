# Agent policy — PV problem research

This repository is a research estate, not a theorem announcement.

Read first: ESTATE.toml, ARCHITECTURE.md, proof/claims.toml,
docs/dossier.md, docs/audit/THREAD_AUDIT_2026-10-05.md.

Before proposing completion run:

    python -m pytest
    python tools/check_claims.py

Status vocabulary: PROVED, COMPUTED, IMPORTED, CANDIDATE, HEURISTIC, OPEN,
WITHDRAWN.

Never describe PV as solved; never promote bounded computation; never reuse a
WITHDRAWN argument by paraphrase; never use floating point in the canonical
kernel; always state what a change does not establish.
