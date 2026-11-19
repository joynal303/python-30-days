"""pop() দিয়ে List থেকে item মুছে ফেলা যায়। তবে এটি মুছে ফেলা item-টিকেও return করে।"""

birds=["Pigeon", "Parrot", "Dove", "Eagle"]
removed_bird = birds.pop()

print("Removed:", removed_bird)
print("Remaining:", birds)


"""pop() → index না দিলে শেষের item মুছে দেয়।



pop(1) → index 1-এর item মুছে দেয়।



remove("Eagle") → নাম দিয়ে item মুছে দেয়।"""


birds=["Pigeon", "Parrot", "Dove", "Eagle"]
removed_bird = birds.pop(2)

print("Removed:", removed_bird)
print("Remaining:", birds)