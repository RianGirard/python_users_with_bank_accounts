class User: 
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.accounts = [BankAccount(account_name="checking", int_rate=0.02, balance=0), BankAccount(account_name="savings", int_rate=0.04, balance=0)]

    def make_deposit(self, account_name, amount):       # make_deposits takes in an account name
        for i in self.accounts:                         # for i in the list of self.accounts
            if i.account_name == account_name:          # if i.account_name (from BankAccount object) == account_name input value
                i.deposit(amount)                       # then have record "i" call the "deposit" method and put that $$$ in the account 
        return self

    def make_withdrawal(self, account_name, amount):       
        for i in self.accounts:                         # same, see above
            if i.account_name == account_name:
                i.withdraw(amount)
        return self

    def display_user_balance(self, account_name):
        for i in self.accounts:                         # same, see above
            if i.account_name == account_name:
                print(i.account_name, i.display_account_info())
        return self

### NEW !!! 
    def create_account(self, account_name, balance):
        self.accounts.append(BankAccount(account_name=account_name, balance=balance))
        return self

    def show_balances(self):
        for i in self.accounts:
            print(i.account_name, i.int_rate, i.balance)
        print('\n', '*'*80)
        return self
### 

class BankAccount:
    def __init__(self, account_name, int_rate=0.02, balance=0):
        self.int_rate = int_rate
        self.account_name = account_name
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

guido.create_account("college fund", 0)
guido.show_balances()
guido.create_account("rainy day", 100)
guido.show_balances()