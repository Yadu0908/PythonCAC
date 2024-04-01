import math

def circle(radius):

    area= math.pi * radius**2;
    circumfarance= 2 * math.pi * radius;


    return round(area, 2), round(circumfarance, 2)   # by using round built in function we can round the long float number.


a, c = circle(3)

print(f"{a} is area and {c} is circumfarance")