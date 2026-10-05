# Frontier P4 — two-state period-four gcd dynamics

## Why this is first

The October 5 audit corrected a structural mistake:
[
g_n
e g_{n+2}
]
does not force three gcd states. With exactly two states (A
e B), it forces,
up to shift/renaming,
[
A,A,B,B,A,A,B,B,ldots
]

This is the minimal genuinely varying bounded-gcd case.

## Standing exact data

Let
[
g_n=gcd(a_n,a_{n+1}),quad
a_n=g_nu_n,quad a_{n+1}=g_nv_n,quad c_n=g_nh_n.
]
Set
[
b_n=gcd(v_n,h_n),qquad
g_{n+1}=b_nd_n,quad d_nmid g_n,
]
and
[
D_n=rac{c_n}{g_ng_{n+1}}inmathbb Z.
]

On P4 the edge types are
[
A	o A,quad A	o B,quad B	o B,quad B	o A.
]

## Proof obligations

**P4.1 Four-step normal form.** Express the primitive pair after four steps and
the four (D_n)'s in terms of the initial primitive pair and overlap factors.

**P4.2 Valuation cycle.** Track (v_p(A),v_p(B),v_p(b_j),v_p(d_j),v_p(D_j))
through a period.

**P4.3 Defect support split.** Separate primes (plemax(A,B)) from fresh
primes. No fresh-mass conclusion without a lower bound on the large-prime part.

**P4.4 Exact census.** Search bounded seeds and emit exact witnesses with tail
values, gcd states, defects, and transition data.

## Negative controls

- constant gcd tails;
- period-two (A,B,A,B,ldots), which has two-step returns;
- gcd-one Fibonacci-type tails;
- half-integer nearest-integer ties.

## Significant milestone

Either prove P4 impossible in the PV residual regime, or produce a reproducible
persistent witness family showing what invariant is still missing.
