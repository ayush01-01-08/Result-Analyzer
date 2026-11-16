n = int(input("\nNumber of student: "))

total_percentage = 0
highest_percentage = 0
topper_student = ""

for i in range(1, n + 1):
    name = input("\nStudent name: ")
    physics = float(input("Physics marks: "))
    chemistry = float(input("Chemistry marks: "))
    maths = float(input("Maths marks: "))
    eco = float(input("Economics marks: "))
    python = float(input("Python marks: "))
    total_marks = physics + chemistry + maths + eco + python
    percentage = (total_marks / 500) * 100
    percentage = round(percentage, 2)
    total_percentage += percentage

    print("\nName: ", name)
    print("Total marks: ", total_marks)
    print("Percentage: ", percentage, "%",)
    if percentage >= 80:
        print("Grade: A+")
    elif percentage >= 60:
        print("Grade: A")
    elif percentage >= 45:
        print("Grade: B")
    elif percentage >= 33:
        print("Grade: C")
    else:
        print("Grade: D")

    if percentage > highest_percentage:
        highest_percentage = percentage
        topper_student = name

print("\n[Total students: ", n, "]")
print("\n[Class Average: ", round(total_percentage/n, 2), "%", "]")
print("\n[Toper Student: ", topper_student)
print("Highest percentage: ", highest_percentage, "%", "]")