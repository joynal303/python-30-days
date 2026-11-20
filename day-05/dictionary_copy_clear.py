pet = {
    "name": "Pigeon",
    "age": 2,
    "foods": ["Rice", "Corn", "Wheat"]
}

new_pet = pet.copy()#pet-এর একটি আলাদা copy তৈরি করা হয়েছে, যার নাম new_pet।

new_pet["age"] = 5

print(pet)
print(new_pet)
#এখন clear() শেখা যাক। এটা Dictionary-এর সব data মুছে দেয়।
new_pet.clear()
print(new_pet)
print(pet)