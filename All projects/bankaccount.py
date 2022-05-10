class BankAccount:
    '''constructs a Bank Account and puts n money in it'''
    def __init__(self, n = 0):
        self.cbalance = n
    ''' withdraws a specific amount from the Bank account'''
    def withdraw(self,amount):
        self.cbalance -= amount
    '''deposits a specific amount in the Bank account'''
    def deposit(self,amount):
        self.cbalance += amount
    '''returns the balance in the account'''
    def balance(self):
        return self.cbalance
    '''returns a boolean that expresses if 2 accounts have the same balance'''
    def __eq__(self,other):
        return (self.cbalance == other.cbalance)
    '''str will return the string representation of the balance in an account'''
    def __str__(self):
        return str(self.cbalance)

x = BankAccount(700)
print(x.balance())
x.withdraw(70)
print(x.balance())
x.deposit(7)
print(x)
print(x == BankAccount(637))
