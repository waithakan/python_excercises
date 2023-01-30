#selecting all items in a list
country = ["kenya", "Somalia", "Uganda", "Tanzania"]
country = input("Enter an Eastern African country: ").lower()
age = int(input("Enter your age: "))
if (age >= 18 and country is country):
    print("You can vote ")
else:
    print("You can not vote")