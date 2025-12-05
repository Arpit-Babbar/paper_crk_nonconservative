# state file generated using paraview version 5.10.1

# uncomment the following three lines to ensure this script works in future versions
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--nx', type=str, default='50')
args = parser.parse_args()

nx = args.nx

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [600, 600]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.0, 0.0, 10000.0]
renderView1.CameraFocalPoint = [0.0, 0.0, 0.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 1.7434870882563087

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(600, 600)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
input_filename = os.path.join(dir_path, f'tmp_super_stiff_2d_nx{nx}', 'avg010.vtr')
# create a new 'XML Rectilinear Grid Reader'
avg0 = XMLRectilinearGridReader(registrationName='avg0*', FileName=[input_filename])
avg0.PointArrayStatus = ['sol', 'rho', 'vx', 'vy', 'P11', 'P12', 'P22', 'Exact rho', 'Exact vx', 'Exact vy', 'Exact P11', 'Exact P12', 'Exact P22']
avg0.TimeArray = 'None'

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=avg0)
calculator1.Function = 'rho'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from calculator1
calculator1Display = Show(calculator1, renderView1, 'UniformGridRepresentation')

# get color transfer function/color map for 'Result'
resultLUT = GetColorTransferFunction('Result')
resultLUT.RGBPoints = [0.0036281049925972367, 0.231373, 0.298039, 0.752941, 0.91039026452291, 0.865003, 0.865003, 0.865003, 1.8171524240532217, 0.705882, 0.0156863, 0.14902]
resultLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Result'
resultPWF = GetOpacityTransferFunction('Result')
resultPWF.Points = [0.0036281049925972367, 0.0, 0.5, 0.0, 1.8171524240532217, 1.0, 0.5, 0.0]
resultPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['POINTS', 'Result']
calculator1Display.LookupTable = resultLUT
calculator1Display.SelectTCoordArray = 'None'
calculator1Display.SelectNormalArray = 'None'
calculator1Display.SelectTangentArray = 'None'
calculator1Display.OSPRayScaleArray = 'Result'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'None'
calculator1Display.ScaleFactor = 0.398
calculator1Display.SelectScaleArray = 'Result'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'Result'
calculator1Display.GaussianRadius = 0.0199
calculator1Display.SetScaleArray = ['POINTS', 'Result']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'Result']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityUnitDistance = 0.16513128189825013
calculator1Display.ScalarOpacityFunction = resultPWF
calculator1Display.OpacityArrayName = ['POINTS', 'Result']
calculator1Display.IsosurfaceValues = [51.535275802294635]
calculator1Display.SliceFunction = 'Plane'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [32.00013467764074, 0.0, 0.5, 0.0, 71.07041692694852, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [32.00013467764074, 0.0, 0.5, 0.0, 71.07041692694852, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for resultLUT in view renderView1
resultLUTColorBar = GetScalarBar(resultLUT, renderView1)
# resultLUTColorBar.WindowLocation = 'Any Location'
# resultLUTColorBar.Position = [0.02029209621993129, 0.034468179795282654]
# resultLUTColorBar.Title = ''
# resultLUTColorBar.ComponentTitle = ''
# resultLUTColorBar.RangeLabelFormat = '%2.1f'
# resultLUTColorBar.ScalarBarLength = 0.9416666666666642

# set color bar visibility
# resultLUTColorBar.Visibility = 1

# show color legend
calculator1Display.SetScalarBarVisibility(renderView1, False)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(calculator1)
# ----------------------------------------------------------------

myview = GetActiveView()
filename = f'./tmp_2d_rho_final_nx{nx}.png'
SaveScreenshot(filename, myview,
        ImageResolution=[2400, 2400])

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')