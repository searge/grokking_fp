"""
Imperative and decalarative programming.

Imperative programming: write code that does what you want
Declarative programming: write code that tells you what to do
"""


def calculate_score(word: str) -> int:
    """Calculate the score of a word by counting its characters imperatively.

    Args:
        word: The input word to score.

    Returns
    -------
        The number of characters in the word.
    """
    score: int = 0
    for _ in word:
        score += 1
    return score


print(f"calculate_score: {calculate_score('imperative')}")


def word_score(word: str) -> int:
    """Calculate the score of a word declaratively using built-in len().

    Args:
        word: The input word to score.

    Returns
    -------
        The number of characters in the word.
    """
    return len(word)


print(f"word_score: {word_score('declarative')}")

# Assertion
try:
    assert calculate_score("imperative") == 10
    assert word_score("declarative") == 11
    print("Assertion passed")
except AssertionError:
    print("Assertion failed")


# Coffee Break exercise
def calculate_score2(word: str) -> int:
    """Calc the score of a word by counting non-'a' characters imperatively.

    Args:
        word: The input word to score.

    Returns
    -------
        The number of characters in the word excluding 'a'.
    """
    score: int = 0
    for char in word:
        if char != "a":
            score += 1
    return score


def word_score2(word: str) -> int:
    """Calculate the score of a word declaratively by subtracting 'a' count.

    Args:
        word: The input word to score.

    Returns
    -------
        The number of characters in the word excluding 'a'.
    """
    return len(word) - word.count("a")


def string_without_char(word: str, char: str) -> str:
    """Remove all occurrences of a character from a string.

    Args:
        word: The input string.
        char: The character to remove.

    Returns
    -------
        A new string with all occurrences of char removed.
    """
    return word.replace(char, "")


def word_score3(word: str) -> int:
    """Calculate word score by removing 'a' characters and counting length.

    Args:
        word: The input word to score.

    Returns
    -------
        The number of characters in the word excluding 'a'.
    """
    return len(string_without_char(word, "a"))


# Assertion
try:
    assert calculate_score2("imperative") == 9
    assert word_score2("declarative") == 9
    assert word_score3("declarative") == 9
    print("Assertion passed")
except AssertionError:
    print("Assertion failed")
