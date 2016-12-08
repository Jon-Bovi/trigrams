"""Testing trigrams function."""

import pytest
import re
import random

PARAMS_TABLE = [
    ['one night', 'it'],
    ['when my', 'way'],
    ['were brilliantly', 'lit'],
    ['he was', 'pacing'],
    ['he was', 'at'],
    ['was shown', 'up'],
    ['his attitude', 'and']
]


@pytest.mark.parametrize("key, value", PARAMS_TABLE)
def test_parse_into_dict(key, value):
    """Test parse_into_dict """
    from trigrams import parse_into_dict
    assert value in parse_into_dict('./sherlock.txt')[key]


def test_main_length():
    """Test that text generator returns output of chosen length."""
    from trigrams import main
    num = random.randrange(0, 200)
    output = main('./sherlock.txt', num)
    assert len(output.split()) == num


def test_cleanup():
    """Test that unwanted punctuation is removed."""
    from trigrams import cleanup
    fake = """
        This is my favorite fiiind i>i, idjivn jqj99_0 9(( ()
        f2,jhfuhef..,v)) WORDS OK>>>. not b8&d
    """
    assert len(re.sub('[a-zA-Z0-9\- ]', '', cleanup(fake))) == 0
