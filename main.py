#!/usr/bin/env python3
"""Six Words, One Story - make.fun entry.

Writes a complete six-word story to the output file.
"""

import os

STORY = "Mother called. I finally answered sober."


def validated_content() -> str:
    words = STORY.split()
    if len(words) != 6:
        raise ValueError(f"story must be exactly six words, got {len(words)}")
    # The file content is the story plus a trailing newline; keep the
    # total within the 60-character gate.
    content = STORY + "\n"
    if len(content) > 60:
        raise ValueError(f"entry must be at most 60 characters, got {len(content)}")
    if not STORY.strip():
        raise ValueError("story must not be only whitespace")
    return content


def main() -> None:
    content = validated_content()

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


if __name__ == "__main__":
    main()
