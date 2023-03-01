#program to calculate compound interest 
import math
def compound_interest(principle, rate, time):
   amount = principle * (math.pow((1+(rate/100)),time))
   print("compound amount: ", amount)
   compound_interest2 = amount - principle
   return compound_interest2
principle=float(input("Enter principle amount: "))
rate=float(input("Enter interest rate: "))
time=float(input("Enter time: "))
print("Compound interest: " , compound_interest(principle, rate, time))