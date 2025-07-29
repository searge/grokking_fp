# Coding Guidelines

## 1. Guiding Principles

The goal is to write clean, readable, and robust code for the "Grokking Functional Programming" exercises. Our approach is guided by three core principles:

1. **Functional First**: We solve problems declaratively. We prefer pure functions, composition, and expressions over statements.
2. **Immutability**: Data should be immutable by default. Instead of changing data, create a new copy with the updated values.
3. **Strict Typing**: All code must be fully and explicitly typed. Types are our primary form of documentation and error prevention.

## 2. Tooling: The Single Source of Truth

Our coding style is enforced automatically by tools. **There are no style arguments.**

- **`ruff`**: The primary tool for formatting and linting.
- **`mypy`**: The tool for static type checking.

Always run these tools before committing code:

```bash
# Format your code
ruff format .

# Lint and auto-fix issues
ruff check . --fix

# Check types
mypy src
```

## 3. Core Style Rules

These rules are configured in `pyproject.toml` and enforced by `ruff`.

- **Line Length**: Max 79 characters.
- **Quotes**: Use double quotes (`"`).
- **Docstrings**:
  - Every public module, class, and function must have a docstring.
  - Use the `numpy` docstring convention.
  - Use simple English sentences.

A minimal `numpy` docstring example:

```python
"""A one-line summary of the function's purpose."""

def my_function(param1: int) -> str:
    """
    A more detailed explanation of what the function does.

    Parameters
    ----------
    param1 : int
        A description of the parameter.

    Returns
    -------
    str
        A description of the return value.
    """
    return str(param1)
```

## 4. Functional Programming Patterns with `returns`

We use the `returns` library to apply functional patterns idiomatically in Python.

### 4.1. Handling Optional Values with `Maybe`

Instead of returning `None` or using `Optional[T]`, use the `Maybe` container. It makes missing values explicit and safe to chain.

- **Don't do this:**

    ```python
    def find_item(items: list[int], item: int) -> int | None:
        return item if item in items else None
    ```

- **Do this:**

    ```python
    from returns.maybe import Maybe

    def find_item(items: list[int], item: int) -> Maybe[int]:
        return Maybe.from_value(item if item in items else None)
    ```

### 4.2. Handling Errors with `Result`

Instead of `try...except` blocks, use the `Result` container for functions that can fail. This makes error handling a predictable part of your data flow. The `@safe` decorator is the easiest way to achieve this.

- **Don't do this:**

    ```python
    def to_int(text: str) -> int:
        try:
            return int(text)
        except ValueError:
            # How do we handle this? Raise? Return -1?
            raise
    ```

- **Do this:**

    ```python
    from returns.result import Result, safe

    @safe
    def to_int(text: str) -> Result[int, ValueError]:
        """Returns Success(number) or Failure(ValueError)."""
        return int(text)
    ```

### 4.3. Handling Side Effects with `IO`

Pure functions cannot perform I/O (like `print`, file access, or network requests). To keep your core logic pure, wrap side effects in `IO` containers. This pattern is often called **"Functional Core, Imperative Shell"**.

- **Don't mix logic and I/O:**

    ```python
    def process_and_print(text: str):
        # Business logic mixed with a side effect:
        processed = text.upper()
        print(processed) # Impure!
    ```

- **Do this (separate logic from effects):**

    ```python
    from returns.io import IO

    def process(text: str) -> str:
        """This function is pure and easy to test."""
        return text.upper()

    def create_printable_io(text: str) -> IO[None]:
        """This function describes the side effect but doesn't run it."""
        return IO(print(text))

    # In your main script (the "Imperative Shell"):
    pure_result = process("hello")
    io_action = create_printable_io(pure_result)
    # The side effect is executed here, at the edge of the program:
    io_action.unsafe_perform_io()
    ```

This approach keeps your business logic testable and predictable, while clearly isolating the "impure" parts of your application.
