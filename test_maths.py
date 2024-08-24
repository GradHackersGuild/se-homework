import sys
import maths as OPs

def test_addition():
    assert OPs.addition(5,3) == 8

def test_multiplication():
    assert OPs.multiplication(6,6) == 36

#pytest==8.3.2
# pytest-cov==5.0.0
#coverage==7.6.1