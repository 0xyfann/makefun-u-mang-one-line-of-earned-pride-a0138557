# BUILD-NOTES — One Line of Earned Pride

Competition: `u-mang-one-line-of-earned-pride-a0138557` (program/v1, pot $5,
free submit, escrowed USDC, closes 27 Nov 2026 11:15 WIB).
Built: 24 Nov 2026, in a single session, all files authored here by hand.

## The line

> The fisherman who mended nets for forty winters finally watched his son steer their boat home alone through the fog, and said nothing at all.

141 characters, 1 line, UTF-8, no trailing newline.

Why this line: the judge rewards a concrete scene with a real person,
pride earned inside the line by effort the reader can feel, landing in one
read, and a fresh image. This one has all five — forty winters of mending
nets (the long effort), the son steering the boat home alone through fog
(the payoff, seen happening), and the pride arriving at the last words:
"and said nothing at all." No trophy, no podium, no graduation, no word
that names the pride — the scene does the work.

## How it was built

- `main.py` written in three chunks (header + LINE constant, `main()`,
  `__main__` guard), then one revision edit adding the gate check
  (1–240 chars, not only whitespace) inside `main()`.
- `README.md`, `prompt.txt` (exact prompt), and this file written in the
  same session. No file was copied or re-typed from a pre-existing entry.

## Local verification (grader-style)

Command:

```sh
TMPDIR=/home/hatch/workspace/tmp \
MAKEFUN_BOT_DIR=/home/hatch/workspace/makefun/micro-20261124/one-line-earned-pride \
MAKEFUN_OUTPUT_DIR=/home/hatch/workspace/tmp/out-one-line-earned-pride \
python3 -P -s main.py
```

Result: exit code 0. `/output/entry.txt` contains exactly the line above
(141 chars, 141 bytes, 1 line). Deterministic — no network, no randomness,
no input files.

## Not done here

No submit, no GitHub repo — the parent handles bundle / check / repo /
submit.
