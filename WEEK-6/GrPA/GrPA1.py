def get_marks(scores_dataset, subject, gender):
    L = [ ]
    for student in scores_dataset:
        if student['Gender'] == gender:
            marks = student[subject]
            name = student['Name']
            L.append((name, marks))
    return L
def get_toppers(scores_dataset, subject, gender):# get the list of tuples
    L = get_marks(scores_dataset, subject, gender)
    toppers = [ ]
    maxmarks = 0
    for i in range(len(L)):
        # L[i][0] -> name, L[i][1] -> marks
        if L[i][1] > maxmarks:
            maxmarks = L[i][1]
        # if a new max is found,
        # create a new list and add L[i][0] as first element
            toppers = [L[i][0]]
        # if two have obtained same maximum, just append L[i][0] to current list
        elif L[i][1] == maxmarks:
            toppers.append(L[i][0])
    return toppers