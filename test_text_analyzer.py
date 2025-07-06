import pytest
from text_analyzer import TextAnalyzer

def test_word_count():
    analyzer = TextAnalyzer("Hello world hello")
    assert analyzer.word_count() == 3

def test_unique_words():
    analyzer = TextAnalyzer("Hello world hello")
    assert analyzer.unique_words() == {"hello", "world"}

def test_most_common_word():
    analyzer = TextAnalyzer("Hello world hello")
    assert analyzer.most_common_word() == "hello"

def test_replace_word():
    analyzer = TextAnalyzer("Hello world")
    assert analyzer.replace_word("Hello", "Hi") == "Hi world"

def test_empty_text():
    analyzer = TextAnalyzer("")
    assert analyzer.word_count() == 0
    assert analyzer.unique_words() == set()
    assert analyzer.most_common_word() == ""