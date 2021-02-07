
x = int(input("Enter Your score : "))
if (x >= 80) and (x < 100):
    print("Your score is :", x,)
    print("Grade: A")
elif (x >= 75) and (x <= 79):
    print("Your score is :", x,)
    print("Grade: B+")
elif (x >= 70) and (x <= 74):
    print("Your score is :", x,)
    print("Grade: B")
elif (x >= 65) and (x <= 69):
    print("Your score is :", x,)
    print("Grade: C+")
elif (x >= 60) and (x <= 64):
    print("Your score is :", x,)
    print("Grade: C")
elif (x >= 55) and (x <= 59):
    print("Your score is :", x,)
    print("Grade: D+")
elif (x >= 50) and (x <= 54):
    print("Your score is :", x,)
    print("Grade: D")
else:
    print("Your score is :", x,)
    print("Grade: F")
