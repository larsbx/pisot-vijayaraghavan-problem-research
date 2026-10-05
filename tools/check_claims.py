"""Fail closed on claim-status drift."""

from pathlib import Path
import tomllib

ROOT = Path(__file__).resolve().parents[1]
CLAIMS = ROOT / "proof" / "claims.toml"
DOSSIER = ROOT / "docs" / "dossier.md"
ALLOWED = {"PROVED", "COMPUTED", "IMPORTED", "CANDIDATE", "HEURISTIC", "OPEN", "WITHDRAWN"}


def main() -> None:
    data = tomllib.loads(CLAIMS.read_text())
    claims = data.get("claim", [])
    if not claims:
        raise SystemExit("no claims declared")
    ids = set()
    dossier = DOSSIER.read_text()
    errors = []
    for claim in claims:
        cid = claim.get("id", "")
        status = claim.get("status", "")
        if not cid or cid in ids:
            errors.append(f"invalid or duplicate claim id: {cid!r}")
        ids.add(cid)
        if status not in ALLOWED:
            errors.append(f"{cid}: invalid status {status!r}")
        if cid not in dossier:
            errors.append(f"{cid}: missing from docs/dossier.md")
        if not claim.get("statement"):
            errors.append(f"{cid}: missing statement")
        if not claim.get("does_not_establish"):
            errors.append(f"{cid}: missing does_not_establish boundary")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"claim audit: {len(claims)} claims, statuses and dossier coverage consistent")


if __name__ == "__main__":
    main()
