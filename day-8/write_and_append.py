""""w"	আগের লেখা মুছে নতুন করে লেখে
"a"	আগের লেখা রেখে শেষে নতুন তথ্য যোগ করে"""

"""with open("student.txt", "a") as file:
    file.write("\nCourse: Python Programming")"""
#এটি আগের তথ্য মুছে ফেলবে না। শেষে নতুন লাইন যোগ করবে।

"""with open("student.txt", "a") as file:
    file.write("\nUniversity: Private University")
    file.write("\nGoal: AI Engineer")
with open("student.txt", "r") as file:
    data = file.read()
    print(data)"""

#Challenge 07
"""with open("student.txt", "a") as file:
    file.write(" \nHobby: Pigeon Breeding")

with open("student.txt", "r") as file:
    data= file.read()
    print(data)
"""

#Challenge 08: Student Information Update


with open("student_info.txt", "w") as file:
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    country = input("Enter your country: ")
    skill = input("Enter your skill: ")
    goal = input("Enter your goal: ")

    file.write("Name: " + name + "\n")
    file.write("Age: " + age + "\n")
    file.write("Country: " + country + "\n")
    file.write("Skill: " + skill + "\n")
    file.write("Goal: " + goal + "\n")

with open("student_info.txt", "r") as file:
    data = file.read()
    print(data)