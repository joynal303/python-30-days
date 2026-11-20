"""এবার Dictionary-এর update() Method
একসাথে একাধিক Value পরিবর্তন বা নতুন Key যোগ করতে update() ব্যবহার করা যায়:"""
birds = {
    "name": "Pigeon",
    "color": "White",
    "age": 2
}
birds["age"]=3
birds["country"]="Spain"
print(birds)

birds.update({
    "color": "Black",
    "age": 4
})

print(birds)

#chalange
birds = {
    "name": "Pigeon",
    "color": "White",
    "age": 3
}

birds.update({
    "color": "Gray",
    "age": 5
    })

print(birds)