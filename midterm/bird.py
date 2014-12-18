#! /bin/env python

import math

class Bird(object):
    def __init__(self, name, speed, age):
        self.name = name
        self.speed = speed
        self.age = age
        self.pos = [0, 0] # x,y
    
    def __str__(self):
        """ also fill this in """
        return self.name + ", " + str(self.speed) + ", " + str(self.age)
    
    def fly(self, flaps, direction):
        rad_dir = math.radians(direction)
        self.pos[0] = self.pos[0] + (self.speed * flaps * math.cos(rad_dir))
        self.pos[1] = self.pos[1] + (self.speed * flaps * math.cos(rad_dir))

    def grow_up(self):
        self.age += 1


""" Create a child class phoenix that inherits from Bird. 
implement at least one new method e.g. reborn_from_ashes
override at least one method
add at least one attribute
set one attribute to be a specific value for phoenix objects
"""
class Phoenix(Bird):
    def __init__(self, name, died, heat_tolerance, age): 
        Bird.__init__(self, name, 1000, age)
        self.died = died
        self.heat_tolerance = heat_tolerance

    def __str__(self):
        return self.name + ", " + str(self.died) + ", " + str(self.heat_tolerance) + ", " + str(self.age)

    def die_in_flames(self):
        self.died += 1
        self.grow_up() # every time a phoenix is reborn they grow up

    def does_it_die_quesionmark(self, temperature): # when it wants to be reborn it heats itself up past it's tolerance
        if temperature > self.heat_tolerance:
            self.die_in_flames()

    def grow_up(self):
        self.heat_tolerance += math.sqrt(self.died) # heat tolerance increases by the square root of the number of rebirths
        if self.died % 10 == 0:
            self.age -= 20 # phoenixes get 20 lives back from being reborn ten times
        else:
            self.age += 1

def main():
    """create an instance of both the parent and child class
    call a method with each
    change an attribute for each
    print each instance
    """
    mogule = Bird("Mogule", 300, 2)
    mogule.grow_up()
    mogule.speed = 20 # he got in an accident
    print(mogule)

    diatrix = Phoenix("Diatrix", 300, 1032, 0)
    diatrix.grow_up()
    diatrix.name = "Fudge"
    print(diatrix)
    

if __name__ == "__main__":
    main()

