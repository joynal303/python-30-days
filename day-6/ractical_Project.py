
"""name = name.strip()
name = name.title()

country = country.upper()

skill = skill.capitalize()

print(f"My name is {name}. My country name is {country}. My skill is {skill}.")"""

"""#String Project : Text Analyzer।
text = input("Enter a sentence: ")

words = text.split()

print("Total characters:", len(text))
print("Total words:", len(words))

word = input("Enter a word to search: ")

print("Word frequency:", words.count(word))"""

#Step 4 — Word আছে কি না যাচাই
text = input("Enter a sentence: ")

words = text.split()

word = input("Enter a word to search: ")

if word in words:
    print("Word Found")
else:
    print("Word Not Found")