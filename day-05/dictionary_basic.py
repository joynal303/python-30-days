 
"""বার Python-এর চতুর্থ Data Structure শিখব।

Dictionary-তে তথ্য Key: Value আকারে রাখা হয়।S"""

student = {
    "name": "Abedin",
    "age": 28,
    "country": "Bangladesh"
}

print(student["name"])
print(student["age"]) 

"""name, age, country হলো Key।

"Abedin", 28, "Bangladesh" হলো Value।"""

#Dictionary-তে তথ্য থাকে Key : Value আকারে।
student = {
    "name": "Abedin",
    "age": 28,
    "country": "Bangladesh"
}

print(student)

#২. Dictionary থেকে Value বের করা
#Key ব্যবহার করে Value বের করি:

print(student["name"])
print(student["age"])
print(student["country"])
#List-এ আমরা সাধারণত Index ব্যবহার করি:,birds[0]
#কিন্তু Dictionary-তে Key ব্যবহার করি:,student["name"]

#chalange
bird={
    "name": "pigeon",
    "color": "White",
    "age": 2
}
print(bird["name"])
print(bird["color"])
print(bird["age"])
print(bird)


#Dictionary-তে Value পরিবর্তন করা
bird["color"]="black"
print(bird)

#Dictionary-তে নতুন Key-Value যোগ করা
bird["country"] = "Bangladesh"
print(bird)


#Challenge

birds = {
    "name": "Pigeon",
    "color": "White",
    "age": 2
}
birds["age"]=3
birds["country"]="Spain"
print(birds)