# Repository architecture

This repository adopts the authority separation of `langlands-lab` and
`finite-math-kernels`, initially without their full governance estate.

The ordering rule is:

~~~text
claim authority -> mathematical concern -> implementation
~~~

## Exact kernel — `kernel/`

Canonical executable identities using exact arithmetic only. It may generate
nearest-integer (E)-sequences, compute defects/Hankel minors/gcd
normalizations, and expose deterministic predicates.

It may not turn a census into a theorem.

## Evidence — `tests/`

Regression evidence for exact identities. Tests support the implementation and
catch algebraic drift; they do not prove universal mathematics by enumeration.

## Experiments — `experiments/`

Non-authoritative frontier searches. Caps and skipped half-integer ties are
reported explicitly.

## Claim state — `docs/`

`docs/dossier.md` is the status ledger; `docs/roadmap.md` is the active
research plan; audit notes preserve corrections that change claim meaning.

## Initial frontier

The first executable target is the two-state period-four gcd pattern
(A,A,B,B,ldots). The repository deliberately does not start with the later
three-state cycle calculations because the October 5 audit found that period
four is the true minimal no-two-step-return model.
