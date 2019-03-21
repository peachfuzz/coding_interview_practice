# todo: first line doesn't highlight via better comments
# todo:
# * highlighted
# ! important
# ? questions
# // strikethrough
def concat(s1, s2):
    # idea: start from the end of both strings
    # ex: I am at the
    # ex:     the end
    # end = end ? check next : move down
    liststr1 = list(s1)
    liststr2 = list(s2)
    len1 = len(liststr1)
    len2 = len(liststr2)
    temp_answer_pos1 = 0
    temp_answer_pos2 = len2  # 0

    # pseudocode:
    # check st1 end to s2 end
    # if match, check next one down
    # else move s2 down 1

    # if no match by the end of iteration, check the other way

    # if len1 > len2:  # AABBCC, AABBCCC
    #     answer = concat(s2, s1)  # I want the first string to always be shorter
    #     return answer
    # else:
    #                    var 0 - end                    0 - var len

    answer = liststr1[temp_answer_pos1:] + liststr2[:temp_answer_pos2]
    # magic calculation
    return "".join(answer)  # making that list into a string

