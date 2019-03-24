def binary_sort(nums):
    if len(nums) > 2:
        split_nums_first = binary_sort(nums[len(nums) :])
        split_nums_second = binary_sort(nums[: len(nums)])
        ordered_first_second = []
        length_combo = len(split_nums_first) + len(split_nums_second)
        i = 0
        j = 0
        while len(ordered_first_second) < length_combo:
            if split_nums_first[i] < split_nums_second[j]:
                ordered_first_second.append(split_nums_first[i])
                i += 1
                if i == len(split_nums_second):
                    ordered_first_second.append(split_nums_second[j:])
            else:
                ordered_first_second.append(split_nums_second[j])
                j += 1
                if j == len(split_nums_second):
                    ordered_first_second.append(split_nums_first[i:])

        return ordered_first_second

    if len(nums) == 1:
        return nums

    else:
        if nums[0] < nums[1]:
            return nums
        else:
            return [nums[1], nums[0]]


if __name__ == "__main__":
    test_list = [16, 2, 3, 20, 1, 0]
    expected_list = [0, 1, 2, 3, 16, 20]
    actual_list = binary_sort(test_list)
    assert expected_list == actual_list

