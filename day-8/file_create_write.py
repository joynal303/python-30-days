"""এবার নিজে কোড লিখবে।

একটি student.txt ফাইল তৈরি করে সেখানে নিচের তথ্যগুলো সংরক্ষণ করো:
- Name: Abedin
- Age: 28
- Country: Bangladesh
- Skill: Python
শর্ত:
1. open() ব্যবহার করবে।
2. "w" mode ব্যবহার করবে।
3. write() দিয়ে চারটি তথ্য লিখবে।
4. close() দিয়ে ফাইল বন্ধ করবে।"""

file=open("student.txt", "w")
file.write("Name: Abedin \nAge: 28 \nCountry: Bangladesh \nSkill: Python")
file.close()