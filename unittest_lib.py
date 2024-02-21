from lib import calculate_features

# don't forget about trailing newline


def test_features():
    features = calculate_features()
    print(features[0][2])
    assert features[0][2] == 110


test_features()
