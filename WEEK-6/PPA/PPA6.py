def get_marks(scores_dataset, subject):
    L = [ ]
    for student in scores_dataset:
        marks = student[subject]
        name = student['Name']
        L.append((name, marks))
    return L
print(get_marks(100, 'Physics'))