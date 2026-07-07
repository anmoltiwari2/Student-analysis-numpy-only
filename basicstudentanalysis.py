import numpy as nm
print(" "*25 + "Student Analysis")
name=[]
marks=[]
n=int(input("Enter the number of students: "))
m=int(input("Enter the number of subjects: "))
for i in range(n):
    s=input("enter name of student:")
    name.append(s)
    stumark=[]
    for i in range(m):
        mark=int(input("enter marks of subject:"))
        stumark.append(mark)
    marks.append(stumark)
marks=nm.array(marks)
for i in range(n):
    print(name[i],marks[i])
print(" "*25 + "Average Marks of Each Student")
for i in range(n):
    avg=nm.mean(marks[i])
    print(name[i],avg)
print(" "*25 + "percentage of Each Student")
for i in range(n):
    per=nm.mean(marks[i])/100*100
    print(name[i],per)