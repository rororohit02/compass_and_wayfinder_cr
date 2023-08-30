#Function: Takes any universal point and creates a unit vector with
#          respect to the origin in a 3d space. Graph is designed to
#          be rotated about the azimuth (horizontal angle) to account
#          for the user's orientation.

#TODO: Implement latitude and longitude coordinates
# and translate to Cartesian using ESRI maps and MATLAB.
# https://www.mathworks.com/help/matlab/matlab_external/call-matlab-functions-asynchronously-from-python.html
# https://www.mathworks.com/help/map/ref/projcrs.html
# UTM ESRI Code for North Texas: 103539 (https://epsg.io/?q=kind:PROJCRS&page=67)
# UTM ESRI Code for North Central Texas: 103540 (worth using both, I can't decide)

#TODO: Find a way to remove the grid so that only the vector is graphed
#       without any axis

#TODO: Loop code to run indefinitely


import math
import random # To be used with random coordinates in the future

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.switch_backend('TkAgg') # Recommended for plotting vectors in a 3d space

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#Set limits to max length of unit vector in all directions.
#Unit vector: Vector length (magnitude) will not exceed 1.
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

#Set labels for all 3 axes
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
  
# giving a title to my graph
plt.title('Compass')

print("Running")

# Get cartesian coordinates from origin. Represents vector between two
# geographical coordinates with origin being observer's coords, along with
# horizontal offset accounting for the direction that the observer 
# is facing (azimuth).
x = int(input('enter x: '))
y = int(input('enter y: '))
z = int(input('enter z: '))
azimuth = int(input('enter initial horizontal angle facing: '))

#Get magnitude of vector
magnitude = math.sqrt((x*x)+(y*y)+(z*z))

# plotting the points 
ax.quiver(0 ,0, 0, (x/magnitude), (y/magnitude), (z/magnitude), )

#Orient graph along x-axis without adjustment for azimuth
ax.view_init(30,azimuth-90)

#Show graph
plt.show()







