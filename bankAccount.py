class BankAccount:
    #class attribute

    all_accounts = []
#class constructor
    def __init__(self,interest_rate, balance = 0):
        self.interest_rate = (0.01) * interest_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
#increases the balance 
    def deposit(self, amount):
        self.balance += amount
        return self
# checks if there are sufficient finds and then decreases the amount of the balance
    def withdraw(self, amount):
        if BankAccount.check_funds(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient funds")
            self.balance -=5
        return self
#displays the account balance
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
# increases the account balance by the current balance * 
# the interest rate (as long as the balance is positive)
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.interest_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for i in cls.all_accounts:
            print(i.balance)
            i.display_account_info()
           
                

    @staticmethod
    def check_funds(balance, amount):
            if balance-amount < 0:
                return False
            else:
                return True

acct1 = BankAccount(20, 2000)
acct2 = BankAccount(10, 1000)

acct1.deposit(300).deposit(300).deposit(300).withdraw(300).yield_interest().display_account_info()
acct2.deposit(300).deposit(300).withdraw(300).withdraw(300).withdraw(300).withdraw(300).yield_interest().display_account_info()
print()
BankAccount.print_all_accounts()

