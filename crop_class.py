import random

class Crop:
    """A generic food crop"""
    #Constructor
    def __init__(self, growth_rate, light_need, water_need):
        #Set the attributes with an initial value
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"
        #Above attributes are private, due to the _ underscore infront of them

def main():
    #class instantiation
    new_crop = Crop(1,5,4)
    #crop test
    print(new_crop._status)
    print(new_crop._light_need)
    print(new_crop._water_need)

if __name__ == "__main__":
    main()
