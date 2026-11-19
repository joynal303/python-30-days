birds = ["Pigeon", "Parrot", "Dove", "Eagle", "Crow"]

print(birds[0:3])
print(birds[1:4])
print(birds[:3])
print(birds[2:])

"""Python-এ List Slicing-এর নিয়ম:
start = কোন Index থেকে শুরু হবে।



end = কোন Index-এর আগ পর্যন্ত যাবে।



end Index-এর আইটেমটি অন্তর্ভুক্ত হবে না।
"""


animals = ["Cat", "Dog", "Cow", "Goat", "Sheep", "Horse", "Tiger"]
print(animals[:3])
print(animals[4:])
print(animals[1:4])
print(animals.reverse())#এখানে মূল List-টাই স্থায়ীভাবে উল্টো হয়ে যায়।

print(animals[::-1])#এখানে মূল List পরিবর্তন হয় না। শুধু উল্টো ক্রমের একটি নতুন List পাওয়া যায়।