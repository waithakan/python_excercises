#calculating discount if amount spent is equal or greater than 1000
amount = int(input("Enter amount spent: "))
discount = amount * 0.05
if (amount >= 1000):
    print("your discount is ", discount)
    print("pay ", amount - discount)
else:
    print("you have no discount")