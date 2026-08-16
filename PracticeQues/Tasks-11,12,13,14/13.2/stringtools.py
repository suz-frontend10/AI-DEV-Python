__all__ = [
    "reverse",
    "is_palindrome",
    "count_vowels",
    "title_case",
    "remove_spaces"
]


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == text[::-1]


def count_vowels(text):
    return sum(1 for ch in text.lower() if ch in "aeiou")


def title_case(text):
    return text.title()


def remove_spaces(text):
    return text.replace(" ", "")


def _private_helper(text):
    return text.lower()