# Research roadmap

PV is open. Only claims marked PROVED in proof/claims.toml are established here.

## Priority 1 — close proof interfaces
1. Prove PV-HANKEL-RANK-BRIDGE with the exact contiguous-minor hypotheses.
2. Write and independently audit the rank-one perturbation proof for
   PV-EXP-WINDOW; never reuse the withdrawn limsup argument.
3. Write and audit the ratio-drift bootstrap for PV-POLY-EQUIV.

## Priority 2 — minimal bounded-state frontier
Analyze the two-state no-two-step-return word

    A,A,B,B,A,A,B,B,...

and its shifts using

    g_{n+1}=b_n d_n,
    b_n=gcd(v_n,h_n),
    d_n|g_n.

Targets: complete the four-phase transition table, derive exact primitive
defect identities, identify which freshness/QR constraints survive a period,
and either contradict the branch or reduce it honestly to coprime-tail.

## Priority 3 — coprime-tail and subexponential frontier
Transport is background algebra, not an independent solution method.

## Deferred
Three-state Plücker/cycle identities are conditional special-case salvage and
stay off the critical path until the two-state frontier is understood.
