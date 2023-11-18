import random as rd
import math

def random_points(radius, x_center, y_center):
    x = rd.uniform(x_center-radius,x_center+radius)
    y = math.sqrt(abs((x-x_center)**2 - radius**2))
    y = rd.uniform(y_center-y,y+y_center)
    return x,y
