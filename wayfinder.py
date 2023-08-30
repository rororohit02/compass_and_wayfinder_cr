#TODO: Modify code to be a grid that represents 30 degrees horizontal and 30 degrees vertical. Does not utilize AR.
#      and make the universal angles change as the user rotates
#      i.e. user horizontally faces north @ 0deg, program captures -15deg to 15deg, horizontally and vertically

#TODO: Incorporate into glass display


import math
import random

import matplotlib.pyplot as plt
plt.switch_backend('TkAgg')
# setting x and y axis range
plt.ylim(-30,30)
plt.xlim(-30,30)
  
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
  
# giving a title to my graph
plt.title('Longitude & Latitude Graph')

print("Running")

x = int(input('enter x: '))
y = int(input('enter y: '))
z = int(input('enter z: '))
initialHorizontalAngle = int(input('enter initial horizontal angle facing: '))
initialVerticalAngle = int(input('enter initial vertical angle facing: '))

horizontalDistance = math.sqrt((x*x)+(y*y))


lat_rad = math.atan(x/y)
lon_rad = math.atan(z/horizontalDistance)


lat = math.degrees(lat_rad) #change to degrees for graph
lat = round(lat/10)*10 #round to nearest 10th

lon = math.degrees(lon_rad) # ""

lon = round(lon/5)*5 # ""

initialHorizontalAngle = round(initialHorizontalAngle/10)*10 #same for this ^
initialVerticalAngle = round(initialVerticalAngle/5)*5


azimuth = lat - initialHorizontalAngle ##horizontal sweep
elevation = lon - initialVerticalAngle ##vertical sweep

print(x)
print(y)

# plotting the points
plt.plot(azimuth, elevation, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)

# function to show the plot
plt.show()






