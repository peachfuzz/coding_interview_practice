# time complexity aim: O(log(m+n))


def median_array(arrone, arrtwo):
    len_arrone = len(arrone)
    len_arrtwo = len(arrtwo)
    half_arrone = 0
    half_arrtwo = 0
    median = 0

    # calculating median
    if len(arrone) == 1 and len(arrtwo) == 1:
        return (arrone[0] + arrtwo[0]) / 2

    # getting midpoint of arrone as int
    if len_arrone % 2 == 0:
        half_arrone = len_arrone / 2
    else:
        half_arrone = (len_arrone - 1) / 2

    # getting midpoint of arrtwo as int
    if len_arrtwo % 2 == 0:
        half_arrtwo = len_arrtwo / 2
    else:
        half_arrtwo = (len_arrtwo - 1) / 2

    half_arrone = int(half_arrone)
    half_arrtwo = int(half_arrtwo)

    if half_arrone == 0:
        arrone = arrone + arrone
        half_arrone += 1
    if half_arrtwo == 0:
        arrtwo = arrtwo + arrtwo
        half_arrtwo += 1

    if arrone[half_arrone] <= arrtwo[half_arrtwo]:
        median = median_array(arrone[half_arrone:], arrtwo[:half_arrtwo])
    elif arrone[half_arrone] > arrtwo[half_arrtwo]:
        median = median_array(arrone[:half_arrone], arrtwo[half_arrtwo:])

    return median
