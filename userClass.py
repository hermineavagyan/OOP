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

#creating 3 users
user1 = User("Adrien", "adrien@yahoo.com")
user2 = User("Hermine", "hermine@codingdojo.com")
user3 = User("Bob", "bob@codingdojo.com")

#first user makes 3 deposits and 1 withdrawals
user1.make_deposit(400)
user1.make_deposit(400)
user1.make_deposit(600)
user1.make_withdrawal(200)

#second user makes 2 deposits and 2 withdrawals
user2.make_deposit(500)
user2.make_deposit(800)
user2.make_withdrawal(300)
user2.make_withdrawal(100)

#third user makes 1 deposits and 3 withdrawals
user3.make_deposit(800)
user3.make_withdrawal(300)
user3.make_withdrawal(500)
user3.make_withdrawal(150)

#call display_user_balance method to display the users' account balances
user1.display_user_balance()
user2.display_user_balance()
user3.display_user_balance()

user1.transfer_money(user3,200)
print()
print("After calling transfer money method the account balances of the first and the third user")
# after calling transfer money method the account balances of the first and the third user
user1.display_user_balance()
user3.display_user_balance()


