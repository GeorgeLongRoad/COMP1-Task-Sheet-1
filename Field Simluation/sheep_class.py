from animal_class import *

class Sheep(Animal):
    """A sheep simulation"""
    def __init__(self):
        super().__init__(1,7,7)
        self._type = "Sheep"
        self._weight = 0

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Baby" and water > self._water_need and( food > self._food_need) :
                self._weight += self._growth_rate * 2.2
            elif self._status == "Young" and water > self._water_need and( food > self._food_need):
                self._weight += self._growth_rate * 2
            elif self._status == "Old" and water > self._water_need and( food > self._food_need):
                self._weight += self._growth_rate / 1.8
            else:
                self._weight += self._growth_rate
        self._days_growing += 1
        self._update_status()

def main():
    #create a new sheep
    sheep_one = Sheep()
    print(sheep_one.report())

    manual_grow(sheep_one)
    print(sheep_one.report())

    manual_grow(sheep_one)
    print(sheep_one.report())

if __name__ == "__main__":
    main()
