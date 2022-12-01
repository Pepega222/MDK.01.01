from abc import ABC
from abc import abstractmethod
class Transport(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def get_info(self):
        pass

class Boat(Transport):
    def start(self):
        print('Корабль поплыл')
    def stop(self):
        print('Корабль остановился')
    def get_info(self):
        print('Это корабль')

Boat1 = Boat()
Boat1.start()
Boat1.stop()
Boat1.get_info()