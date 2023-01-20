class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
        else:
            print('Insuffician funds: Charging a $5 fee.')
            self.balance -= 5
        return self

    def display_account_info(self):
        print (f'Balance: ${self.balance}')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
checking = BankAccount(.02,500)
savings = BankAccount(.07,700)

checking.deposit(52000).deposit(5000).deposit(5000).withdraw(2000).yield_interest().display_account_info()

savings.deposit(6000).deposit(60000).withdraw(6000).withdraw(590).withdraw(2500).yield_interest().display_account_info()