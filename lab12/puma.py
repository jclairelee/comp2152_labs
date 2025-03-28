from mammal import Mammal
from tick import Tick

class Puma(Mammal):
    def __init__(self, age, tick=None):
        super().__init__(age)
        self.tick = tick if tick else Tick()

    def speak(self):
        print("Roar")

    def claw(self):
        print("The puma takes a swipe!")

    def __str__(self):
        return f"Puma is {self.age} years old."
