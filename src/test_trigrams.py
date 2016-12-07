"""Testing trigrams function."""

import pytest

PARAMS_TABLE = [
    ['One night', 'it'],
    ['when my', 'way'],
    ['were brilliantly', 'lit'],
    ['He was', 'pacing'],
    ['He was', 'at'],
    ['was shown', 'up'],
    ['his attitude', 'and']
]


@pytest.mark.parametrize("word, result", PARAMS_TABLE)
def test_parse_into_dict(word, result):
    """"""
    from trigrams import parse_into_dict
    assert result in parse_into_dict('./sherlock.txt')[word]
