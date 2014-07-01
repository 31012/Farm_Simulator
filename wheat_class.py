from crop_class import *

class Wheat(Crop):
    """A Wheat Crop"""
    #Constructor
    def __init__(self):
        #call the superclass with the default values
        #Growth rate: 1, light need: 3, water need:6
        super().__init__(1,7,5)
        self._type = "Wheat"

    #Polymorph grow method for potato subclass
    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            if water > self._water_need:
                self._growth += self._growth_rate *0.5
            elif light > self._light_need:
                self._growth += self._growth_rate * 1.25
            else:
                self._growth += self._growth_rate
        self._days_growing += 1
        self.update_status()
