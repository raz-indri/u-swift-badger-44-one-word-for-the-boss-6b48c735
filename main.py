#!/usr/bin/env python3
"""One Word for the Boss — writes the entry word to /output/entry.txt.

The word: Hovercraft. The boss who hovers over your shoulder all day,
never quite landing, never quite leaving — a micromanager with lift.

Run with no arguments to write the entry. Run with --self-test to
validate the word, write it, read it back, and report the result.
"""

import os
import sys

WORD = "Hovercraft"
ENTRY_PATH = "/output/entry.txt"


def check_word(word: str) -> None:
    """Make sure the word meets the competition gate before writing it:
    a single word, 1 to 30 characters, not only whitespace."""
    assert 1 <= len(word) <= 30, "word must be 1-30 characters"
    assert word.strip(), "word must not be only whitespace"
    assert " " not in word, "word must be a single word"


def write_entry() -> None:
    """Validate the word and store it at the entry path."""
    check_word(WORD)
    os.makedirs(os.path.dirname(ENTRY_PATH), exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


def self_test() -> int:
    """End-to-end check: write the entry, read it back, and confirm
    the stored text is exactly the word we meant to submit."""
    write_entry()
    with open(ENTRY_PATH, encoding="utf-8") as f:
        stored = f.read()
    if stored != WORD:
        print(
            f"self-test FAILED: entry file holds {stored!r}, "
            f"expected {WORD!r}",
            file=sys.stderr,
        )
        return 1
    print(f"word: {WORD}")
    print(f"characters: {len(WORD)}")
    print("self-test OK")
    return 0


def main(argv: list[str]) -> int:
    if argv and argv[0] == "--self-test":
        return self_test()
    write_entry()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
