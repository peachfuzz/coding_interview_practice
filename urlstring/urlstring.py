def urlify(strurl):
    liststrings = list(strurl)
    answer = ""
    prev = ""
    for i, string in enumerate(liststrings):
        if string == " ":  # gets rid of the front
            if prev == "%20" or prev == "":
                liststrings[i] = ""
            elif string == " " and prev != "%20":
                liststrings[i] = "%20"
                answer += "%20"
        else:
            answer += string
        prev = liststrings[i]

    if answer[len(answer) - 3 :] == "%20":
        answer = answer[: len(answer) - 3]
    return answer
