from crop_class import *

class Potato(Crop):
    """A Potato Crop"""
    #Constructor
    def __init__(self):
        #call the superclass with the default values
        #Growth rate: 1, light need: 3, water need:6
        super().__init__(1,3,6)
        self._type = "Potato"

    #Polymorph grow method for potato subclass
    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == "Seedling" and water > self._water_need:
                self._growth += self._growth_rate *1.5
            elif self._status == "Young" and water > self._water_need:
                self._growth += self_growth_rate * 1.25
            else:
                self._growth += self._growth_rate
        self._days_growing += 1
        self.update_status()

def main():
    potato_crop = Potato()
    print(potato_crop.report())
    manual_grow(potato_crop)
    print(potato_crop.report())
    manual_grow(potato_crop)
    print(potato_crop.report())

if __name__ == "__main__":
    main()
