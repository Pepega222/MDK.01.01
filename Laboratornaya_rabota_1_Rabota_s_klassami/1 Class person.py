class person():
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
    def calc_bmi(self):
        print("Индекс массы тела: ", self.weight/(self.height**2))
BMI= person(60,180)
BMI.calc_bmi()
BMI = person(100,150)
BMI.calc_bmi()
BMI = person(80,190)
BMI.calc_bmi()