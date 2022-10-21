def two_level_sort(scores):
    sorted_L = [ ]
    while scores != [ ]:
        # minentry[0] -> name, minentry[1] -> score
        minentry = scores[0]
        for i in range(len(scores)):
        # scores[i][0] -> name, scores[i][1] -> marks
            if scores[i][1] < minentry[1]:
                minentry = scores[i]
        # If scores are equal, check for alphabetical order
            elif (scores[i][1] == minentry[1] and
                scores[i][0] < minentry[0]):
                minentry = scores[i]
        sorted_L.append(minentry)
        scores.remove(minentry)
    return sorted_L