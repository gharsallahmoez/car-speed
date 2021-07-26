from utils import isValidCoordinateLength,convertListToInt

# valid test
def test_isValidCoordinateLength():
    assert isValidCoordinateLength([2,1,3])

# invalid test
def test_isValidCoordinateLength():
    assert not isValidCoordinateLength([2,1])

# valid test for convertListToInt
def test_convertListToInt():
    list = ['1','2','3']
    result = convertListToInt(list)
    assert all(isinstance(x, int) for x in result)
