import pytest
import logic1

def main():
    testSquare()

def testSquare():

    assert logic1.square(2) == 4
    assert logic1.square(3) == 9
    assert logic1.square(4) == 16
    assert logic1.square(-2) == 4
    assert logic1.square(-4) == 16
    assert logic1.square(0) == 0

if __name__ == "__main__":
    main()


# Use "pytest EasyTest1.py" in integrated terminal