"""Testing trigrams function."""

import pytest
import re

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
    """Test parse_into_dict."""
    from trigrams import parse_into_dict
    assert value in parse_into_dict('./sherlock.txt')[key]


def test_gen_text():
    """Test that text generator returns output of chosen length."""
    from trigrams import gen_text
    fake_dict = {
        u'ipsum jaqgel': [u'sieds'],
        u'iwqsad asdiwef': [u'asdiuwdas'],
        u'jaqgel sieds': [u'iwqsad'],
        u'lorem ipsum': [u'jaqgel'],
        u'sieds iwqsad': [u'asdiwef']
    }
    output = gen_text(fake_dict, 200)
    assert len(output.split()) == 200


def test_cleanup():
    """Test that unwanted punctuation is removed."""
    from trigrams import cleanup
    fake = """
        This is my favorite fiiind i>i, idjivn jqj99_0 9(( ()
        f2,jhfuhef..,v)) WORDS OK>>>. not b8&d
    """
    assert len(re.sub('[a-zA-Z0-9\- ]', '', cleanup(fake))) == 0
