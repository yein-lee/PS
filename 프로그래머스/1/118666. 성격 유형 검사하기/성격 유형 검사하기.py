def solution(survey, choices):
    scores = [0, 0, 0, 0] # RT, CF, JM, AN
    for s, c in zip(survey, choices):
        if s == "RT":
            scores[0] += c - 4
        elif s == "CF":
            scores[1] += c - 4
        elif s == "JM":
            scores[2] += c - 4
        elif s =="AN":
            scores[3] += c - 4
        elif s == "TR":
            scores[0] -= c - 4
        elif s == "FC":
            scores[1] -= c - 4 
        elif s == "MJ":
            scores[2] -= c - 4 
        elif s == "NA":
            scores[3] -= c - 4 

    answer = ''
    if scores[0] <= 0:
        answer += "R"
    else:
        answer += "T"
    if scores[1] <= 0:
        answer += "C"
    else:
        answer += "F"
    if scores[2] <= 0:
        answer += "J"
    else:
        answer += "M"
    if scores[3] <= 0:
        answer += "A"
    else:
        answer += "N"
    return answer