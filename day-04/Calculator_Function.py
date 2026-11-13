def calculator(a, b, operation):

    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b

    elif operation == "div":
        if b==0:
            return "Cannot divide by zero"
        else:
            return a / b  
    else:
        return "Invalid Operation" 



addition_result=calculator(20, 10, "add")
subtraction_result=calculator(20, 10, "sub")
multiplication_result=calculator(20, 10, "mul")
zero_ifnity=calculator(20, 0, "div")	
power=calculator(20, 10, "power")
print(addition_result)
print(subtraction_result)
print(multiplication_result)
print(zero_ifnity)
print(power)

