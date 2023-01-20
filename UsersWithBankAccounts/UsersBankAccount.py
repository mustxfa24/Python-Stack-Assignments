# class User:
#     def example_method(self):
#         self.account.deposit(100)		# we can call the BankAccount instance's methods
#     	print(self.account.balance)		# or access its attributes

# class User:
#     # other methods
#     def make_deposit(self, amount):
#     	self.account_balance += amount	# hmmm...the User class doesn't have an account_balance attribute anymore

class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
        else:
            print('Insufficient Funds: Charging a $5 Fee.')
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_intrest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self


class User:
    def __init__(self,name):
        self.name = name
        self.account =BankAccount(0.03, 1900)

    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, student Balance: {self.account.display_account_info()}")
        return self

mustafa = User('Mustafa')
mustafa.display_user_balance()
mustafa.display_user_balance()
mustafa.make_withdrawal(200)
mustafa.display_user_balance()