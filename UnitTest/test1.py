import logic1

def main():
    testSquare()

def testSquare():
    try:
        assert logic1.square(2) == 4
    except AssertionError as e:
        print(e)
        print("err occured")
    try:
        assert logic1.square(3) == 9
    except AssertionError as e:
        print(e)
        print("err occured")
    try:
        assert logic1.square(4) == 16
    except AssertionError as e:
        print(e)
        print("err occured")
    try:
        assert logic1.square(-4) == 16
    except AssertionError as e:
        print(e)
        print("err occured")
    try:
        assert logic1.square(0) == 0
    except AssertionError as e:
        print(e)
        print("err occured")

if __name__ == "__main__":
    main()