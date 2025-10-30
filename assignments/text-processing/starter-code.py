#!/usr/bin/env python3
"""
Starter code for Python Text Processing assignment.

Features:
- Read a text file
- Normalize and count words
- Print a short summary and write a report file
- (Optional) simple find-and-replace and save transformed file

This is intentionally simple — extend for extra credit.
"""
import sys
import string
from collections import Counter
from pathlib import Path


def normalize_token(token: str) -> str:
    """Lowercase and strip punctuation from a token."""
    return token.strip(string.punctuation).lower()


def analyze_text(text: str):
    tokens = [normalize_token(t) for t in text.split()]
    tokens = [t for t in tokens if t]
    total = len(tokens)
    counts = Counter(tokens)
    unique = len(counts)
    top5 = counts.most_common(5)
    return {
        "total": total,
        "unique": unique,
        "top5": top5,
        "counts": counts,
    }


def write_report(input_path: Path, analysis: dict):
    out_path = input_path.with_name(f"{input_path.stem}-report.txt")
    with out_path.open("w", encoding="utf-8") as f:
        f.write(f"Report for: {input_path.name}\n")
        f.write(f"Total words: {analysis['total']}\n")
        f.write(f"Unique words: {analysis['unique']}\n")
        f.write("Top 5 words:\n")
        for w, c in analysis["top5"]:
            f.write(f"  {w} — {c}\n")
    return out_path


def find_and_replace(text: str, target: str, replacement: str) -> str:
    # Simple case-insensitive replace; this does not preserve original case in replaced words
    return text.replace(target, replacement).replace(target.lower(), replacement).replace(target.upper(), replacement)


def main(argv):
    if len(argv) < 2:
        print("Usage: python3 starter-code.py <input-file> [--replace old new]")
        return 1

    input_file = Path(argv[1])
    if not input_file.exists():
        print(f"Error: {input_file} does not exist")
        return 2

    text = input_file.read_text(encoding="utf-8")
    if not text.strip():
        print("Input file is empty")
        return 0

    analysis = analyze_text(text)
    report_path = write_report(input_file, analysis)

    print(f"Input: {input_file.name}")
    print(f"Total words: {analysis['total']}")
    print(f"Unique words: {analysis['unique']}")
    print("Top 5 words:")
    for w, c in analysis['top5']:
        print(f"  {w} — {c}")
    print(f"Report written to: {report_path.name}")

    # Simple CLI for optional replacement
    if len(argv) >= 5 and argv[2] == "--replace":
        old = argv[3]
        new = argv[4]
        replaced = find_and_replace(text, old, new)
        out_path = input_file.with_name(f"{input_file.stem}-replaced{input_file.suffix}")
        out_path.write_text(replaced, encoding="utf-8")
        print(f"Replaced '{old}' with '{new}' and saved to: {out_path.name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
