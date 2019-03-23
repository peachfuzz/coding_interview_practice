import concattwostrings

import pytest

# I am going to break up your tests here. 
# It is good practice to have only one test per function.
# This is used to calculate test covereage, number of tests,
# and it can be easier to see why your tests fail as your 
# projects get bigger. - Thomas

# The other thing that is useful about writing short tests 
# is you can copy paste most of the code and just change 
# the top test values under "given"

def test_concat_two_strings_with_overlap_a_then_b():
    # given
    test_string_a = "The quick brown"
    test_string_b = "brown fox."

    expected_response = "The quick brown fox."

    # when 
    actual_response = concattwostrings.concat(test_string_a, test_string_b)

    # then
    assert expected_response == actual_response


def test_concat_two_strings_with_overlap_b_then_a():
    # given
    test_string_a = "brown fox."
    test_string_b = "The quick brown"

    expected_response = "The quick brown fox."

    # when 
    actual_response = concattwostrings.concat(test_string_a, test_string_b)

    # then
    assert expected_response == actual_response


# Here I wrote tests for the "ambiguous" and "no overlap" cases that
# expect the function to throw ValueErrors. For this to work, you will
# need the `pytest` module.

def test_check_overlap_ambiguous():
    # given
    test_string_a = "the lazy dog. The quick brown fox jumped"
    test_string_b = "fox jumped over the lazy dog."

    expected_error_value = ValueError(
        "There is ambiguity between which input is first:\n"
        + f"String A: {test_string_a}\n"
        + f"String B: {test_string_b}"
    )

    # when
    with pytest.raises(ValueError) as actual_error:
        actual_response = concattwostrings.concat(test_string_a, test_string_b)


def test_check_no_overlap():
    # given
    test_string_a = "The quick brown fox jumped"
    test_string_b = "the lazy dog."

    expected_error_value = ValueError(
        "There is no overlap between input A and B:\n"
        + f"String A: {test_string_a}\n"
        + f"String B: {test_string_b}"
    )

    # when
    with pytest.raises(ValueError) as actual_error:
        actual_response = concattwostrings.concat(test_string_a, test_string_b)


def test_integration_with_good_input():
    # given
    test_str1 = "The quick brown"
    test_str2 = "The quick"
    test_str3 = "The quick brown fox jumped"
    test_str4 = "brown fox jumped."
    test_str5 = "brow n fox jumped."
    test_str6 = "nothing is equal but The"

    test_combo14 = "The quick brown fox jumped."  # (1,4), (3,4)
    test_combo16 = "The quick brownothing is equal but The"
    test_combo26 = "nothing is equal but The quick"
    test_combo36 = "nothing is equal but The quick brown fox jumped"
    test_combofail = ""  # (1,5), (2,4), (2,5), (3,5)

    # when
    actual_string14 = concattwostrings.concat(test_str1, test_str4)
    actual_string16 = concattwostrings.concat(test_str1, test_str6)
    actual_string34 = concattwostrings.concat(test_str3, test_str4)  # == (1,4)
    actual_string26 = concattwostrings.concat(test_str2, test_str6)
    actual_string36 = concattwostrings.concat(test_str3, test_str6)
    actual_string_self = concattwostrings.concat(test_str1, test_str1)

    # then
    assert actual_string14 == test_combo14
    assert actual_string16 == test_combo16
    assert actual_string34 == test_combo14  # == (1,4)
    assert actual_string26 == test_combo26
    assert actual_string36 == test_combo36
    assert actual_string_self == test_str1

