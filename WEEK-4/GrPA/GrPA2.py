def solution(marks):
    ### Enter your solution below this line
    ### Indent your entire code by one unit (4 spaces) to the right
    

    marks_sort = []
    for x in range(len(marks)):
        marks_sort.append(min(marks))
        marks.remove(min(marks))
    if len(marks_sort)%2 ==0:
        median = (((marks_sort[(int(len(marks_sort)//2))-1] +
marks_sort[(int(len(marks_sort)//2)+1)-1])/2))
    elif len(marks_sort)%2 != 0:
        median = (marks_sort[(((int(len(marks_sort)))+1)//2)-1])
### Enter your solution above this line

    ### Enter your solution above this line
    return median