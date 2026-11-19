#১. union()
#২. intersection()


set_a = {"Pigeon", "Parrot", "Dove"}
set_b = {"Dove", "Eagle", "Crow"}

print(set_a.union(set_b))
print(set_a.intersection(set_b))

"""union() → দুই Set-এর সব Unique Item।
intersection() → দুই Set-এ থাকা Common Item।"""

#৩. difference()
print(set_a.difference(set_b))

#৪. symmetric_difference()
"""দুই Set-এর মধ্যে যেসব Item শুধু একটিতে আছে, সেগুলো বের করে। Common Item বাদ যায়।"""
print(set_a.symmetric_difference(set_b))

#chalange
set_a = {10, 20, 30, 40}
set_b = {30, 40, 50, 60}

print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a.difference(set_b))
print(set_a.symmetric_difference(set_b))


"""সহজে মনে রাখার নিয়ম
Operation	ফলাফল
union()	সব Unique Item
intersection()	Common Item
difference()	প্রথম Set-এ আছে, দ্বিতীয়টিতে নেই
symmetric_difference()	Common বাদে বাকি সব"""

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.difference(B))
print(B.difference(A))
#difference()-এর ক্ষেত্রে কোন Set আগে লিখছ, সেটি খুব গুরুত্বপূর্ণ।
