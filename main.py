"""Invent-a-word entry: writes one word plus its definition to OUTPUT_DIR/entry.txt (stdlib only, deterministic)."""
import os

ENTRY = "Doorjog (n.): the awkward half-run you do because someone is holding a door for you from much too far away."
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main():
    # Gate: UTF-8 text inside the bounty's character limit, not only white space.
    assert ENTRY.strip() and 1 <= len(ENTRY) <= 140
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
