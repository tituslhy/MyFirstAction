from main import string_add, string_remove

def test_string_add():
    assert string_add("Hello", "there!") == "Hello there!"

def test_string_remove():
    assert string_remove(
        "Hello hello!",
        " hello"
    ) == "Hello!"