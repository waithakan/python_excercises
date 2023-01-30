#program to check if voter is qualifies to vote
nationality = input("Please state your Nationality: ").lower()
age = int(input("Enter your age: "))
if (age >= 18 and nationality == "kenyan"):
    print("You can vote")
else:
    print("you are not eligible to vote")