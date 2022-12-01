from typing import NamedTuple

class VMF_(NamedTuple):
    men: float
    boats: float

def VMF() -> VMF_:
    return VMF_(1000,20)

coordinates = VMF()
print(f"Моряков:", coordinates.men) 
# print(f"Моряков:", coordinates.boatsRRR) #IDE подсветит
from typing import TypedDict

class VMF_(TypedDict):
    men: float
    boats: float

c = VMF_(men=1999, boats=25)
print(c["men"])
# ошибка print(c["mens"]) 

from dataclasses import dataclass

@dataclass
class _VMF:
    men: float
    boats: float
def VMF() -> _VMF:
    return _VMF(421,10)

print(VMF().men)
print(VMF().men12) #Покажет ошибку
