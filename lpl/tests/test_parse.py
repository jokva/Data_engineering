import os
import pytest
import lpl

@pytest.fixture
def datadir():
    return os.path.dirname(os.path.abspath(__file__)) + '/'

def test_parse(datadir):
    lpl.parse_lasfile(datadir + 'LAS30a.las')
