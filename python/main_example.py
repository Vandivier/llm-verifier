def add(a: int, b: int) -> int:
    """Returns the sum of two integers."""
    return a + b


def is_palindrome(s: str) -> bool:
    """Checks whether a given string is a palindrome."""
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
