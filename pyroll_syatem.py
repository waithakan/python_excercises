#using class Employee to create a payroll systemgit
class Employee:
    def __init__(self, name, hourly_rate):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = 0

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

    def __str__(self):
        return f"{self.name} earned {self.calculate_pay():.2f} dollars"

class PayrollSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_payroll(self):
        print("Payroll Report")
        print("==============")
        total_payroll = 0
        for employee in self.employees:
            employee_pay = employee.calculate_pay()
            total_payroll += employee_pay
            print(f"{employee.name}: {employee_pay:.2f} dollars")
        print("==============")
        print(f"Total Payroll: {total_payroll:.2f} dollars")
