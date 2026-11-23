#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

The first word that comes to mind, and nothing else: petrichor, the
scent of rain on dry earth. Pure standard library, deterministic, no
network and no randomness: it writes the word to entry.txt inside the
grader's output directory and exits.
"""

import os
import sys

WORD = "petrichor"
MAX_CHARS = 24


def check_word(word):
    """Refuse anything the gate would refuse, before writing it out."""
    if not isinstance(word, str) or not word:
        raise ValueError("entry word must be a non-empty string")
    if word != word.strip() or len(word.split()) != 1:
        raise ValueError("entry must be exactly one word, no whitespace")
    if len(word) > MAX_CHARS:
        raise ValueError("entry word exceeds the 24-character gate")
    if not word.isprintable():
        raise ValueError("entry word must be printable text")
    return word


def output_path():
    """Where the entry goes: the grader's output dir, else /output."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def main():
    word = check_word(WORD)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)
    return 0


if __name__ == "__main__":
    sys.exit(main())
