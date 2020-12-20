def solution(w, q):
    result = []

    for i in range(len(q)):
        count = 0
        lenAll = len(q[i])

        startQ = q[i].find("?")
        endQ = startQ + q[i].count("?")-1

        fStartQ = 0
        fEndQ = 0

        if startQ == 0:
            fStartQ = endQ + 1
            fEndQ = lenAll - 1
        else:
            fStartQ = 0
            fEndQ = startQ - 1
        for j in range(len(w)):
            if len(w[j]) == len(q[i]):

                final = w[j][fStartQ: fEndQ + 1]
                compare = q[i][fStartQ: fEndQ + 1]
                if(final == compare):
                    count = count + 1

        result.append(count)

    return result
