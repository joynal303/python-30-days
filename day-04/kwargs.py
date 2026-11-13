
"""এবার শিখব **kwargs।
- *args → একাধিক positional argument গ্রহণ করে (tuple)।
- **kwargs → একাধিক keyword argument গ্রহণ করে (dictionary)।"""


def student_info(**details):
    print(details)

student_info(name="Abedin", age=28, country="Bangladesh")


def emply_deails( **details_emp):
    for i in details_emp:
     print(i, details_emp[i])

emply_deails(name="Abedin", age=28, country="Bangladesh")