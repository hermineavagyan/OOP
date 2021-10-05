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
        return self

#decreases the user's balance by the amount specified
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

#prints the user's name and account balance to the terminal
    def display_user_balance(self):
        print(self.name, self.account_balance)
        return self

#decrease the user's balance by the amount and 
# add that amount to other other_user's balance
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

    
#prints greeting message togteher with the user name
    def greeting(self):
        print("Hello my name is", self.name)
        print("my email is ", self.email)
        return self
#creating 3 users
user1 = User("Adrien", "adrien@yahoo.com")
user2 = User("Hermine", "hermine@codingdojo.com")
user3 = User("Bob", "bob@codingdojo.com")

#chaning first user's behavior
user1.make_deposit(400).make_deposit(400).make_deposit(600).make_withdrawal(200)


#chaining the second user's activities
user2.make_deposit(500).make_deposit(800).make_withdrawal(300).make_withdrawal(300).make_withdrawal(100)


#chaining the third user's activities
user3.make_deposit(800).make_withdrawal(300).make_withdrawal(500).make_withdrawal(150)


#call display_user_balance method to display the users' account balances
print("the second code is running")
user1.display_user_balance()
user2.display_user_balance()
user3.display_user_balance()

user1.transfer_money(user3,200)
print()
print("After calling transfer money method the account balances of the first and the third user")
# after calling transfer money method the account balances of the first and the third user
user1.display_user_balance()
user3.display_user_balance()


