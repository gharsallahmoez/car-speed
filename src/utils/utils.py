# isValidCoordinateLength checks if coordinates length is valid based on requirements
# return bool
def isValidCoordinateLength(cords):
    return len(cords) == 3

# convertToInt converts list of string to list of int
# return List
def convertListToInt(new_cor):
    results = []
    try:
        results = list(map(int, new_cor))
    except ValueError:
        print("some coordinates are ignored because they are wrong!")
    return results
