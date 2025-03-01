""" Test Utils module 

Testing all the static methods of Utils class that are reused in other modules.
"""
# from http.client import responses
from typing import Iterator, Type
import pytest
from bs4 import BeautifulSoup
from pipeline.utilities.utils import Utils

@pytest.mark.parametrize("text, expected_result", [
    ("", ""),
    ("\n", ""),
    ("INVALIDTEXT","invalidtext")
])
def test_get_valid_text(text: str, expected_result: str) -> None:
    """Test get_valid_text"""
    result = Utils.get_valid_text(text)
    assert result == expected_result

@pytest.mark.parametrize("text, expected_result", [
    ("INVALIDTEXT", "invalidtext"),
    ("INVALIDTEXT\n\n\n", "invalidtext"),
    (None, "N/A")
])
def test_get_valid_value(text: str, expected_result: str) -> None:
    """Test valid value is returned"""
    result = Utils.get_valid_value(text)
    assert result == expected_result

@pytest.mark.parametrize("text, expected_result", [
    ("1, 2, 3, 4, 5", [1, 2, 3, 4, 5]),
    ("2,123,235 31",[2123235, 31]),
])
def test_get_numbers_from_string(text,expected_result) -> None:
    """Test get_numbers_from_string"""
    result = Utils.get_numbers_from_string(text)
    assert result == expected_result

@pytest.mark.parametrize("search_word, text, expected_result", [
    ("python", "python is great", True),
    ("python", "pythons is great", False),
    ("java", "all programming languages're great", False),
])
def test_is_word_found(search_word: str, text: str, expected_result: bool) -> None:
    """Test is_word_found"""
    result = Utils.is_word_found(search_word, text)
    assert result is expected_result

@pytest.mark.parametrize("search_words, text, expected_result", [
    (["python", "java"], "python is great", False),
    (["python", "java"], "java is great", False),
    (["python", "java"], "python is great and java is great", True),
    (["python", "java"], "python is great and java is great and python is great", True),
    (["python", "java"], "all programming languages're great", False),
])
def test_are_all_words_found(search_words: list[str], text: str, expected_result: bool) -> None:
    """Test are_words_found"""
    result = Utils.are_all_words_found(search_words, text)
    assert result is expected_result

def test_get_configs() -> None:
    """Test get_configs"""
    configs_path = "app/etl/settings/pipeline_configs.yaml"
    configs = Utils.get_configs(configs_path)
    expected_result = dict
    assert isinstance(configs, expected_result)

    
