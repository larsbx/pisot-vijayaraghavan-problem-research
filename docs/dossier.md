# PV research dossier

Authoritative statuses are in proof/claims.toml.

## Banked

### PV-REDUCTION-FWD — PROVED
A PV witness gives the eventual quadratic-rounding defect reduction.
Does not establish the converse or algebraicity.

### PV-DODGSON-H3 — PROVED
a_{n+2} H_n^(3) = c_n c_{n+2} - c_{n+1}^2.

### PV-SQRT-BARRIER — PROVED
If |c_n|=o(a_n^(1/2)) in the expanding regime, H_n^(3)=0 eventually.
Does not establish recurrence until PV-HANKEL-RANK-BRIDGE is closed.

### PV-GCD-NORMALIZATION — PROVED
g_n g_{n+1}|c_n, and with a_n=g_n u_n, a_{n+1}=g_n v_n,
c_n=g_n h_n, b_n=gcd(v_n,h_n), one has b_n|g_{n+1} and
d_n=g_{n+1}/b_n divides g_n.

### PV-FRESHNESS — PROVED
Under eventual g_n≤G, p>G and p|c_n implies
p does not divide a_n a_{n+1} a_{n+2}. This is local freshness only.

### PV-TRANSPORT — PROVED
a_n^2 c_{n+1}+c_n^2 ≡ 0 mod a_{n+1}. Retained as a shadow identity,
not as independent mesoscopic leverage.

### PV-TWO-STEP-RETURN — PROVED
Under exact g_n=g_{n+2}=g, scaling by g gives the primitive quadratic shape
U_n W_n-V_n^2=E_n and local freshness. This is a reduction to the still-open
coprime-tail QR problem.

## Candidates and open interfaces

### PV-REDUCTION-CONVERSE — CANDIDATE
Needs a rewritten audited tail-summation proof.

### PV-EXP-WINDOW — CANDIDATE
The limsup proof is withdrawn. A rank-one perturbation proof is the replacement
route and needs a full writeup plus review.

### PV-HANKEL-RANK-BRIDGE — OPEN
Match the exact eventual contiguous-minor hypothesis to finite Hankel rank /
constant-coefficient recurrence before claiming algebraicity.

### PV-POLY-EQUIV — CANDIDATE
Needs the ratio-drift bootstrap proof.

## Withdrawn and heuristic

### PV-SIGMA-CONCAVITY — WITHDRAWN
Separate limsups cannot be added in the required direction.

### PV-THREE-STATE-MINIMAL — WITHDRAWN
A,A,B,B,... is a two-state no-two-step-return counterexample.

### PV-BETA-CASCADE — HEURISTIC
Smooth-model prediction only.

### PV-PLUCKER-PATH — CANDIDATE
Conditional special-case salvage only; not the critical path.

## Frontier

### PV-BOUND-GCD-FRONTIER — OPEN
Analyze the actual minimal bounded-state residual: the two-state period-4
A,A,B,B pattern and its shifts, with the full b_n,d_n transition decomposition.
