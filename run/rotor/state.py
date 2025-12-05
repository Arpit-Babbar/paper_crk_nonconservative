# state file generated using paraview version 5.10.1

# uncomment the following three lines to ensure this script works in future versions
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

import numpy as np
import argparse
parser = argparse.ArgumentParser()
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
parser.add_argument('--input', type=str, default='128')
args = parser.parse_args()
input_file = os.path.join(dir_path, f'output_rotor_{args.input}', 'avg001.vtr')
# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [500, 500]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [0.5, 0.5, 0.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.5221861432527093, 0.49750491359071486, 10000.0]
renderView1.CameraFocalPoint = [0.5221861432527093, 0.49750491359071486, 0.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.43457146980081657
renderView1.UseColorPaletteForBackground = 0
renderView1.Background = [1.0, 1.0, 1.0]

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(500, 500)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Rectilinear Grid Reader'
sol00 = XMLRectilinearGridReader(registrationName='avgl00*', FileName=[input_file])
sol00.PointArrayStatus = ['rho', 'v1', 'v2', 'v3', 'p', 'B1', 'B2', 'B3', 'psi']
sol00.TimeArray = 'None'

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=sol00)
calculator1.Function = 'sqrt(v1^2+v2^2)/sqrt(1.4*p/rho)'

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=calculator1)
contour1.ContourBy = ['POINTS', 'Result']
contour1.Isosurfaces = np.linspace(0.0, 4.0, 20).tolist()
contour1.PointMergeMethod = 'Uniform Binning'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from contour1
contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

# get separate color transfer function/color map for 'Result'
separate_contour1Display_ResultLUT = GetColorTransferFunction('Result', contour1Display, separate=True)
separate_contour1Display_ResultLUT.AutomaticRescaleRangeMode = 'Never'
separate_contour1Display_ResultLUT.RGBPoints = [0.0, 1.0, 1.0, 1.0, 1.1757813367477812e-38, 0.0, 0.0, 0.0]
separate_contour1Display_ResultLUT.ColorSpace = 'RGB'
separate_contour1Display_ResultLUT.NanColor = [1.0, 0.0, 0.0]
separate_contour1Display_ResultLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = ['POINTS', 'Result']
contour1Display.LookupTable = separate_contour1Display_ResultLUT
contour1Display.SelectTCoordArray = 'None'
contour1Display.SelectNormalArray = 'None'
contour1Display.SelectTangentArray = 'None'
contour1Display.OSPRayScaleArray = 'Result'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = 0.04241829812526703
contour1Display.SelectScaleArray = 'Result'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'Result'
contour1Display.GaussianRadius = 0.0021209149062633515
contour1Display.SetScaleArray = ['POINTS', 'Result']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = ['POINTS', 'Result']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'
contour1Display.LineWidth = 2.0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [1.9026877097546613, 0.0, 0.5, 0.0, 1.902931809425354, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [1.9026877097546613, 0.0, 0.5, 0.0, 1.902931809425354, 1.0, 0.5, 0.0]

# set separate color map
contour1Display.UseSeparateColorMap = True

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get separate opacity transfer function/opacity map for 'Result'
separate_contour1Display_ResultPWF = GetOpacityTransferFunction('Result', contour1Display, separate=True)
separate_contour1Display_ResultPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
separate_contour1Display_ResultPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(contour1)
# ----------------------------------------------------------------

myview = GetActiveView()
if args.input == '128':
    output_filename = './rotor_density_128.png'
elif args.input == '256':
    output_filename = './rotor_density_256.png'
elif args.input == '512':
    output_filename = './rotor_density_512.png'
else:
    assert False, "unknown input file"
SaveScreenshot(output_filename, myview,
        ImageResolution=[2000, 2000])

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')