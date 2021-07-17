from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric(self):
        pass


class Coat(Clothes):
    def __init__(self, V):
        self.V = V

    @property
    def fabric(self):
        return self.V / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, H):
        self.H = H

    @property
    def fabric(self):
        return self.H * 2 + 0.3


my_c = Coat(5)
my_s = Suit(1.70)
print(my_c.fabric)
print(my_s.fabric)
