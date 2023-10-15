"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary, rate, hours, commissionType, commission, contractAmount):

        self.name = name
        self.salary = salary
        self.rate = rate
        self.commissionType = commissionType
        self.pay = 0

        if salary:
            self.hours = None
        else:
            self.hours = hours

        if commissionType is None:
            self.commission = None
            self.contractAmount = None
        else:
            if commissionType == 1:
                self.bonus = commission
                self.contractAmount = None
            elif commissionType == 2:
                self.commission = commission
                self.contracts = contractAmount



    def get_pay(self):
        if self.salary:
            self.pay += self.rate
        else:
            self.pay += self.rate * self.hours

        if self.commissionType == 1:
            self.pay += self.bonus
        elif self.commissionType == 2:
            self.pay += self.commission * self.contracts

        return self.pay

    def __str__(self):
        if self.salary:
            if self.commissionType == 1:
                return self.name + "works on a monthly salary of "+self.rate+" and receives a bonus commission of"+self.bonus+". Their total pay is "+self.pay+"."
            elif self.commissionType == 2:
                return self.name + "works on a monthly salary of "+self.rate+" and receives a commission for "+self.contracts+" contract(s) at "+self.commission+"/contract. Their total pay is "+self.pay+"."
            else:
                return self.name + "works on a monthly salary of "+self.rate+". Their total pay is "+self.pay+"."
        else:
            if self.commissionType == 1:
                return self.name + "works on a contract salary of "+self.hours+" hours at "+self.rate+"/hour and receives a bonus commission of"+self.bonus+". Their total pay is "+self.pay+"."
            elif self.commissionType == 2:
                return self.name + "works on a contract salary of "+self.hours+" hours at "+self.rate+"/hour and receives a commission for "+self.contracts+" contract(s) at "+self.commission+"/contract. Their total pay is "+self.pay+"."
            else:
                return self.name + "works on a contract salary of "+self.hours+" hours at "+self.rate+"/hour. Their total pay is "+self.pay+"."




# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', True, 4000, None, None, None, None)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', False, 25, 100, None, None, None)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', True, 3000, None, 2, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', False, 25, 150, 2, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', True, 2000, None, 1, 1500, None)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', False, 30, 120, 1, 600, None)
