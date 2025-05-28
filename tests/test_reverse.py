from src.reverse import reverse_string

def test_up_reverse():
    assert reverse_string('skypro') == 'orpyks'
    assert reverse_string('111') == '111'
    assert reverse_string('') == ''

import pytest

@pytest.mark.parametrize("string, expected_result", [
    ("hello", "olleh"),
    ("world", "dlrow"),
    ("12345", "54321"),
    ("", ""),
])
def test_reverse_string(string, expected_result):
    assert reverse_string(string) == expected_result