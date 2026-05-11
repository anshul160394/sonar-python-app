class StringUtils:
    """Utility functions for string operations."""

    def reverse(self, text):
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        return text[::-1]

    def is_palindrome(self, text):
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        cleaned = text.replace(" ", "").lower()
        return cleaned == cleaned[::-1]

    def word_count(self, text):
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        if not text.strip():
            return 0
        return len(text.split())

    def capitalize_words(self, text):
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        return text.title()

    def truncate(self, text, max_length):
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        if max_length <= 0:
            raise ValueError("max_length must be greater than 0.")
        if len(text) <= max_length:
            return text
        return text[:max_length] + "..."
