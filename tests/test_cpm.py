import pytest
import numpy as np

from cpm.cpm.something import something

def test_something():
    """testing something"""

    input = 3

    output = 4

    test = something(input)
    
    check = test == output
    assert check.all()
