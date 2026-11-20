
# Day 06: Text Analyzer Project

text = input("Enter a sentence: ")

# Character Count
print("Total characters:", len(text))

# Word Count
words = text.split()
print("Total words:", len(words))

# Search Word
word = input("Enter a word to search: ")

# Word Frequency
frequency = words.count(word)
print("Word frequency:", frequency)

# Check Word
if word in words:
    print("Word Found")
else:
    print("Word Not Found")
