import medianarray


def test_integration_with_good_input_unequal():
    # given
    test_nums_one = [1, 3]
    test_nums_two = [2]

    expected_median = 2

    # when
    actual_median = medianarray.median_array(test_nums_one, test_nums_two)

    # then
    assert expected_median == actual_median


def test_integration_with_good_input_equal():
    # given
    test_nums_one = [1, 2]
    test_nums_two = [3, 4]

    expected_median = 2.5

    # when
    actual_median = medianarray.median_array(test_nums_one, test_nums_two)

    # then
    assert expected_median == actual_median
