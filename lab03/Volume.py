import math
def sphereVolume(radius):
    if radius<=0:
        print('Enter integer bigger than 0')
        return
    else:
        d= round(4/3*(math.pow(radius,3)), 2)
        dPi= round(4/3*(math.pow(radius,3))*math.pi,2)
        print(f'Diameter of the sphere without converting pi - {d}π, and without - {dPi}')
        return 
#rounded to 2 numbers after point for less numbers in the answer