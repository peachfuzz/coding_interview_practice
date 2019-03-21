import concattwostrings


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

