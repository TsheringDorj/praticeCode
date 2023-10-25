#To find average marks
def find_average_marks(marks):
    sum_of_marks = sum(marks)
    Total_subject = len(marks)
    average_marks = sum_of_marks / Total_subject
    return average_marks
def find_grade(avera_marks):
    if average_marks >= 80:
        grade = "A"
    elif average_marks >=70:
        grade = "B"
    else:
        grade = "F"
    return grade
marks = [70,71,72,73,74]
average_marks = find_average_marks(marks)
print("Your average mark is ", average_marks)

grade = find_grade(average_marks)
print("GRade is",grade)


