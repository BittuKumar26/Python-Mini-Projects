sub1 = float(input("Enter marks of Subject 1: "))
sub3 = float(input("Enter marks of Subject 3: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub4 = float(input("Enter marks of Subject 4: "))
sub5 = float(input("Enter marks of Subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
average = total / 5

if average >= 90:
    grade = "A++"
elif average >= 80:
    grade = "A+"
elif average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B+"
elif average >= 50:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "F"

print("Your grade is:", grade)
