#Encapsulation কী?
"""Encapsulation হলো Class-এর ভিতরে Data (Attributes) এবং Methods একসঙ্গে রাখা এবং প্রয়োজন অনুযায়ী Data-এর access নিয়ন্ত্রণ করা।
সহজভাবে বললে, কোনো object-এর গুরুত্বপূর্ণ তথ্য সরাসরি পরিবর্তন করা থেকে সুরক্ষিত রাখার একটি পদ্ধতি।"""

#১. Public Attribute: যে attribute বাইরে থেকেও সরাসরি access ও পরিবর্তন করা যায়।
"""class BankAccount:
    def __init__(self, balance):
        self.balance = balance

account1 = BankAccount(10000)

print(account1.balance)

account1.balance = 5000
print(account1.balance)"""
#এখানে balance একটি Public Attribute।

#২. Private Attribute
#Python-এ attribute-এর নামের শুরুতে Double Underscore (__) দিলে সেটিকে name-mangled করা হয়।
"""class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

account1 = BankAccount(10000)

print(account1.__balance)"""
"""এখানে সরাসরি account1.__balance access করলে AttributeError হবে।
কারণ Python এই attribute-টির নাম internally পরিবর্তন করে"""

#practice:
class BankAccount:
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
print(person1.name) #name Public, তাই বাইরে থেকেও access করা যাবে।
#self.__balance = balance, balance Private, তাই বাইরে থেকে সরাসরি access করা যাবে না।
#কিন্তু Class-এর নিজের method show_balance()-এর ভিতর থেকে access করা যাচ্ছে। এটাই Encapsulation-এর মূল ধারণার একটি অংশ।


