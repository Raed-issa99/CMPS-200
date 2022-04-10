class BankAccount:
    def __init__(self,bal):
        self.bal=bal

    def withdraw(self,amount):
        '''takes an amount as input and withdraws it from the balance'''
        if self.bal>=amount:
            self.bal-=amount
        else:
            raise ValueError('Overdraft')

    def deposit(self,amount):
        ''' takes an amount as input and adds it to the balance '''
        if amount>0:
            self.bal+=amount
        else:
            raise ValueError('Negative deposit')

    def balance(self,amount):
        '''returns the balance on the account '''
        if amount<0:
            raise ValueError("Illegal amount")
        else:
            self.bal=amount

    def __eq__(self,other):
        '''returns a boolean indicating if two bank accounts have
        the same amount (this is the method that the equality operator == calls) '''
        return self.bal==other.bal

    def __str__(self):
        ''' returns a string representation of the object (will be used by print())'''
        return str(self.bal)


x= BankAccount(500)
x.withdraw(600)
x.deposit(100)
print(x.bal)
x.balance(-600)
