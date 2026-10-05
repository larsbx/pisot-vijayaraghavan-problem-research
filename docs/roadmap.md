# Research roadmap

## Phase 0 — bank the audited core

1. Write PV-D1 cleanly.
2. Promote PV-H2 to a standalone theorem note.
3. Finish the rank-one proof for PV-H3 and prove/cite the fixed-Hankel-rank
   recurrence endpoint.
4. Pin the exact Salem-recurrent theorem needed for PV-S.

## Phase 1 — two-state period-four frontier

Attack
[
A,A,B,B,A,A,B,B,ldots
]
under bounded gcd and residual subexponential defect decay.

Deliverables:

- four-step symbolic normal form;
- ((b_n,d_n,D_n)) valuation cycle;
- exact seed census with replayable witnesses;
- negative controls for constant and period-two gcd patterns.

See `docs/frontier-period4.md`.

## Phase 2 — small-prime versus fresh-prime mass

Split
[
c_n=c_{n,S}c_{n,S^c},qquad S={p:ple G}.
]

Treat large (S)-parts by (p)-adic valuation dynamics and large (S^c)-parts
by freshness/run/projective methods. Never use a fresh-prime-mass argument
without proving the (S^c)-part is large.

## Phase 3 — return blocks and coprime-tail dynamics

Treat two-step returns as local coprime-normalized QR instances; determine what
extra input is needed to glue those local instances.

## Phase 4 — larger finite-state models

Only after period four is understood should conditional three-state/Plücker
models return to the main line.
