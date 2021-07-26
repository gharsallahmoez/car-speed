from calcul import distance, duration, calcul_speed


# valid test for distance function
def test_distance():
    expected = 5
    result = distance(1,2,4,6)
    assert result == expected

# invalid test for distance function
def test_invalid_distance():
    wrong_result = 2
    result = distance(1,2,4,6)
    assert result != wrong_result

# valid test for duration function
def test_duration():
    expected = 4
    result = duration(2,6)
    assert result == expected

# invalid test for duration function
def test_invalid_duration():
    wrong_result = 2
    result = duration(2,6)
    assert result != wrong_result

# valid test for speed function
def test_speed():
    input = [[0,0,0],[1,4,2],[6,8,6],[3,2,9]]
    expected = 1.914937088394431
    result = calcul_speed(input)
    assert result == expected

# valid test for speed function
def test_invalid_speed():
    input = [[0,0,0],[1,4,2],[6,8,6],[3,2,9]]
    wrong_result = 5
    result = calcul_speed(input)
    assert result != wrong_result
