# GradeA = 100>=80
# GradeB = 79>=65
# GradeC = 64>=50
# GradeD = 49>=40
# GradeF = 39>=0

marks = int(input("Enter marks:"))

if marks <=100 and marks >=80:
    print("Grade A")

elif marks <=79 and marks >=65:
    print("Grade B")

elif marks <=64 and marks >=50:
    print("Grade C")

elif marks <=49 and marks >=40:
    print("Grade D")

elif marks <=39 and marks >=0:
    print("Grade F")

else:
    print("Undefined")