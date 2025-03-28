from mammal import Mammal
from person import Person
from tick import Tick
from puma import Puma

# Mammal instance
m = Mammal(10)
m.speak()
print(m)

print("\n---\n")

# Person instance
p = Person(name="John Doe", age=25, height=175)
p.speak()
p.heart.beat()
print(p)

print("\n---\n")

# Tick instance
t = Tick()
t.suck_blood()
print(t)

print("\n---\n")

# Puma with a Tick (aggregation)
pm = Puma(age=4, tick=t)
pm.speak()
pm.claw()
pm.tick.suck_blood()
print(pm)
