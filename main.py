"""Warning Label for Humans: One Line, Big Laugh.

The entry line, against the judge brief:
- On-subject first: it opens with WARNING and reads exactly like a
  printed safety label stuck on a human being.
- The laugh lands in the last few words: after a list of very human
  faults, the handling instruction is "Handle with snacks" — the
  punchline is the label's own remedy, and it is the only instruction
  the label gives.
- Recognition: caffeine-fuelled, overthinking, narrating your own life
  like a documentary — behaviour almost every human recognises in
  themselves the moment they read it.
- Label wording and rhythm: terse clauses, no filler, one idea,
  and it uses the line without a second joke.
"""

ENTRY = (
    "WARNING: This human runs on caffeine, overthinks everything, "
    "and may spontaneously narrate their life like a documentary. "
    "Handle with snacks."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    import os

    # Guard: the gate allows 1-160 characters, one line, not only
    # whitespace. Enforce it here so a bad edit fails loudly locally.
    if not (1 <= len(ENTRY) <= 160):
        raise SystemExit(f"entry must be 1-160 chars, got {len(ENTRY)}")
    if "\n" in ENTRY or ENTRY != ENTRY.strip():
        raise SystemExit("entry must be a single line with no extra whitespace")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Verify what landed on disk is exactly the entry, nothing else.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        raise SystemExit("output mismatch: entry.txt does not match the entry")


if __name__ == "__main__":
    main()
