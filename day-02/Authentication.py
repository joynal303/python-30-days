correct_password = "12345"
correct_username = "admin"

login_username = input("Enter username: ")
login_password = input("Enter password: ")

if login_username == correct_username and login_password == correct_password:
    print("Login Successful")
else:
    print("Wrong username or password!")
    