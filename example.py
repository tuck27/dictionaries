names = ["Maya", "JP", "Erica", "Vincent"] #defining a list
grades = ["100", "99", "98", "80"]

#accessing names using a for loop in a list
#student_names is a variable only used in a list

#for student_names in name:
   # print(student_names)

for i in range(len(names)):
    print(f"{names[i]}'s grade is {grades[i]}")