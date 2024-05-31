grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Stive', 'Khendrik', 'Aaron'}

grades_ = sum(grades[0])
len_ = len(grades[0])
average_score_ = grades_ / len_

grades_1 = sum(grades[1])
len_1 = len(grades[1])
average_score_1 = grades_1 / len_1

grades_2 = sum(grades[2])
len_2 = len(grades[2])
average_score_2 = grades_2 / len_2

grades_3 = sum(grades[3])
len_3 = len(grades[3])
average_score_3 = grades_3 / len_3

grades_4 = sum(grades[4])
len_4 = len(grades[4])
average_score_4 = grades_4 / len_4

students = list(students)
students.sort()

grades = [average_score_, average_score_1, average_score_2, average_score_3, average_score_4]

list_ = dict(zip(students, grades))
print(list_)



