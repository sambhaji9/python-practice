# program to display the student percentage in school exam

grade = "Fail class"
maths = int(input("Enter marks in maths: "))
science = int(input("Enter marks in science: "))
english = int(input("Enter marks in english: "))
hindi = int(input("Enter marks in hindi: "))
marathi = int(input("Enter marks in marathi: "))
total = (maths + science + hindi + marathi + english)
percentage = (total/5)
fail = False

if maths < 40 or science < 40 or english < 40 or hindi < 40 or marathi < 40:
    fail = True

if percentage >= 70 and not fail:
    grade = "Distinction"
elif percentage >= 60 and not fail:
    grade = "First class"
elif percentage >= 50 and not fail:
    grade = "Second class"
elif percentage >= 40 and not fail:
    grade = "Pass class"
else:
    grade = "Fail class"

print("\n\nName: Sambhaji Mane")
print("Roll no: 26")
print("=========================")
print("Maths: ", maths)
print("Science: ", science)
print("English: ", english)
print("Hindi:", hindi)
print("Marathi: ", marathi)
print("=========================")
print("Total: ", total)
print("Percentage: ", percentage)
print("Grade: ", grade)
