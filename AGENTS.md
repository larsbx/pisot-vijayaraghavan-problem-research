# Agent policy — pisot-vijayaraghavan-problem-research

This repository studies the classical PV problem through exact integer
dynamics, Hankel determinants, gcd normalizations, and controlled experiments.

**Canonical arithmetic:** Python integers and `fractions.Fraction`.
**CI:** GitHub Actions runs the exact regression suite.
**Research rule:** computations are evidence, never theorem promotion.

## Read first

- `README.md`
- `ARCHITECTURE.md`
- `docs/dossier.md`
- `docs/roadmap.md`
- `docs/audit/2026-10-05-thread-audit.md`

## Gate

Before describing a change as finished:

~~~bash
pytest
~~~

For experiment changes, also run the relevant experiment with committed
parameters and report the exact command and cap.

## Claim statuses

Use these in `docs/dossier.md`:

- **PROVED** — proof written and surviving the current audit;
- **DERIVED** — exact algebraic identity/reduction;
- **COMPUTED** — exact finite computation only;
- **PROVISIONAL** — proof candidate with a named obligation remaining;
- **HEURISTIC** — model or asymptotic prediction;
- **IMPORTED** — external theorem used without proof here;
- **OPEN** — unresolved target.

## Standing prohibitions

- No floating point in `kernel/` or proof-relevant tests.
- Do not turn a finite census into a theorem.
- Do not infer recurrence from one moving vanishing Hankel minor.
- Do not reuse the invalid limsup-splitting proof of Hankel-profile concavity.
- Do not assume no-two-step-return requires three gcd states: two states admit
  (A,A,B,B,ldots).
- Do not describe the transport congruence as independent leverage past the
  square-root threshold.
- Keep periodic three-state calculations explicitly conditional.
- Do not claim large fresh-prime mass from local freshness alone.

The current proof frontier is `docs/frontier-period4.md`.
