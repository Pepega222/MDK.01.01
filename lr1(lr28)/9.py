class House():   
    def __init__(self,adress, floor,rooms,square):
        self.adress = adress
        self.floor = floor
        self.rooms = rooms
        self.square = square
    def room(self,n):
        rooms1=[]
        if int(self.rooms) == n:
            rooms1.append(self.adress)
        print(rooms1)
    def roomFloor(self,r,f,f1):
        rooms2=[]
        if int(self.rooms) == r and f<= int(self.floor) <=f1:
            rooms2.append(self.adress)
        print(rooms2)
    def squares(self,sq):
        rooms3=[]
        if float(self.square) > sq:
            rooms3.append(self.adress)
        print(rooms3)
house1=House('pushkina',1,1,500)
print(house1.room(1), house1.roomFloor(1,1,2), house1.squares(400))
house1=House('lenina',1,1,2) 
print(house1.room(1), house1.roomFloor(1,1,2), house1.squares(400))
house1=House('voronina',1,1,2) 
print(house1.room(1), house1.roomFloor(1,1,2), house1.squares(400)) 