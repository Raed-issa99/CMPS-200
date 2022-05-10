import random
from datetime import datetime


class BankAccount:
    def __init__(self, type, balance=0, date=datetime.now()):
        self.type = type
        self.balance = balance
        self.opendate = date

    def __str__(self):
        return ('Account opening date: %s \n Account Type: %s \n Current Balance: $ %d') % (
            self.opendate, self.type, self.balance)

    def balance(self):
        if self.balance < 0:
            raise ValueError('Illegal Balance')
        else:
           return self.balance

    def withdraw(self, value):
        if value > self.balance:
            raise ValueError('Overdraft')
        else:
            self.balance -= value

    def deposit(self, value):
        if value < 0:
            raise ValueError('Negative Deposit')
        else:
            self.balance += value

    def __lt__(self, other):
        return self.balance > other.balance


class CheckingAccount(BankAccount):
    def __init__(self, balance=0):
        super().__init__('Checking', balance)


class SavingsAccount(BankAccount):
    def __init__(self, rate, balance=0):
        super().__init__('Savings', balance)
        self.rate = rate

    def compute_interest(self, t):
        P = self.balance
        r = self.rate
        n = 12
        A = P * (1 + r / n)**(n * t)
        return A

    def earn_interest(self, t):
        self.balance += self.compute_interest(1 / 12)


s = SavingsAccount(0.5, 5000)
print('Account Opening Date: ' + str(s.opendate))
print('Account type: ' + str(s.type))
print('Current Balance = $ ' + '   ' + str(s.balance))
for i in range(1, 37):
    s.earn_interest(1 / 12)
    if i == 1:
        m = 'month'
    else:
        m = 'months'
    print('After %2d %s : $ %10.2f ' % (i, m, s.balance))


accounts = []
for i in range(10):
    balance = random.uniform(50, 5000)
    c = CheckingAccount(balance)

    accounts.append(c)
    print(accounts[i])

print('--------------------------------------------------------------------')
accounts.sort()
for i in range(10):
    print(accounts[i])
