import pytest
from app.string_utils import StringUtils

@pytest.fixture
def utils():
    return StringUtils()

def test_reverse(utils):
    assert utils.reverse("hello") == "olleh"
    assert utils.reverse("") == ""
    assert utils.reverse("a") == "a"

def test_reverse_invalid_type(utils):
    with pytest.raises(TypeError):
        utils.reverse(123)

def test_is_palindrome_true(utils):
    assert utils.is_palindrome("racecar") is True
    assert utils.is_palindrome("A man a plan a canal Panama") is True

def test_is_palindrome_false(utils):
    assert utils.is_palindrome("hello") is False

def test_is_palindrome_invalid_type(utils):
    with pytest.raises(TypeError):
        utils.is_palindrome(None)

def test_word_count(utils):
    assert utils.word_count("hello world") == 2
    assert utils.word_count("") == 0
    assert utils.word_count("one") == 1

def test_word_count_invalid_type(utils):
    with pytest.raises(TypeError):
        utils.word_count(42)

def test_capitalize_words(utils):
    assert utils.capitalize_words("hello world") == "Hello World"
    assert utils.capitalize_words("devops engineer") == "Devops Engineer"

def test_truncate(utils):
    assert utils.truncate("Hello World", 5) == "Hello..."
    assert utils.truncate("Hi", 10) == "Hi"
    assert utils.truncate("Exact", 5) == "Exact"

def test_truncate_invalid_length(utils):
    with pytest.raises(ValueError, match="greater than 0"):
        utils.truncate("Hello", 0)

def test_truncate_invalid_type(utils):
    with pytest.raises(TypeError):
        utils.truncate(123, 5)
