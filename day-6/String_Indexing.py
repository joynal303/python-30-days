#List-এর মতো String-এর প্রতিটি Character-এর একটি Index থাকে।

#Lesson 02: String Indexing
name = "ABEDIN"

""" A   B   E   D   I   N
    0   1   2   3   4   5
    
OR

    A   B   E   D   I   N
    -6 -5   -4  -3  -2  -1
"""

name = "ABEDIN"

print(name[0])   # A
print(name[2])   # E
print(name[-1])  # N
print(name[-2])  # I

#Lesson 03: String Slicing
#একটি String থেকে নির্দিষ্ট অংশ বের করাকে Slicing বলে।
name = "ABEDIN"

print(name[0:3])  # ABE name[0:3] মানে Index 0 থেকে শুরু, কিন্তু Index 3 অন্তর্ভুক্ত হবে না।
print(name[1:4])  # BED
print(name[:3])   # ABE
print(name[2:])   # EDIN

#Practice Challenge 01

name = "PYTHON"

print(name[0])
print(name[3])
print(name[-1])
print(name[1:4])
print(name[:3])
print(name[2:])
