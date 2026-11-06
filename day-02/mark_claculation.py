mark=int (input("Enter your mark:"))

if mark >=80 and mark <100:
    print("A+")
elif mark < 80 and mark >= 70:
    print("A")
elif mark < 70 and mark >= 60:
    print("A-")
elif mark < 60 and mark >= 50:
    print("B")
elif mark < 50 and mark >= 40:
    print("C")
elif mark < 40 and mark >= 0:
    print("Fail")
else:
    print("Worng Input")