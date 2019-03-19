import orderdep


def test_integration_with_good_input():
    # given
    test_filenames = ["a", "b", "c", "d", "e", "f"]
    test_dependencies = [("c", "d"), ("d", "a"), ("d", "b"), ("a", "f"), ("b", "f")]

    expected_order = ["e", "f", "a", "b", "d", "c"]

    # when
    actual_order = coding_prep.orderDep(test_filenames, test_dependencies)

    # then
    assert expected_order == actual_order
