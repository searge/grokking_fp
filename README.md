# Grokking Functional Programming - Python Exercises

This repository contains my personal solutions and notes for the exercises in the book ["Grokking Functional Programming"](https://www.manning.com/books/grokking-functional-programming "null") by Michał Płachta. The goal is to practice functional programming concepts in a modern Python (3.13+) environment.

[The official code examples](https://github.com/miciek/grokkingfp-examples "null") for the book.

## Setup

This project uses `uv` for fast dependency and environment management.

1. **Create a virtual environment:**

    ```bash
    uv venv
    ```

2. **Activate the environment:**

    ```bash
    # On macOS/Linux
    source .venv/bin/activate
    ```

3. **Install all dependencies:**

    ```bash
    uv pip install -e ".[dev]"
    ```

## How to Run an Exercise

All exercises are located in the `src/` directory. To run a specific script, use the `python` command from the root of the project.

For example, to run an exercise from Chapter 2:

```bash
python src/grokking_fp/ch02_pure_functions/01_what_is_purity.py
```

## Code Quality & Debugging

We use `ruff` for linting/formatting and `mypy` for type checking.

- **Check your code:**

    ```bash
    # Format code
    ruff format .

    # Lint and fix issues
    ruff check . --fix

    # Check types
    mypy src
    ```

- **Debugging:** The simplest way to debug a script is to place a breakpoint directly in the code. Just add `breakpoint()` where you want the debugger to start.

    ```python
    def my_function(data):
        # ... some logic ...
        breakpoint() # The script will pause here
        # ... rest of the logic ...
    ```

    Then run the script as usual.

## Project Structure

The code is organized by book chapters to make it easy to find specific exercises.

```bash
.
├── docs/
│   └── CODING_GUIDELINES.md
├── pyproject.toml
└── src/
    └── grokking_fp/
        ├── ch01_introduction/
        │   └── 01_first_example.py
        └── ch02_pure_functions/
            └── 01_what_is_purity.py
```
