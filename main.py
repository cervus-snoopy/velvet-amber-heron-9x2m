import os

LINES = [
    "An echo is a wall playing catch with your voice \u2014 you throw a shout at it, and it throws the same shout back to you.",
    "It works because your shout really does travel to the wall and bounce back, but it leaves out that the wall isn't catching anything \u2014 your voice comes back quieter and a little scrambled, and the wall never chooses to answer.",
]


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    os.chmod(out_dir, 0o755)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(LINES))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
