#remove() এবং discard()-এর মধ্যে একটি গুরুত্বপূর্ণ পার্থক্য আছে।
animals = {"Cat", "Dog", "Cow"}

animals.remove("Tiger")  # Error হবে
animals.discard("Tiger")  # Error হবে না

"""remove() vs discard() মনে রাখবে
Method	Item থাকলে	Item না থাকলে
remove()	মুছে দেয়	Error হয়
discard()	মুছে দেয়	Error হয় না"""

birds = {"Pigeon", "Parrot", "Dove"}

birds.discard("Eagle")

print(birds)

