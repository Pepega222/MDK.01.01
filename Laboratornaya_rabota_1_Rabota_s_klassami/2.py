class year():    
    def __init__(self,number):
        self.number = number
    def visokosniy(self):
        if (int(self.number)%4==0 and int(self.number)%100!=0) or int(self.number)%400 == 0:
            print(str(self.number) +' год високосный')
        else:
            print(str(self.number) +' год не високосный')
Year = year(2012)
Year.visokosniy()
