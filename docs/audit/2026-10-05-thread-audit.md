# October 5, 2026 thread audit

**Status:** audit record. It proves no theorem by itself.
Current claim states are in proof/claims.toml and explained in
docs/dossier.md.

## Surviving core

- PV-witness to eventual nearest-integer E-sequence reduction.
- $H_n^{(2)}=c_n$ and the third-Hankel Desnanot–Jacobi identity.
- The sub-square-root collapse, with adjacent growth comparability.
- Exact gcd normalization, $g_ng_{n+1}\mid c_n$, and local freshness.
- Exact transport congruence as background algebra.
- Exact two-step-return scaling under exact gcd hypotheses.
- Conditional Plücker/common-core identities under repeated-path hypotheses.

## Corrections that reset the frontier

### Invalid limsup concavity

Splitting limsups across the Dodgson product is invalid.
PV-SIGMA-CONCAVITY is WITHDRAWN. The exponential-window theorem remains
CANDIDATE pending the rank-one proof and recurrence-endpoint audit.

### Moving minors are not moving recurrences

One equality $H_n^{(K(n))}=0$ does not bound the recurrence order of a tail.
Even the relevant fixed contiguous-minor hypothesis must be matched to an
explicit finite-rank bridge before claiming recurrence or algebraicity.

### Reconstruction and polynomial decay remain candidates

The converse reconstruction needs the rewritten tail-summation proof.
Polynomial defect equivalence needs the ratio-drift bootstrap.
Neither is promoted by this bootstrap consolidation.

### Freshness is local

Large primes of $c_n$ are locally fresh when adjacent gcds are bounded and
$p>G$. The defect may be dominated by the finite small-prime set.
No large fresh-prime-mass conclusion follows without an additional bound.

### Transport is not independent leverage

The transport congruence reaches no further than the square-root barrier
without additional input.

### Two states already realize no-two-step-return

The word $(A,A,B,B,A,A,B,B,\ldots)$ satisfies $g_n\neq g_{n+2}$.
PV-THREE-STATE-MINIMAL is WITHDRAWN. Period four is the first bounded-state
frontier; the seed $(9,38)$ supplies transient finite evidence only.

### Two-step return and three-cycle calculations are conditional

Two-step return scales a local window into primitive pairs; it does not solve
the open coprime-tail problem. Three-state cycles remain special periodic
models, not a reduction of the general bounded-state problem.

### Gap-2 inverse-unit compatibility is tautological

It is not a new cocycle obstruction after the units are written explicitly.

## Bootstrap consolidation

PR #1 supplies the exact E-sequence kernel, canonical rotation labels,
regressions, period-four diagnostic, and replayable census.
PR #5 supplies estate-v2 policy, an authoritative ledger, additional identity
interfaces/tests, and explicit candidate/withdrawn boundaries.

The consolidated bootstrap uses one ledger and one dossier. The status
checker compares actual claim headings against the ledger, rejecting missing,
duplicate, unknown, malformed, and mismatched claim entries.
Former bootstrap IDs are mapped in the dossier; no proof obligation is
closed merely by this reconciliation.

## Reset

1. Bank the exact core and close the reconstruction/recurrence interfaces.
2. Finish the corrected exponential-window and polynomial-decay proofs.
3. Attack P4 and analyze its transient spike transitions.
4. Split small-prime valuation mass from fresh-prime mass.
5. Return to larger state models only after P4.
