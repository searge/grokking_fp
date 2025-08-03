# Grokking Functional Programming

Personal solutions and notes for exercises from ["Grokking Functional Programming"](https://www.manning.com/books/grokking-functional-programming) by Michał Płachta.
Each exercise is implemented in both **Python** and **Scala** to compare functional programming approaches across languages.

[The official code examples](https://github.com/miciek/grokkingfp-examples "null") for the book.

## Quick Start

### Python + Scala Environment (Recommended)

```bash
# Enter Nix shell with both languages
nix develop

# Run exercises
task run:scala -- Ch01Intro
task run:py -- ch01_intro
```

### Python Only

```bash
# Setup Python environment
task setup
source .venv/bin/activate

# Run Python exercises
task run:py -- ch01_intro
```

## Project Structure

```bash
src/
├── main/                         # Python exercises
│   └── ch01_intro.py
└── scala/                        # Scala exercises
    └── Ch01Intro.scala
```

## Available Commands

```bash
# Run `task` with no arguments to list available tasks
task

# Environment
task setup                        # Setup development environment

# Run exercises
task run:py -- ch01_intro         # Run Python exercise
task run:scala -- Ch01Intro       # Run Scala exercise
task list                         # List all exercises

# Code quality
task check:py                     # Format and lint Python code
task clean:artifacts              # Clean build artifacts
task clean:nix                    # Clean Nix garbage (free up disk space)
```

## Key Technologies

- **Python 3.13** with `returns` library for functional patterns
- **Scala 3** for native functional programming
- **Nix** for reproducible development environment
- **Task** for simple command runner

## Learning Approach

Both implementations follow the same exercises but showcase different approaches:

- **Python**: Functional patterns using `returns` library (Maybe, Result, IO)
- **Scala**: Native functional programming with immutable data structures

Each exercise includes both imperative and declarative solutions to demonstrate the evolution toward functional thinking.
