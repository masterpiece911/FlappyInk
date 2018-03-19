
__author__="Alexander De Luca"

import math

class Vector(object):
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        if x <> 0 or y <> 0:
            self.magnitude = math.sqrt(self.x**2 + self.y**2)
            self.angle = math.acos(self.x/self.get_magnitude())/math.pi*180

            if self.y > 0:
                self.angle = 360 - self.angle
        else:
            self.magnitude = 0
            self.angle = 0

    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)

    def get_magnitude(self):
        return self.magnitude

    def normalize(self):
        magnitude = self.get_magnitude()
        if magnitude != 0:
            self.x /= magnitude
            self.y /= magnitude

    @classmethod
    def vector_from_points(cls,from_p,to_p):
        return cls(to_p[0]-from_p[0],to_p[1]-from_p[1])

    """Returns the angle based on the vector. """
    def get_angle(self):
    	# print "Angle: %s"%(self.angle,)
    	return self.angle
