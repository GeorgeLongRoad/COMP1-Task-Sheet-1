from crop_class import *

class Wheat(Crop):
    """A wheat crop"""

    #constructor
    def __init__(self):
        #call the parent class  constructor with the default values
        #for wheat, growth rate = 1, light need = 4, water need = 7
        super().__init__(1,4,7)
        self._type = "Wheat"

    #override grow for subclass
    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == "Seedling": 
                self._growth += self._growth_rate * 1.5
            elif self._status == "Young": 
                self._growth += self._growth_rate * 1.25
            elif self._status == "Old":
                self._growth += self._growth_rate / 2
            else:
                self._growth =+ self._growth_rate
        #increment days gorwing
        self._days_growing += 1
        #update status
        self._update_status()
                


def main():
    #create a new wheat crop
    wheat_crop = Wheat()
    print(wheat_crop.report())
    #manually grow crop
    manual_grow(wheat_crop)
    print(wheat_crop.report())
    manual_grow(wheat_crop)
    print(wheat_crop.report())

if __name__ == "__main__":
    main()
    
