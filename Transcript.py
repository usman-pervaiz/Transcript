from prettytable import PrettyTable
diff_num = int(input("Enter Differential Equation Number: "))
ISE_num = int(input("Enter Introduction to software Engineering Number: "))
ECO_num = int(input("Enter Economics Number: "))
Micro_num = int(input("Enter Microprocessor & Assembly Language Number: "))
DCOM_num = int(input("Enter Data Communication & Computer Networks Number: "))

lst = [diff_num,ISE_num,ECO_num,Micro_num,DCOM_num]
name = ["Differential Equation", "Introduction to software Engineering","Economics",
        "Microprocessor & Assembly Language","Data Communication & Computer Networks"]
marks = []
final = []
cgpa = 0

for i in range(len(lst)):
    marks = []
    if lst[i] >= 93:
        grade = "A+"
        gpa = 4
        cgpa += 4
    elif lst[i] >= 85:
        grade = "A"
        gpa = 4
        cgpa += 4
    elif lst[i] >= 81:
        grade = "A-"
        gpa =3.7
        cgpa += 3.7
    elif lst[i] >= 76:
        grade = "B+"
        gpa = 3.4
        cgpa += 3.4
    elif lst[i] >= 70:
        grade = "B"
        gpa = 3
        cgpa += 3
    elif lst[i] >= 67:
        grade = "B-"
        gpa = 2.7
        cgpa += 2.7
    elif lst[i] >= 63:
        grade = "C+"
        gpa = 2.4
        cgpa += 2.4
    elif lst[i] >= 60:
        grade = "C"
        gpa = 2
        cgpa += 2
    elif lst[i] >= 57:
        grade = "C-"
        gpa = 1.7
        cgpa += 1.7
    elif lst[i] >= 53:
        grade = "D+"
        gpa = 1.4
    elif lst[i] >= 50:
        grade = "D"
        gpa = 1
        cgpa += 1
    elif lst[i] < 50:
        grade = "F"
        gpa = 0
        cgpa += 0
    marks.append(name[i])
    marks.append(grade)
    marks.append(gpa)
    final.append(marks)
    #print(name[i],"\t",grade,"\t",gpa)

CGPA = round(cgpa/5,2)
print("\n")
table1= PrettyTable()
table1.field_names = ["Total GPA"]
table1.add_row([CGPA])
print(table1)

table= PrettyTable()
table.field_names = ["Course","Grade","GPA"]
for i in final:
    table.add_row(i)
print(table)







#print(final)
#print(CGPA)
    
    
    
