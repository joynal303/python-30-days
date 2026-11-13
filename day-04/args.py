#যেকোনো সংখ্যক value function-এ পাঠাতে

def add_numbers(*numbers):
    print(numbers)

add_numbers(10, 20, 30, 40)
#এখানে numbers একটি tuple হিসেবে সব arguments ধরে রাখে।

#"কতগুলো argument আসবে আমি আগে থেকে জানি না, সবগুলো গ্রহণ করো।"

def calculate_sum(*numbers):
    total = 0

    for i in numbers:
        total = total + i

    return total

result = calculate_sum(10, 20, 30)
print(result)

#গুরুত্বপূর্ণ: for i in numbers মানে tuple-এর প্রতিটি value একে একে i-তে আসবে।

