class Cat():    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title()+ " is now sitting.")
    def roll_over(self):
        print(self.name.title()+ " rolled over!")
    def eat(self):
        print(self.name.title()+ " is eating")
my_cat = Cat('lariska', 3)
print("My cat's name is " + my_cat.name.title() + ".")
print("My cat is " + str(my_cat.age) + " years old.")
my_cat.sit()
my_cat.roll_over()
my_cat.eat()

