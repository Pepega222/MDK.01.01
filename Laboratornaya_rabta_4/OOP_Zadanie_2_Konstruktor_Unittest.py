_next = 0
def _next_number():
    global _next
    _next +=1

from datetime import datetime

class BankTransaction(object):
    def __init__(self,amount):
        self.when = datetime.today()
        self.amount = amount
    def __del__(self):
        with open('transactionVMF.txt', 'a') as f:
            f.write('when {0} : amount {1} \n'.format(self.when, self.amount))
            f.closed
import pickle
class PersistenceAccount(object):

    @staticmethod
    def serialize(account):
        with open('VMF_account.pkl', 'wb') as f:
            pickle.dump(account, f)
        f.closed
    
    @staticmethod
    def deserialize():
        with open('VMF_account.pkl', 'rb') as f:
            account = pickle.load(f)
        f.closed
        return account

class VMF:
    def __init__(self, Boats = 0):
        self.number = _next_number()
        self.Boats = Boats
        self.queue = []
    def Pokypka(self, amount):
        self.Boats += amount
        self.queue.append(BankTransaction(amount))
    def Sell(self, amount):
        self.Boats -= amount
    def transfer_from(self, account, amount):
        account.Pokypka(amount)
        self.Sell(amount)
    def test_deposit(account):
        print(account)
        amount = int(input('enter amount to deposit on number {0}:'.format(account.number)))
        account.Pokypka(amount)
        print(account)
    def test_withdraw(account):
        print(account)
        amount = int(input('enter amount to sell on number {0}:'.format(account.number)))
        account.Sell(amount)
        print(account)
    def get_transaction(self):
        for i in range(len(self.queue)):
            item = self.queue.pop(0)
            print('when {0} : amount {1}'.format(item.when, item.amount))
    @classmethod
    def create_bank_account(cls, value):
        return cls(value)
    def __str__(self):
        return 'number: {0}, Boats: {1}'.format(self.number, self.Boats)

class PersonalVMFAccount(VMF):
    def __init__(self, Boats = 0, name = None):
        VMF.__init__(self, Boats )
        self.name = name
    def __str__(self):
        return 'number: {0}, boats: {1}, name: {2}'.format(self.number,self.Boats, self.name)
    def interest(self, rate):
        self.Boats *= (1 + rate)

class OverdrawnBankAccount(VMF):
    def __init__(self, Boats = 0, overdrawn = -1000):
        super(OverdrawnBankAccount, self).__init__(Boats)
        self.overdrawn = overdrawn
    def __str__(self):
        return 'number: {0}, boats: {1},  overdrawn {2}'.format(self.number, self.Boats,  self.overdrawn)
    def Sell(self, amount):
        if self.Boats - amount > self.overdrawn:
            Boats -= amount

class One(object):
    def one(self):
        return 'one'
class Two(object):
    def two(self):
        return 'two'
class Three(One, Two):
    pass

t = Three()
print(t.one())
print(t.two())

oba = OverdrawnBankAccount(100)
VMF.test_deposit(oba)
VMF.test_withdraw(oba)

person = PersonalVMFAccount(100, 'Alex')
person.interest(.3)
print(person)

ba = VMF.create_bank_account(50)
print(ba) 

ba1 = VMF(100)
ba2 = VMF(100)  
print(ba1)
print(ba2)
ba1.transfer_from(ba2, 50)
print(ba1)
print(ba2)

ba = VMF(100)
PersistenceAccount.serialize(ba)
print(PersistenceAccount.deserialize())

ba = VMF()
VMF.test_deposit(ba)
VMF.test_withdraw(ba)
ba.get_transaction()


import unittest
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = VMF(5)
    def test_account_Pokypka(self):
        test_Boats = 10
        self.account.Pokypka(5)
        self.assertEqual(self.account.Boats, test_Boats)
    def test_account_Sell(self):
        test_Boats = 0
        self.account.Sell(5)
        self.assertEqual(self.account.Boats, test_Boats)
if __name__ == '__main__':
    unittest.main()
