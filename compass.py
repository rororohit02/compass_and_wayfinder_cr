"""
Module Name: compass.py
Function:   Takes any universal point and creates a unit vector with
            respect to the origin in a 3d space. Graph is designed to
            be rotated about the azimuth (horizontal angle) to account
            for the user's orientation.
"""

#TODO: Implement latitude and longitude coordinates
#       and translate to Cartesian using ESRI maps and MATLAB.
#       https://www.mathworks.com/help/matlab/matlab_external/call-matlab-functions-asynchronously-from-python.html
#       https://www.mathworks.com/help/map/ref/projcrs.html
#       UTM ESRI Code for North Texas: 103539 (https://epsg.io/?q=kind:PROJCRS&page=67) North Central Texas: 103540 (worth using both) 103539-103543 Texas Range


#TODO: Find a way to remove the grid so that only the vector is graphed
#       without any axis DONE

#TODO: Loop code to run indefinitely

#TODO: Format code better


import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#import random #To be used with random coordinates in the future


def setup_graph():
    plt.switch_backend('TkAgg') # Recommended for plotting vectors in a 3d space
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    #Unit vector: Vector length (magnitude) will not exceed 1.
    
    ax.set_xlim([-1, 1]) #Set limits to max length of unit vector for all 3 axes.
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    
    plt.axis('off') #Turns off axes and grid

    plt.title('Compass')
    return fig, ax


def get_user_input():
    # Get cartesian coordinates from origin. Represents vector between two
    # geographical coordinates with origin being observer's coords, along with
    # horizontal offset accounting for the direction that the observer 
    # is facing (azimuth).
    x = int(input('Enter x: '))
    y = int(input('Enter y: '))
    z = int(input('Enter z: '))
    azimuth = int(input('Enter initial horizontal angle facing: '))
    return x, y, z, azimuth


def generate_unit_vector(coordinate: tuple, azimuth: int) -> tuple:
    assert(len(coordinate) == 3)
    x,y,z = coordinate
    magnitude = math.sqrt((x*x)+(y*y)+(z*z))
    return ((x/magnitude), (y/magnitude), (z/magnitude))


#Main Function
if __name__ == "__main__":
    print("START")

    fig, ax = setup_graph()
    x, y, z, azimuth = get_user_input()
    origin = (0,0,0)
    unit_vector = generate_unit_vector((x,y,z), azimuth)
    ax.quiver(*origin, *unit_vector, ) #Plot vector 
    ax.view_init(30,azimuth-90)  #Orient graph along x-axis without adjustment for azimuth
    plt.show()

    print("FINISH")