# Python Engineering

My solutions to the exercises, labs and exams from the **SoftUni Python** track — from the very first `print()` to object-oriented programming.

This repo is my learning log. The code is written while studying, so early folders will look rougher than later ones. That's the point.

## Modules

| Module | Folder | Status |
|---|---|---|
| Programming Basics with Python | [`python_basics`](./python_basics) | In progress |
| Python Fundamentals | [`python_fundamentals`](./python_fundamentals) | In progress |
| Python Advanced | `python_advanced` | Planned |
| Python OOP | `python_oop` | Planned |

## Structure

Each module is split by topic, numbered in the order it's taught:

```
python_basics/
├── 01.first_steps_in_coding/
│   ├── lab/
│   ├── exercise/
│   └── more_exercises/
├── 02.conditional_statements/
└── ...
exams/
└── <date>_<exam_name>/
```

- **lab** — problems solved together in class
- **exercise** — homework problems
- **more_exercises** — optional extra practice
- **exams** — solutions to past and mock exams

## Running the code

Each file is a standalone script. Python 3.10+ recommended.

```bash
python python_basics/01.first_steps_in_coding/lab/hello_softuni.py
```

Most problems read from standard input, so type the input after running, or pipe it in:

```bash
echo "5" | python path/to/script.py
```

## Notes

- Problem statements belong to [SoftUni](https://softuni.bg) and are not included here. Test your own solutions in the SoftUni Judge system.
- These are *my* solutions, not official ones. If you're a SoftUni student — solve it yourself first, then compare.

## License

[GPL-3.0](./LICENSE)
