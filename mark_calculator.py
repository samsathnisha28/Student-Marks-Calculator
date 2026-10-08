# Student Marks Calculator

print("===== STUDENT MARKS CALCULATOR =====")

name = input("Enter student name: ")

m1 = float(input("Enter Tamil mark: "))
m2 = float(input("Enter English mark: "))
m3 = float(input("Enter Maths mark: "))
m4 = float(input("Enter Physics mark: "))
m5 = float(input("Enter Chemistry mark: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

if m1 >= 40 and m2 >= 40 and m3 >= 40 and m4 >= 40 and m5 >= 40:
    result = "PASS"
else:
    result = "FAIL"

print("\n===== MARKS REPORT =====")
print("Student Name :", name)
print("Tamil        :", m1)
print("English      :", m2)
print("Maths        :", m3)
print("Physics      :", m4)
print("Chemistry    :", m5)
print("Total Marks  :", total, "/ 500")
print("Average      :", average)
print("Grade        :", grade)
print("Result       :", result)