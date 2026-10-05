# PV research dossier

Authoritative statuses are in proof/claims.toml. Every claim below has exactly
one status heading, checked against that ledger. Computation supplies finite
evidence; the elementary derivations below justify the banked identities.

## Banked

### PV-REDUCTION-FWD — PROVED

A PV witness gives an eventual nearest-integer E-sequence with $c_n=o(a_n)$.

**Derivation.** Replace $\lambda$ by $|\lambda|>0$ and write
$a_n=\lambda\alpha^n+\varepsilon_n$, where $\varepsilon_n\to0$ and $a_n$
is the nearest integer. Expanding the defect gives

$$
c_n=\lambda\alpha^n
(\varepsilon_{n+2}+\alpha^2\varepsilon_n-2\alpha\varepsilon_{n+1})
+\varepsilon_n\varepsilon_{n+2}-\varepsilon_{n+1}^2.
$$

Thus $c_n=o(a_n)$ and $a_{n+2}-a_{n+1}^2/a_n=c_n/a_n\to0$.
Eventually the difference has absolute value below $1/2$, so the quadratic
rounding is unique. Also $a_{n+1}/a_n\to\alpha>1$.

**Boundary.** This does not establish the converse or algebraicity.

### PV-DODGSON-H3 — PROVED

$H_n^{(2)}=c_n$ and
$a_{n+2}H_n^{(3)}=c_nc_{n+2}-c_{n+1}^2$.

**Derivation.** The first equality is the $2\times2$ determinant.
For $(a,b,c,d,e)=(a_n,a_{n+1},a_{n+2},a_{n+3},a_{n+4})$, expansion gives

$$
H_n^{(3)}=ace-ad^2-b^2e+2bcd-c^3.
$$

Multiplying by $c$ equals $(ac-b^2)(ce-d^2)-(bd-c^2)^2$.
The kernel also checks the general Desnanot–Jacobi identity.

**Boundary.** No asymptotic vanishing follows from this identity alone.

### PV-SQRT-BARRIER — PROVED

For a positive expanding sequence with adjacent growth comparability,
$|c_n|=o(a_n^{1/2})$ implies $H_n^{(3)}=0$ eventually.

**Derivation.** Assume $a_{n+j}\asymp a_n$ for each fixed nearby $j$
(as holds if $a_{n+1}/a_n\to\alpha>1$).
Then $c_nc_{n+2}-c_{n+1}^2=o(a_n)$.
Divide the Dodgson identity by $a_{n+2}\asymp a_n$ to get
$H_n^{(3)}=o(1)$. It is an integer, hence eventually zero.

**Boundary.** The resulting fixed layer now uses PV-HANKEL-RANK-BRIDGE to
give a tail recurrence of order at most two. This does not close the general
subexponential defect frontier.

### PV-EXP-WINDOW — PROVED

For integer $a_n$ positive on a tail with $a_{n+1}/a_n\to\alpha>1$ and
$|c_n|=O(\alpha^{\gamma n})$, $\gamma<1$, the ratio summation gives
$a_n=\lambda\alpha^n+O(\alpha^{(\gamma-1)n})$.
The rank-one determinant bound vanishes at every late starting index when
$(k-1)(1-\gamma)>1$. Its least guaranteed size is
$\lfloor1/(1-\gamma)\rfloor+2$.

**Proof.** [Manuscript Sections 1-3](exponential-window-hankel.md).

**Boundary.** Equality at a reciprocal integer gives only bounded
determinants under big-O; the little-o hypothesis does give vanishing there.
Integer Lucas and cubic trace sequences certify the big-O distinction.
The subexponential window and $\gamma=1$ remain outside this theorem.

### PV-HANKEL-RANK-BRIDGE — PROVED

Over any field, a fixed $D_K(n)=0$ for every $n\ge N$ gives a constant tail
recurrence of order $r<K$ and tail Hankel rank $r$, with tail start at most
$N+K-1$. Desnanot-Jacobi descent supplies the needed nonvanishing lower
layer, including singular cases and the eventually zero tail. Overlapping
windows make the recurrence coefficients constant.

**Proof.** [Manuscript Section 4](exponential-window-hankel.md), using exactly
the fixed-size, every-late-shift hypothesis obtained above.

**Boundary.** One moving minor, sparse shifts, or finite-prefix vanishing
does not suffice. No genericity or lower-minor nonvanishing is assumed.

### PV-H3 — PROVED

The audited composition of PV-EXP-WINDOW and PV-HANKEL-RANK-BRIDGE retains
the earlier PV-H3 identifier in the same authoritative ledger. Under their
expanding integer hypotheses, the minimal recurrence is monic over
$\mathbb Z$, $\alpha$ is Pisot of degree at most
$\lfloor1/(1-\gamma)\rfloor+1$, and $\lambda\in\mathbb Q(\alpha)$.

**Proof.** [Manuscript Sections 4-5](exponential-window-hankel.md): rational
recurrence, integer shift lattice, and poles of the tail generating series.

**Boundary.** This does not solve the general PV problem or promote
PV-POLY-EQUIV, the general converse reduction, or PV-SALEM-EXCLUSION in
its broader merely-vanishing-error setting.

### PV-GCD-NORMALIZATION — PROVED

Let $g=\gcd(a,b)$, $g'=\gcd(b,c)$ and
$a=gu$, $b=gv$, $ac-b^2=gh$.
Then $gg'\mid ac-b^2$, and with $b_*=\gcd(v,h)$ one has
$g'=b_*d$, $d\mid g$.

**Derivation.** The product $ac$ is divisible by $gg'$.
For each prime, $b^2$ has valuation at least
$2\max(v_p(g),v_p(g'))\ge v_p(g)+v_p(g')$, so it too is divisible
by $gg'$. Also $\gcd(u,v)=1$ and $h=uc-gv^2$, hence
$b_*=\gcd(v,c)$. Write $v=b_*v'$ and $c=b_*c'$ with
$\gcd(v',c')=1$. Then
$g'=\gcd(gb_*v',b_*c')=b_*\gcd(g,c')$, giving $d=\gcd(g,c')$.

In the sequence notation, $b_*=b_n$, $d=d_n$, and
$D_n=c_n/(g_ng_{n+1})\in\mathbb Z$.

**Boundary.** This proves neither boundedness of gcds nor termination.

### PV-FRESHNESS — PROVED

If $g_n,g_{n+1}\le G$, $p>G$, and $p\mid c_n$, then
$p\nmid a_na_{n+1}a_{n+2}$.

**Derivation.** If $p$ divides either endpoint term, the defect identity forces
$p$ to divide the middle term, contradicting the adjacent gcd bound.
If $p$ divides the middle term, it divides the product of the endpoints,
giving the same contradiction.

**Boundary.** This is local freshness only. It supplies no nonlocal return
freshness or lower bound on fresh-prime mass.

### PV-TRANSPORT — PROVED

$a_n^2c_{n+1}+c_n^2\equiv0\pmod{a_{n+1}}$.

**Derivation.** For $(a,b,c,d)$, direct expansion yields

$$
a^2(bd-c^2)+(ac-b^2)^2=b(a^2d-2abc+b^3).
$$

**Boundary.** This is background algebra, not independent leverage past the
square-root threshold.

### PV-TWO-STEP-RETURN — PROVED

Under exact $g_n=g_{n+2}=g$, all four displayed terms
$a_n,\ldots,a_{n+3}$ are divisible by $g$.
Scaling gives integer pairs $(U,V)$ and $(W,X)$ with
$\gcd(U,V)=\gcd(W,X)=1$ and

$$
UW-V^2=c_n/g^2.
$$

**Derivation.** Divisibility and the two primitive endpoint pairs follow
directly from the exact gcd equalities. The displayed identity follows by
dividing the defect by $g^2$. Any already valid local freshness condition
transplants to the scaled terms; a prime dividing a scaled term also divides
the original term.

**Boundary.** The intervening pair $(V,W)$ need not be primitive.
This local window does not establish a coprime tail or solve its open
quadratic-residue dynamics.

## Candidates and open interfaces

### PV-REDUCTION-CONVERSE — CANDIDATE

An expanding eventual quadratic-rounding sequence with normalized defect
tending to zero is proposed to reconstruct a PV witness.
The tail-summation proof must be rewritten and independently reviewed.
No promotion is made here.

### PV-POLY-EQUIV — CANDIDATE

The proposed equivalence between $c_n=O(\alpha^n/n^A)$ and
$\|\lambda\alpha^n\|=O(n^{-A})$ needs the ratio-drift bootstrap proof.
It is not promoted by the identity regressions.

### PV-SALEM-EXCLUSION — CANDIDATE

Once recurrence is known, the proposed exclusion of the Salem-recurrent
branch needs a pinned structural citation or complete proof.
This does not establish recurrence or algebraicity.

### PV-COPRIME-TAIL — OPEN

Resolve the coprime-tail mesoscopic quadratic-residue dynamics and the
additional input needed to glue local return instances.
Exact scaling and finite experiments leave this branch open.

## Withdrawn and heuristic

### PV-SIGMA-CONCAVITY — WITHDRAWN

The claim of unconditional concavity of separate limsup Hankel profiles is
withdrawn: separate limsups cannot be added in the required direction.

### PV-THREE-STATE-MINIMAL — WITHDRAWN

The claim that no two-step return requires at least three states is false:
$(A,A,B,B,\ldots)$ is a two-state counterexample.

### PV-BETA-CASCADE — HEURISTIC

Under a smooth regularly varying ansatz, the prediction
$\beta_k=(k-1)(k+A-2)$ is a model only.
It supplies no theorem, fixed-rank collapse, or recurrence.

### PV-PLUCKER-PATH — CANDIDATE

Conditional repeated-path Plücker/common-core identities are special-case
salvage only. The required path hypotheses and derivations must be explicit;
these paths are not shown to be exhaustive or on the critical frontier.

## Frontier and finite evidence

### PV-BOUND-GCD-FRONTIER — OPEN

Analyze the two-state no-two-step-return period-four word and its shifts
with the full $(b_n,d_n,D_n)$ transitions.
The symbolic obligations are in docs/frontier-period4.md.
Neither coprime-tail nor the full PV problem is solved.

### PV-PERIOD4-CENSUS — COMPUTED

At length 120, seed $(9,38)$ has three separate six-period AABB-type gcd
runs interrupted by spikes. The exact intervals and replay command are in
docs/experiments/2026-10-05-period4-census.md.

**Boundary.** This does not establish an eventual tail, a persistent family,
or an impossibility theorem in the PV residual regime.

## Earlier bootstrap ID mapping

These are aliases for continuity, not an additional status ledger.

| Earlier ID | Authoritative claim ID |
| --- | --- |
| PV-D1 | PV-REDUCTION-FWD; PV-REDUCTION-CONVERSE |
| PV-H1 | PV-DODGSON-H3 |
| PV-H2 | PV-SQRT-BARRIER |
| PV-H3 | PV-H3 (audited composition); PV-EXP-WINDOW; PV-HANKEL-RANK-BRIDGE |
| PV-G1; PV-G2 | PV-GCD-NORMALIZATION |
| PV-G3 | PV-FRESHNESS |
| PV-T1 | PV-TRANSPORT |
| PV-P4 | PV-BOUND-GCD-FRONTIER |
| PV-COP | PV-COPRIME-TAIL |
| PV-S | PV-SALEM-EXCLUSION |
