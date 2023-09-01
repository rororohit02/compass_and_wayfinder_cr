"""
Module Name: wayfinder.py
Function:   ...
"""
#TODO: Modify code to be a grid that represents 30 degrees horizontal and 30 degrees vertical. Does not utilize AR.
#      and make the universal angles change as the user rotates
#      i.e. user horizontally faces north @ 0deg, program captures -15deg to 15deg, horizontally and vertically then if they rotate right to NE @ 30deg, program captures 0deg to 30deg, horizontally and still -15deg to 15deg vertically

#TODO: Incorporate into glass display


import math
import matplotlib.pyplot as plt
#import random


def setup_graph():
    plt.switch_backend('TkAgg')
    plt.ylim(-30,30)
    plt.xlim(-30,30)
    
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    
    plt.title('Longitude & Latitude Graph')

def get_user_input():
    x = int(input('Enter x: '))
    y = int(input('Enter y: '))
    z = int(input('Enter z: '))
    initialHorizontalAngle = int(input('Enter initial horizontal angle facing: ')) #initialHorizontalAngle
    initialVerticalAngle = int(input('Enter initial vertical angle facing: ')) #initialVerticalAngle
    return x, y, z, initialHorizontalAngle, initialVerticalAngle


#IDK WHAT'S GOING ON HERE BRO
def do_calculations(coordinate: tuple, iHA, iVA):
    assert(len(coordinate) == 3)
    x,y,z = coordinate

    horizontalDistance = math.sqrt((x*x)+(y*y))

    lat_rad = math.atan(x/y)
    lon_rad = math.atan(z/horizontalDistance)

    lat_deg = math.degrees(lat_rad) #change to degrees for graph
    lat_deg = round(lat_deg/10)*10 #round to nearest 10th
    """
    ABOVE LINE OF CODE ACTUALLY ROUNDS LAT VARIABLE TO CLOSEST MULTIPLE OF 10
    """

    lon_deg = math.degrees(lon_rad) # ""
    lon_deg = round(lon_deg/5)*5 # ""
    """
    ABOVE LINE OF CODE ACTUALLY ROUNDS LON VARIABLE TO CLOSEST MULTIPLE OF 5
    """

    iHA = round(iHA/10)*10 #same for this ^
    iVA = round(iVA/5)*5
    azimuth = lat_deg - iHA ##horizontal sweep
    elevation = lon_deg - iVA ##vertical sweep

    return azimuth, elevation


#Main Function
if __name__ == "__main__":
    print("START")

    x, y, z, initialHorizontalAngle, initialVerticalAngle = get_user_input()
    azimuth, elevation = do_calculations((x,y,z), initialHorizontalAngle, initialVerticalAngle)
    plt.plot(azimuth, elevation,    color='green', 
                                    linestyle='dashed', 
                                    linewidth = 3,
                                    marker='o', 
                                    markerfacecolor='blue', 
                                    markersize=12)
    plt.show()

    print("FINISH")






