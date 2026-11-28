"""class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, deposit):
        self.__balance = self.__balance + deposit

    def show_balance(self):
        print(f"{self.name} balance is: {self.__balance}")



person1 = BankAccount("Abedin",200000 )
person1.deposit(50000)
person1.show_balance()
print(person1.name)"""

#1. Getter কী?
"""Private data সরাসরি বাইরে থেকে access না করে একটি method-এর মাধ্যমে data দেখার পদ্ধতিকে Getter বলা হয়।"""
# self.__balance, এটা private। তাই বাইরে থেকে:
# print(person1.__balance), করা যায় না।
# এর পরিবর্তে আমরা method বানাতে পারি:
"""def get_balance(self):
    return self.__balance
print(person1.get_balance())"""

# 2. Setter কী?
# Private data নতুন value দিয়ে update করার জন্য Setter ব্যবহার করা হয়।
"""def set_balance(self, new_balance):
    self.__balance = new_balance
person1.set_balance(300000)"""

"""Private Data
    ↓
Getter → Data দেখা
    ↓
Setter → Data পরিবর্তন"""

#practice
class BankAccount:
    def __init__(self, name, balance) -> None:
        self.name = name
        self.__balance = balance

#Getter
def get_balance(self):
    return self.__balance

# Setter
def set_balance(self, new_balance):
    self.__balance = new_balance

person1 = BankAccount("Abedin", 200000)

# Getter দিয়ে balance দেখা
print("The Current Balance:",  person1.get_balance())

# Setter দিয়ে balance পরিবর্তন
person1.set_balance(300000)

# আবার Getter দিয়ে নতুন balance দেখা
print("Updated Balance:", person1.get_balance())