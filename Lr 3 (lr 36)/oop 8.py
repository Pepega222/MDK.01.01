from cmath import log
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


class Personal(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name 

class PersonalVMFAccount(VMF):
    def __init__(self, Boats = 0, first_name = None, last_name = None):
        super(PersonalVMFAccount,self).__init__(Boats)
        self.personal = Personal(first_name, last_name)
    def __str__(self):
        return 'number: {0}, boats: {1}, first_name: {2}, last_name: {3}'.format(self.number,self.Boats, self.personal.first_name, self.personal.last_name )
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


def log(func):
    def wrapper(*args, **kwargs):
        print('call func {0}'.format(func.__name__), args, kwargs)
        func(*args, **kwargs)
    return wrapper

class Log(object):
    def __init__(self, func):
        self.func = func
        print('call func {0}'.format(func.__name__))
    def __call__(self, *args, **kwargs):
        print('args {0}'.format(args))
        print('kwargs {0}'.format(kwargs))

class BankDatabase(object):
    def __init__(self):
        self.filename = 'bank.pkl'
        self.database = {}
        self.index = 0
        try:
            self.open_database()
        except:
            self.save_database()
    number = property(lambda self: self.database[self.index].number)
    Boats = property(lambda self: self.database[self.index].Boats)
    def __iter__(self):
        for item in self.database:
            yield self.database[item]
    def next(self):
        if self.index == len(self.database):
            raise StopIteration
        self.index = self.index + 1
        return self.database[self.index]
    def prev(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.database[self.index]
    def open_database(self):
        with open(self.filename, 'rb') as f:
            self.database = pickle.load(f)
        f.closed
    def save_database(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.database, f)
        f.closed
    def add_account(self, Boats):
        ba = VMF(Boats)
        if ba.number in self.database:
            ba.number = len(self.database) + 1
        self.database[ba.number] = ba
        self.save_database()
    def get_account_by_number(self, number):
        if number not in self.database:
            return None
        return self.database[number]
    def delete_account(self, number):
        del self.database[number]
        self.save_database()
    def change_Boats(self, number, Boats):
        account = self.get_account_by_number(number)
        if not account:
            raise ValueError('value does not exist')
        account.Boats = Boats
        self.save_database()

class BankTerm(object):
    def __init__(self):
        self.bank_database = BankDatabase()
    def printDB(self):
        for account in self.bank_database:
            print('account number {0} Boats {1}'.format(account.number, account.Boats))
    def run(self):
        choice = 0
        choices = {
            1 : lambda : self.printDB(),
            2 : lambda : self.bank_database.add_account(int(input('enter Boats'))),
            3 : lambda : self.bank_database.delete_account(int(input('enter number'))),
            4 : lambda : self.bank_database.change_Boats(int(input('enter_number')), int(input('enter Boats')))
        }
        while (choice != 5):
            print()
            print('1. print database')
            print('2. add acount')
            print('3. delete account')
            print('4. change Boats')
            print('5. EXIT')
            print('choose:')
            choice = int(input())
            if choice in choices:
                choices[choice]()
if __name__ == '__main__':
 BankTerm().run()
