from datetime import datetime

_next = 0
def _next_number():
    global _next
    _next +=1


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
        self.__number = _next_number()
        self.__Boats = Boats
        self.__queue = []
    def __add__(self, value):
        self.__Boats += value
    def __call__(self, value):
        self.__Boats = value

    @property
    def number(self):
        return self.__number
    @property
    def Boats(self):
        return self.__Boats
    @Boats.setter
    def Boats(self, value):
        if not  isinstance(value, int):
            print('Boats is number!')
        else:
            self.__Boats = value
    @Boats.deleter
    def Boats(self):
        raise TypeError('Boats dont delete')
    
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
    def date(self):
        CheckingDate(date)
    
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


class InvalidBalanceError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return 'invalid Boats {0}'.format(self.value)

from datetime import date
class CheckingDate(object):
    def __init__(self):
        self.maxdate = date.today()
    def __get__(self, instance, cls):
        return instance._date
    def __set__(self, instance, value):
        if self.maxdate < value:
            instance._date = self.maxdate
        else:
            instance._date = value

ba = VMF(100)
ba(200)
print(ba)
