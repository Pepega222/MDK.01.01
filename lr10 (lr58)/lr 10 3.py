class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state
class Singleton(Borg):
    def __init__(self, arg):
        Borg.__init__(self)
        self.val = arg
    def __str__(self):
        return self.val
if __name__ == '__main__':
    x = Singleton('one')
    print(x)
    y = Singleton('two')
    print(y)
    z = Singleton('three')
    print(z)
    print(x)
    print(y)
