from math import modf, degrees, radians, trunc
 
y = degrees(float(input("y = ")))
print(y)
amin, hours = modf(y/30)
minutes = amin*60
print(f"Угол минутной стрелки: = {minutes*6} градусов")
print(f"{trunc(hours)} ч {trunc(minutes)} мин")
