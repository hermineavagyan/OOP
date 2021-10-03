class User:
#defining a class attriute
    bank_name = "First Dational Dojo"
#creating the class constructor
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

# increases the user's balance by the amount specified
    def make_deposit(self, amount):
        self.account_balance += amount

#decreases the user's balance by the amount specified
    def make_withdrawal(self, amount):
        self.account_balance -= amount

#prints the user's name and account balance to the terminal
    def display_user_balance(self):
        print(self.name, self.account_balance)

#decrease the user's balance by the amount and 
# add that amount to other other_user's balance
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
    
    

#prints greeting message togteher with the user name
    def greeting(self):
        print("Hello my name is", self.name)
        print("my email is ", self.email)


hermine = User("Hermine Avagyan", "hermine@codingdojo.com")
mila = User("Mila Kishmishyan", "mila@codingdojo.com")
bob = User("Bob Smith", "bobsmith@codingdojo.com")
bob.bank_name = "Bank of America"

mila.make_deposit(1000)
print("Mila's account balance is ", mila.account_balance)
print(bob.account_balance)
print()
mila.transfer_money(bob, 200)
print(mila.account_balance)
print(bob.account_balance)



# print("Bobs bank is", bob.bank_name)
# print("Mila's bank is", mila.bank_name)
# mila.make_deposit(1000)
# print("Mila has a balance of")
# mila.display_user_balance()
# print()
# mila.make_withdrawal(200)
# print("MIla has a balance of ")
# mila.display_user_balance()





