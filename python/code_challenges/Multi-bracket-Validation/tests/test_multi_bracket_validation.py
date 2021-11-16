from multi_bracket_validation import __version__
from multi_bracket_validation.brackets import validate_brackets

def test_version():
    assert __version__ == '0.1.0'

def test_HappyPath():
    actual = validate_brackets("x={1:'o'}if(a=3)and[]")
    expected = True
    assert expected == actual 

def test_failure():
    actual = validate_brackets("{acasc[](()}")
    expected = False
    assert expected == actual 
def test_EdgeCase():
    actual = validate_brackets("{(})")
    expected = False
    assert expected == actual 