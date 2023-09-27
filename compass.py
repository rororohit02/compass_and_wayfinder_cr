"""
Module Name: compass.py
Function:   Takes any universal point and creates a unit vector with
            respect to the origin in a 3d space. Graph is designed to
            be rotated about the azimuth (horizontal angle) to account
            for the user's orientation.
"""


import math
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
#from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

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

#Technical Test for animating views and spins with expanding data
def scatter_and_spin(coordinate_data: list, viewing_data: list):
    assert(len(coordinate_data) == len(viewing_data))

    plt.switch_backend('TkAgg') # Recommended for plotting vectors in a 3d space

    #Setup simple 3-D fig/x
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    #Set limits and views, without limits view space fits the existing data
    ax.set_xlim([-1,11]) 
    ax.set_ylim([-1,11])
    ax.set_zlim([-1,11])

    #plt.axis('off')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.title('Compass')

    #Set up simple queue and enumerate test coordinate data and test viewing data
    q_coords = queue.SimpleQueue()
    q_views = queue.SimpleQueue()
    for coord_data in coordinate_data:
        q_coords.put(coord(coord_data))
    for view_data in viewing_data:
        q_views.put(view_data)
    x_data = []
    y_data = []
    z_data = []

    #Loop through queue, update data as new coords dequeued, and redraw plot
    for _ in range(q_coords.qsize()):
        new_coord = q_coords.get()
        new_view = q_views.get()

        #Update data
        x_data.append(new_coord.x) 
        y_data.append(new_coord.y)
        z_data.append(new_coord.z)
        ax.view_init(30,new_view-90)

        #Draw data with pause after
        ax.scatter(x_data, y_data, z_data)
        plt.draw() 
        plt.pause(.5)


#Draw 3d coordinates given object position, viewing angle, and a graphing function
def draw_3d_graph(position_data: list, viewing_angle_data: list, graph_function):
   pass


#Display a static 3d vector with a slider for viewing angle
def mvp_with_slider(endpoint_pos):

    plt.switch_backend('TkAgg') # Recommended for plotting vectors in a 3d space

    #Setup simple 3-D fig/x
    fig = plt.figure()
    plot_ax = fig.add_axes([0, 0, 1, .8], projection='3d')
    slider_ax = fig.add_axes([0.1, 0.85, 0.8, 0.1])
    plot_ax.set_xlim([-1,1]) 
    plot_ax.set_ylim([-1,1])
    plot_ax.set_zlim([-1,1])

    #Make unit vector to endpoint_pos
    #Replace with Matlab calc
    mag = math.sqrt(endpoint_pos[0]**2 + endpoint_pos[1]**2 + endpoint_pos[2]**2)
    unit_vec = (endpoint_pos[0]/mag, endpoint_pos[1]/mag, endpoint_pos[2]/mag)
    origin = (0,0,0)
    plot_ax.quiver(*origin, *unit_vec)

    angle_slide = Slider(ax=slider_ax, label='Azimuth (deg)', valmin=0, valmax=359, valinit=0, valstep=1)

    #Update function for view angle slider
    def update(val):
        azimuth = angle_slide.val
        plot_ax.view_init(30, azimuth)

    angle_slide.on_changed(update)
    plt.show()


#Main Function
#Should be minimal coding within here
if __name__ == "__main__":
    print("START")

    #Animated Vector Graph
    #origin_pos = (0,0,0)

    #Animated Scatter Graph
    """
    scatter_data = [(0,0,0), (10,0,0), (10, 10, 0), (0, 10, 0), (0, 10, 10), (0, 0, 10), (10, 0, 10), (10, 10, 10), (0, 0, -10)]
    views_data = [45,30,15,0,-15,-30,-45, -60, -60] #as the azimuth viewing data
    scatter_and_spin(scatter_data, views_data)
    """
    pos = (10,10,10)
    mvp(pos)



    
    
    print("FINISH")