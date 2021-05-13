class User: 
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.accounts = [BankAccount(account_name="checking", int_rate=0.02, balance=0), BankAccount(account_name="savings", int_rate=0.04, balance=0)]

    def make_deposit(self, account_name, amount):       
        for i in self.accounts:
            if i.account_name == account_name:
                i.deposit(amount)
        return self

    def make_withdrawal(self, account_name, amount):       
        if account_name == "checking":
            self.accounts[0].withdraw(amount)
            return self
        if account_name == "savings":
            self.accounts[1].withdraw(amount)
            return self

    def display_user_balance(self, account_name):
        if account_name == "checking":
            print(account_name, self.accounts[0].display_account_info())
        if account_name == "savings":
            print(account_name, self.accounts[1].display_account_info())
        return self

### NEW !!! 
    def create_account(self, account_name):
        self.accounts.append(BankAccount(account_name=account_name))
        return self
### 

class BankAccount:
    def __init__(self, account_name, int_rate=0.02, balance=0):
        self.int_rate = int_rate
        self.account_name = account_name
        if balance == None:
            self.balance = 0
        else: 
            self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        return self.balance 

guido = User("Guido van Rossum", "guido@python.com")
guido.make_deposit("checking", 20)
guido.make_deposit("checking", 100)
guido.make_deposit("savings", 50)
guido.make_withdrawal("checking", 50)
guido.make_withdrawal("savings", 45)
guido.display_user_balance("checking")
guido.display_user_balance("savings")