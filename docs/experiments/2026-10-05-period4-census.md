# Initial period-four census — 2026-10-05

**Status:** COMPUTED finite evidence, non-authoritative.

## Parameters

The initial scan considered positive seeds
[
2le a_0le 40,qquad a_0<a_1le 80.
]

A first length-60 suffix diagnostic found one period-four-looking seed:
[
(a_0,a_1)=(9,38),
]
with gcd states ending in three repeats of (1,1,2,2).

The seed was then extended exactly to length 120 and maximal period-four runs
were inspected.  The pattern is **not** an eventual tail at this depth.

## Seed (9,38)

For
[
g_n=gcd(a_n,a_{n+1}),
]
the length-120 run contains the following maximal (A,A,B,B)-type blocks
(state indices are zero-based and the end index is exclusive):

| start | end | state count | full periods | phase |
|---:|---:|---:|---:|---|
| 11 | 35 | 24 | 6 | (1,1,2,2) |
| 36 | 60 | 24 | 6 | (1,2,2,1) |
| 61 | 85 | 24 | 6 | (2,2,1,1) |
| 86 | 99 | 13 | 3 | (2,1,1,2) |
| 100 | 110 | 10 | 2 | (1,2,2,1) |

The three six-period blocks are separated by large gcd spikes; observed boundary
values include (49), (98), and later (103).  By the end of the
length-120 sample the final 24 gcd states include additional spikes such as
(103), (98), and (71), so the simple period-four model is transient.

## Interpretation

This is useful for the P4 frontier in two ways:

1. the (A,A,B,B) combinatorics genuinely occur for long exact blocks in a
   natural nearest-integer (E)-sequence;
2. persistence must be measured by maximal run length and boundary transitions,
   not by a short suffix detector.

This computation does **not** show that an eventual period-four tail exists.
It instead supplies a concrete transient witness whose spike transitions should
be analyzed using the exact (b_n,d_n,D_n) normalization.

## Reproduction

After PR #1 contains the persistence upgrade:

~~~bash
python experiments/period4_state.py --seed-max 40 --length 120 --min-periods 3
~~~

The diagnostic is designed to emit exact run intervals, relative-defect
fractions, and first-period transition data for every detected seed.
