# test code transcribed from
# https://www.tutorialspoint.com/pytest/pytest_quick_guide.htm
# tips for good unit tests
# https://myenigma.hatenablog.com/entry/2022/04/24/143753

# run the test just by:
# pytest
# (or -v for verbose description)

import math

def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

def testsquare():
    num = 7
    assert 7*7 == 40

def tesequality():
    assert 10 == 11
