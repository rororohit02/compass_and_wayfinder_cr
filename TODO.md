# TODO List

## General Items
- [x] Make TODO List
- [x] Format code better

## Wayfinder.py
- [ ] Modify code to be a grid that represents 30 degrees horizontal and 30 degrees vertical (Does not utilize AR) and make the universal angles change as the user rotates
- [ ] Incorporate into glass display

## Compass.py

- [ ] Implement latitude and longitude coordinate and translate to Cartesian using ESRI maps and MATLAB.
    * https://www.mathworks.com/help/matlab/matlab_external/call-matlab-functions-asynchronously-from-python.html
    * https://www.mathworks.com/help/map/ref/projcrs.html
    * UTM ESRI Code for North Texas: 103539 (https://epsg.io/?q=kind:PROJCRS&page=67) North Central Texas: 103540 (worth using both) 103539-103543 Texas Range


- [x] Find a way to remove the grid so that only the vector is graphed without any axis
- [ ] Loop code to run indefinitely given coordinates
- [x] Add queue and basic 'animation'
- [ ] Improve animation running time/efficiency
- [ ] Implement more robust calculations with numpy or OpenCV
- [ ] Add support for asynchronous data input
    * https://realpython.com/python-async-features/
    * https://realpython.com/async-io-python/
- [x] Add support for changing view angle
- [ ] Make function to plot compass arrow (vector)
- [ ] Possibly make animation take plotting function as parameter?
