"""name হলো Parameter — Function তৈরির সময় যে Variable গ্রহণ করে।



"Abedin" হলো Argument — Function Call করার সময় যে Value পাঠানো হয়।"""


#Dynamic Greeting

def greet_user(name):
    print("Welcome to Python,", name)

greet_user("Abedin")
greet_user("Rahim")
greet_user("Karim")

 # multipole parameter
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

student_info("Abedin", 28)
student_info("Rahim", 25)