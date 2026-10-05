# Research roadmap

PV is open. Authoritative statuses are in proof/claims.toml; finite
experiments do not close proof obligations.

## Priority 1 — bank the core and close proof interfaces

1. Rewrite and independently audit the tail-summation proof for
   PV-REDUCTION-CONVERSE (formerly the converse portion of PV-D1).
2. Promote the written PV-SQRT-BARRIER argument to a standalone theorem note.
3. Prove/cite PV-HANKEL-RANK-BRIDGE with the exact fixed contiguous-minor
   hypotheses required by the application.
4. Write and independently audit the rank-one proof for PV-EXP-WINDOW
   (formerly PV-H3). Never reuse the withdrawn limsup argument.
5. Write and audit the ratio-drift bootstrap for PV-POLY-EQUIV.
6. Pin the exact structural citation/proof for PV-SALEM-EXCLUSION
   (formerly PV-S), conditional on recurrence already being established.

Issue #2 tracks the exponential-window proof and recurrence endpoint.

## Priority 2 — two-state period-four frontier

Attack $(A,A,B,B,A,A,B,B,\ldots)$ and its shifts under bounded gcd and
residual subexponential defect decay, using the full transition data

$$
g_{n+1}=b_nd_n,\qquad b_n=\gcd(v_n,h_n),\qquad d_n\mid g_n,\qquad
D_n=\frac{c_n}{g_ng_{n+1}}\in\mathbb Z.
$$

Deliverables:

- four-step primitive-pair normal form and four-phase transition table;
- $(b_n,d_n,D_n)$ valuation cycle;
- exact persistence-depth census with replayable witnesses and spike
  transitions;
- negative controls for constant, period-two, gcd-one, and tied rounding.

The existing seed $(9,38)$ is a transient witness only. Issue #3 tracks
persistence depth; issue #4 tracks the symbolic normal form.
See docs/frontier-period4.md and the committed census note.

## Priority 3 — small-prime mass, return blocks, and coprime tails

For nonzero defects, separate the prime factors in
$S=\{p:p\le G\}$ from the complementary fresh-prime part.
Treat large $S$-parts by valuation dynamics and large complementary parts by
freshness/run/projective methods. Prove the relevant mass lower bound before
using a fresh-prime-mass argument.

Treat two-step returns as local coprime-normalized quadratic-residue
instances; identify the additional input needed to glue them.
PV-COPRIME-TAIL remains OPEN. Transport is background algebra.

## Deferred

Three-state Plücker/cycle identities are conditional special-case salvage.
They stay off the critical path until period four is understood.
