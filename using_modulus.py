#using modulus to  print even and odd numbers
#even number
number = int(input("Please enter an even number: "))
if (number%2 == 0):#mean that an even number divide by 2 return 0, so it qualifies to be an even number
    print(number, "is an even number")
else:
    print(number, "is not an even number")

#odd number
number = int(input("Please enter an odd number: "))
if (number%3 == 0):
    print(number, "is an odd number")
else:
    print(number, "is not an odd number")

#divisibility test of 5
number = int(input("Please enter a multiple of 5 number: "))
if (number%5 == 0):
    print(number, "is divisible by 5")
else:
    print(number, "is not divisible by 5")