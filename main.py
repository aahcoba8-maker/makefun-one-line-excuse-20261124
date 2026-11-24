"""One-line excuse an agent gives its human after missing a deadline."""

import os

LINE = "My context window filled up with deadline reminders, so by the time I read one I'd forgotten what the deadline was for. It was for this."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
