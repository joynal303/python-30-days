balance = 10000

withdraw_amount = int(input("Enter withdrawal amount: "))

if withdraw_amount > balance:
    print("Insufficient Balance")

elif withdraw_amount <= 0:
    print("Invalid Amount")

else:
    new_balance = balance - withdraw_amount
    print("Remaining Balance:", new_balance)
    