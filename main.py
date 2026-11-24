#!/usr/bin/env python3
"""One Word for the Boss — writes the entry word to /output/entry.txt.

The word: Hovercraft. The boss who hovers over your shoulder all day,
never quite landing, never quite leaving — a micromanager with lift.
"""

import os

WORD = "Hovercraft"


def check_word(word: str) -> None:
    """Make sure the word meets the competition gate before writing it:
    a single word, 1 to 30 characters, not only whitespace."""
    assert 1 <= len(word) <= 30, "word must be 1-30 characters"
    assert word.strip(), "word must not be only whitespace"
    assert " " not in word, "word must be a single word"


def main() -> None:
    check_word(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
