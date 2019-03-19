import urlstring


def test_integration_with_good_input():
    # given
    test_string = "    hello,  world! This is a URL    .  "
    test_string1 = "      ."
    test_string2 = ".      "

    expected_string = "hello,%20world!%20This%20is%20a%20URL%20."
    expected_string1 = "."
    expected_string2 = "."
    # when
    actual_string = urlstring.urlify(test_string)
    actual_string1 = urlstring.urlify(test_string1)
    actual_string2 = urlstring.urlify(test_string2)
    # then
    assert expected_string == actual_string
    assert expected_string1 == actual_string1
    assert expected_string2 == actual_string2
