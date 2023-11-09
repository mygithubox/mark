RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"

B = "\033[1m"


mark = input( RED + B + "What is youre mark:")
mark = int(mark)


if mark >=80:
    print(GREEN + B +'Grade:A+ \nGrade Point:4.00 \n Very Good 🥰🥰')
elif mark >= 70:
    print(GREEN +B +'Grade:A- \nGrade Point:3.50 \n Nice 😊😊')
elif mark >= 65:
    print(GREEN +B +'Grade:B+ \nGrade Point:3.25 \n Nice Try 🤔🤔')
elif mark >= 55:
    print(GREEN +B +'Grade:B- \nGrade Point:2.75 \n Bettar 😕😕')
elif mark >= 50:
    print(GREEN +B +'Grade:C+ \nGrade Point:2.50 \n Not Bed 🙁🙁')
elif mark >= 45:
    print(GREEN +B +'Grade:C \nGrade Point:2.25 \n Bed 😪😪')
elif mark >= 40:
    print(GREEN +B +'Grade:D \nGrade Point:2.00 \n Very Bed 😨🥶')
else:
    print(GREEN +B +'Grade:F \nGrade Point:00 \n I Didn`t Expect It 😭😭')
