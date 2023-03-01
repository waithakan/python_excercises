# create a class called bank account with attributes like account_number, balance, date_of_opening, 
# customer_name and methods like deposit, withdraw, check_balance and customer details
# i) deposit method should return amount deposited
# ii) withdarw method return insufficient balance if account balance is less than amount to be withdrwan else it
#     should return amount that is withdrwan
# iii) check_balance method should print the current balance
# iv) The customer details method should print customer_name, account_number, date of account opennings, and balance
customer_name = input("Enter your name = ")
account_number = int(input("Enter account number = "))
balance = float(input("Enter account balance = "))
withdraw = int(input("enter amount to withdraw: "))
date_of_opening = int(input("state your opening date = "))


class BankAccount: 
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit (self):
        return(3000)
    def withdraw (self):
        if (self.balance < withdraw):
            print("Insufficient funds")
        else:
            
           print("remainig amount = ",self.balance-withdraw)
        
    def check_balance (self):
        print("Current Balance: ", self.balance-withdraw)

    def customer_details (self):
        print("Customer Name: ", self.customer_name)
        print("Account Number: ", self.account_number)
        print("Date of Opening: ", self.date_of_opening)
        # print("Current Balance: ", self.balance- withdraw)

b = BankAccount(account_number, balance,date_of_opening, customer_name)
b.deposit()
b.withdraw()
b.check_balance()
b.customer_details()
