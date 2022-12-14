class Obstacle:
    def action(self): pass
class Character:
    def interactWith(self, obstacle): pass
class Kitty(Character):
    def interactWith(self, obstacle):
        print('Kitty has encountered a',
        obstacle.action())
class KungFuGuy(Character):
    def interactWith(self, obstacle):
        print('KungFuGuy now battles a',
        obstacle.action())
class Puzzle(Obstacle):
    def action(self):
        print('Puzzle')
class NastyWeapon(Obstacle):
    def action(self):
        print('NastyWeapon')
class GameElementFactory:
    def makeCharacter(self): pass
    def makeObstacle(self): pass
class KittiesAndPuzzles(GameElementFactory):
    def makeCharacter(self): return Kitty()
    def makeObstacle(self): return Puzzle()
class KillAndDismember(GameElementFactory):
    def makeCharacter(self): return KungFuGuy()
    def makeObstacle(self): return NastyWeapon()
class GameEnvironment:
    def __init__(self, factory):
        self.factory = factory
        self.p = factory.makeCharacter()
        self.ob = factory.makeObstacle()
    def play(self):
        self.p.interactWith(self.ob)
if __name__ == '__main__':
    g1 = GameEnvironment(KittiesAndPuzzles())
    g2 = GameEnvironment(KillAndDismember())
    g1.play()
    g2.play()
