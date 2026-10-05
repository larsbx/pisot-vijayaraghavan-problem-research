#!/usr/bin/env python3
"""Exact census for A,A,B,B gcd tails in nearest-integer E-sequences.

NON-AUTHORITATIVE. A missing witness is not a theorem.
"""

from __future__ import annotations

import argparse
import json

from kernel.pv_exact import (
    defects,
    gcd_state,
    generate_e,
    period4_aabb_tail,
    transition_data,
)


def scan(seed_max: int, length: int, repeats: int) -> dict:
    witnesses = []
    ties = []
    total = 0
    for a0 in range(2, seed_max + 1):
        for a1 in range(a0 + 1, 2 * seed_max + 1):
            total += 1
            try:
                values = generate_e(a0, a1, length)
            except ValueError as exc:
                ties.append({"seed": [a0, a1], "reason": str(exc)})
                continue
            states = gcd_state(values)
            pattern = period4_aabb_tail(states, repeats=repeats)
            if pattern is None:
                continue
            cs = defects(values)
            n = len(values) - 3
            td = transition_data(*values[n : n + 3])
            witnesses.append(
                {
                    "seed": [a0, a1],
                    "pattern": list(pattern),
                    "last_values": values[-8:],
                    "last_gcd_states": states[-12:],
                    "last_defects": cs[-8:],
                    "last_relative_defect": {
                        "numerator": abs(cs[-1]),
                        "denominator": values[-3],
                    },
                    "last_transition": {
                        "g_n": td.g_n,
                        "g_next": td.g_next,
                        "b_n": td.b_n,
                        "d_n": td.d_n,
                        "primitive_det": td.primitive_det,
                    },
                }
            )
    return {
        "parameters": {
            "seed_max": seed_max,
            "length": length,
            "period_repeats": repeats,
        },
        "seed_count": total,
        "tie_count": len(ties),
        "witness_count": len(witnesses),
        "witnesses": witnesses,
        "ties": ties[:50],
        "status": "COMPUTED finite census; absence of witnesses is inconclusive",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed-max", type=int, default=40)
    parser.add_argument("--length", type=int, default=60)
    parser.add_argument("--repeats", type=int, default=3)
    args = parser.parse_args()
    print(json.dumps(scan(args.seed_max, args.length, args.repeats), indent=2))


if __name__ == "__main__":
    main()
