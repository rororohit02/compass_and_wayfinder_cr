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

#TODO: Format code better DONE

#TODO: Add support for async data input
#       https://realpython.com/python-async-features/
#       https://realpython.com/async-io-python/

#TODO: Use more efficient python math/matrix package eventually
#       Numpy?
#       OpenCV?

#TODO: Improve animation method for updating graph



import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
#import numpy as np
import queue
#import random #To be used with random coordinates in the future
from time import sleep

class coord:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        
    def __init__(self, coord: tuple):
        assert(len(coord) == 3)
        self.x, self.y, self.z = coord
    
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def get_unit_vector(self) -> tuple:
        mag = self.magnitude()
        return (self.x / mag, self.y / mag, self.z / mag)

    def __str__(self):
        return "Coord x, y, z: "+ str(self.x) + " " + str(self.y) + " " + str(self.z)
    
#Not used in this branch
def setup_graph():
    plt.switch_backend('TkAgg') # Recommended for plotting vectors in a 3d space
    fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')
    ax = fig.add_suplot(projection='3d')
    
    #Unit vector: Vector length (magnitude) will not exceed 1.
    
    #ax.set_xlim([-1, 1]) #Set limits to max length of unit vector for all 3 axes.
    #ax.set_ylim([-1, 1])
    #ax.set_zlim([-1, 1])
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    
    #plt.axis('off') #Turns off axes and grid

    plt.title('Compass')
    return fig, ax

#Not used in this branch
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

#Not used in this branch
def generate_unit_vector(coordinate: tuple) -> tuple:
    assert(len(coordinate) == 3)
    x,y,z = coordinate
    magnitude = math.sqrt((x*x)+(y*y)+(z*z))
    return ((x/magnitude), (y/magnitude), (z/magnitude))


#Main Function
if __name__ == "__main__":
    print("START")

    #Queued Animated Dots
    plt.switch_backend('TkAgg') # Recommended for plotting vectors in a 3d space

    #Setup simple 3-D fig/x
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    #Set limits and views
    ax.set_xlim([-1,11])
    ax.set_ylim([-1,11])
    ax.set_zlim([-1,11])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    azimuth = 45
    ax.view_init(30,azimuth-90)
    plt.title('Compass')
    
    #Set up simple queue and enumerate test coordinate data
    q = queue.SimpleQueue()
    coords_data = [(0,0,0), (10,0,0), (10, 10, 0), (0, 10, 0), (0, 10, 10), (0, 0, 10), (10, 0, 10), (10, 10, 10)]
    for coord_data in coords_data:
        q.put(coord(coord_data))
    x_data = []
    y_data = []
    z_data = []

    #Loop through queue, update data as new coords dequeued, and redraw plot
    for _ in range(q.qsize()):
        new_coord = q.get()

        #Update data
        x_data.append(new_coord.x) 
        y_data.append(new_coord.y)
        z_data.append(new_coord.z)

        #Draw data with pause after
        ax.scatter(x_data, y_data, z_data)
        plt.draw() 
        plt.pause(.5)
    
    print("FINISH")