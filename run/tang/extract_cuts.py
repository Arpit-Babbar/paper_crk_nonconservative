# state file generated using paraview version 5.10.1

# uncomment the following three lines to ensure this script works in future versions
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *

# create a new 'XML Rectilinear Grid Reader'
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
sol = XMLRectilinearGridReader(registrationName='sol*', FileName=[os.path.join(dir_path, 'output_orszag_tang', 'sol100.vtr')])
sol.PointArrayStatus = ['rho', 'v1', 'v2', 'v3', 'p', 'B1', 'B2', 'B3', 'psi']
sol.TimeArray = 'None'

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(registrationName='PlotOverLine1', Input=sol)
plotOverLine1.Point1 = [0.0, 0.3125, 0.0]
plotOverLine1.Point2 = [1.0, 0.3125, 0.0]

SaveData('pressure_profile_3125.csv',
         proxy=plotOverLine1,
         PointDataArrays=['Points_X', 'p'])

plotOverLine2 = PlotOverLine(registrationName='plotOverLine2', Input=sol)
plotOverLine2.Point1 = [0.0, 0.4277, 0.0]
plotOverLine2.Point2 = [1.0, 0.4277, 0.0]

SaveData('pressure_profile_4277.csv',
         proxy=plotOverLine2,
         PointDataArrays=['Points_X', 'p'])