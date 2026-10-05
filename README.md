# Pisot–Vijayaraghavan problem research

A research repository for the classical Pisot–Vijayaraghavan (PV) problem:

> If (alpha>1) and there is (lambda
eq 0) with
> (|lambdaalpha^n|	o 0), must (alpha) be algebraic (hence Pisot)?

The repository follows the authority split used in
`larsbx/langlands-lab` and `larsbx/finite-math-kernels`:

- **exact kernel** under `kernel/`: integer/rational identities only;
- **tests** under `tests/`: evidence for executable identities;
- **experiments** under `experiments/`: exploratory and non-authoritative;
- **docs/dossier.md**: claim ledger with explicit status;
- **docs/roadmap.md**: current frontier and proof obligations.

No computation promotes itself to a theorem. A capped search that finds no
counterexample is evidence about that finite search, not a proof.

## Audited starting point

For an integer sequence ((a_n)), write
[
c_n=a_n a_{n+2}-a_{n+1}^2,qquad
H_n^{(k)}=det(a_{n+i+j})_{0le i,j<k}.
]

The current audited core is:

1. a PV witness yields an expanding eventual nearest-integer (E)-sequence with
   (c_n=o(a_n)), and conversely that discrete regime reconstructs the PV
   approximation;
2. Desnanot–Jacobi gives
   [
   a_{n+2}H_n^{(3)}=c_n c_{n+2}-c_{n+1}^2;
   ]
3. (c_n=o(a_n^{1/2})) forces (H_n^{(3)}=0) eventually;
4. in the bounded-gcd branch, with (g_n=gcd(a_n,a_{n+1})),
   (g_ng_{n+1}mid c_n), and primes (p>G) dividing (c_n) are locally fresh
   when (g_nle G);
5. the transport congruence
   [
   a_n^2c_{n+1}+c_n^2equiv0pmod{a_{n+1}}
   ]
   is exact but does not by itself penetrate the mesoscopic defect window;
6. the first missed finite-state frontier is the two-state no-two-step-return
   pattern
   [
   A,A,B,B,A,A,B,B,ldots,
   ]
   not the later three-state cycle model.

A stronger exponential-window Hankel-collapse argument via a rank-one
perturbation is **PROVISIONAL** until its fixed-Hankel-rank endpoint is fully
audited. See `docs/dossier.md`.

## Layout

~~~text
AGENTS.md
ARCHITECTURE.md
kernel/
  pv_exact.py
tests/
  test_exact_identities.py
experiments/
  period4_state.py
docs/
  dossier.md
  roadmap.md
  frontier-period4.md
  audit/2026-10-05-thread-audit.md
.github/workflows/ci.yml
~~~

## Run

~~~bash
python -m pip install -e '.[test]'
pytest
python experiments/period4_state.py --seed-max 40 --length 120 --min-periods 3
~~~

Canonical arithmetic is exact: Python integers and `fractions.Fraction`.
Floating point is forbidden in the kernel and proof-relevant tests.

## Current frontier

The immediate target is the bounded-gcd two-state period-four pattern. The
experiment lane first determines whether such gcd tails occur naturally among
nearest-integer (E)-sequences and emits exact replayable witnesses. The proof
lane attacks the same pattern symbolically; computation never substitutes for
that proof.
