"""file = open("student.txt", "r")
data = file.read()
file.close()"""

#কিন্তু with open() ব্যবহার করলে আলাদাভাবে close() লিখতে হয় না।
with open("student.txt", "r") as file:
    data = file.read()
    print(data)

"""কাজ শেষে Python নিজে থেকেই ফাইল Close করে।
কোড ছোট ও পরিষ্কার হয়।
File Handling-এর জন্য এটি Recommended Practice।"""

with open("student.txt", "r") as file:
    data=file.read()
    print(data)