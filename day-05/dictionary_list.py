pet = {
    "name": "Pigeon",
    "age": 2,
    "foods": ["Rice", "Corn", "Wheat"]
}

print(pet["name"])
print(pet["foods"])
print(pet["foods"][1])

print(pet["foods"][2])
pet["foods"].append("Millet")#dictionary["key"].append("new item")
print(pet)

#chalange
pet = {
    "name": "Pigeon",
    "age": 2,
    "foods": ["Rice", "Corn", "Wheat"]
}

print(pet["foods"][1])
pet["foods"].append("Millet")
pet["age"] = 3
print(pet)

pet.update({
    "color": "White"

})

print(pet)