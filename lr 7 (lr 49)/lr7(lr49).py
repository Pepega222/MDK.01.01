from collections import defaultdict

colours = (
 ('Yasoob', 'Yellow'),
 ('Ali', 'Blue'),
 ('Arham', 'Green'),
 ('Ali', 'Black'),
 ('Yasoob', 'Red'),
 ('Ahmed', 'Silver'),)

favourite_colours = defaultdict(list)

for name, colour in colours:
    favourite_colours[name].append(colour)

print(favourite_colours)

import collections
tree = lambda: collections.defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = "yellow"

print(some_dict)

from collections import OrderedDict
colours = OrderedDict([("Red", 198), ("Green", 170), ("Blue", 160)])
for key, value in colours.items():
   print(key, value)

from collections import Counter
colours = (
 ('Yasoob', 'Yellow'),
 ('Ali', 'Blue'),
 ('Arham', 'Green'),
 ('Ali', 'Black'),
 ('Yasoob', 'Red'),
 ('Ahmed', 'Silver'),
)
favs = Counter(name for name, colour in colours)
print(favs)

#with open('filename', 'rb') as f:
    #line_count = Counter(f)
#print(line_count)

from collections import deque
d = deque()
d.append('1')
d.append('2')
d.append('3')
print(len(d))

print(d[0])

print(d[-1])

d = deque(range(5))
#print(len(d))
# Вывод: 5
d.popleft()
# Вывод: 0
d.pop()
# Вывод: 4
print(d)
# Вывод: deque([1, 2, 3])

d = deque(maxlen=30)

d = deque([1,2,3,4,5])
d.extendleft([0])
d.extend([6,7,8])
print(d)
# Вывод: deque([0, 1, 2, 3, 4, 5, 6, 7, 8])

man = ('Ali', 30)
print(man[0])

from collections import namedtuple
Arthur = namedtuple('Man', 'name age type')
Arthur = Arthur(name="Arthur", age=31, type="russian")
print(Arthur)

print(Arthur.name)

from collections import namedtuple
Arthur = namedtuple('Man', 'name age type')
Arthur = Arthur(name="Arthur", age=31, type="russian")
print(Arthur[0])

from collections import namedtuple
Arthur = namedtuple('Man', 'name age type')
Arthur = Arthur(name="Arthur", age=31, type="russian")
print(Arthur._asdict())


from collections import namedtuple
from enum import Enum
class Species(Enum):
 cat = 1
 dog = 2
 horse = 3
 aardvark = 4
 butterfly = 5
 owl = 6
 platypus = 7
 dragon = 8
 unicorn = 9

 kitten = 1
 puppy = 2
Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type=Species.cat)
drogon = Animal(name="Drogon", age=4, type=Species.dragon)
tom = Animal(name="Tom", age=75, type=Species.cat)
charlie = Animal(name="Charlie", age=2, type=Species.cat)

print(charlie.type == tom.type)

print(charlie.type)

print(Species(1))
print(Species['cat'])
print(Species.cat)