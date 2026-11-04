from collections import Counter
from pathlib import Path
import re


INPUT_FILE = Path(__file__).with_name("sample.txt")
OUTPUT_FILE = Path(__file__).with_name("report.txt")


def normalize_text(text: str) -> str:
    """Return non-empty, trimmed lines in lowercase."""
    # TODO: Trim each line, discard empty lines, lowercase, and join with newlines.
    raise NotImplementedError


def count_words(text: str) -> Counter[str]:
    """Count words without distinguishing uppercase and lowercase."""
    # TODO: Extract words and return their frequency counts.
    raise NotImplementedError


def main() -> None:
    text = INPUT_FILE.read_text(encoding="utf-8")
    normalized_text = normalize_text(text)
    word_counts = count_words(normalized_text)
    total_words = sum(word_counts.values())
    top_words = word_counts.most_common(5)

    report_lines = [f"Total words: {total_words}", "Top words:"]
    report_lines.extend(f"{word}: {count}" for word, count in top_words)
    OUTPUT_FILE.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    print(f"Report written to {OUTPUT_FILE.name}")


if __name__ == "__main__":
    main()
