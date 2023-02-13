
winning_number = 89
number = int(input("Guess a number: "))
if (number == winning_number):
    print("YOU WIN!!!")
else:
    if(number < winning_number):
        print("Thats too low!!")
    else:
        print("Thats too high!!")