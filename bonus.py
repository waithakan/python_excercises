#using elif statment in python
period = int(input("Eneter number of years worked: "))
salary = int(input("Enter your monthly salary: "))
if (period  >  10):
    bonus = salary * 0.1
    print("Your bonus of 10% is", bonus)
    print("Your net salary is ",bonus + salary )
elif (period  >=  6 and period <= 10):
    bonus = salary * 0.08
    print("Your bonus of 8% is", bonus)
    print("Your net salary is ",bonus + salary  )
else: 
    bonus = salary * 0.05
    print("Your bonus of 5% is", bonus)
    print("Your net salary is ", bonus + salary )