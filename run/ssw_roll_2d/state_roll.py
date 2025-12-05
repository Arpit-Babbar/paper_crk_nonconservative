# state file generated using paraview version 5.10.1

# uncomment the following three lines to ensure this script works in future versions
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1517, 752]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesLabelColor = [0.0, 0.0, 0.0]
renderView1.OrientationAxesOutlineColor = [0.0, 0.0, 0.0]
renderView1.CenterOfRotation = [0.6499999979278073, 0.250000006868504, 0.39098218083381653]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.7979257675914452, -0.9945211867480344, 0.8766808909971586]
renderView1.CameraFocalPoint = [0.6641696788141908, 0.1933611585209929, 0.2758491643291966]
renderView1.CameraViewUp = [-0.39571246800596327, 0.37863914088810563, 0.8366863472366135]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.7134413780295448
renderView1.UseColorPaletteForBackground = 0
renderView1.Background = [1.0, 1.0, 1.0]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.GridColor = [0.0, 0.0, 0.0]

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1517, 752)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Rectilinear Grid Reader'
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
sol0 = XMLRectilinearGridReader(registrationName='sol0*', FileName=[os.path.join(dir_path, 'ssw_roll_2d', 'sol010.vtr')])
sol0.PointArrayStatus = ['sol']
sol0.TimeArray = 'None'

# create a new 'Warp By Scalar'
warpByScalar1 = WarpByScalar(registrationName='WarpByScalar1', Input=sol0)
warpByScalar1.Scalars = ['POINTS', 'sol']
warpByScalar1.ScaleFactor = 45.0

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from warpByScalar1
warpByScalar1Display = Show(warpByScalar1, renderView1, 'StructuredGridRepresentation')

# get color transfer function/color map for 'sol'
solLUT = GetColorTransferFunction('sol')
solLUT.RGBPoints = [0.005157507725791254, 0.278431372549, 0.278431372549, 0.858823529412, 0.006167369502262567, 0.0, 0.0, 0.360784313725, 0.007170169308269046, 0.0, 1.0, 1.0, 0.008187093055205194, 0.0, 0.501960784314, 0.0, 0.009189892861211673, 1.0, 1.0, 0.0, 0.010199754637682986, 1.0, 0.380392156863, 0.0, 0.0112096164141543, 0.419607843137, 0.0, 0.0, 0.012219478190625613, 0.878431372549, 0.301960784314, 0.301960784314]
solLUT.ColorSpace = 'RGB'
solLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'sol'
solPWF = GetOpacityTransferFunction('sol')
solPWF.Points = [0.005157507725791254, 0.0, 0.5, 0.0, 0.012219478190625613, 1.0, 0.5, 0.0]
solPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
warpByScalar1Display.Representation = 'Surface'
warpByScalar1Display.ColorArrayName = ['POINTS', 'sol']
warpByScalar1Display.LookupTable = solLUT
warpByScalar1Display.Ambient = 0.16
warpByScalar1Display.SelectTCoordArray = 'None'
warpByScalar1Display.SelectNormalArray = 'None'
warpByScalar1Display.SelectTangentArray = 'None'
warpByScalar1Display.OSPRayScaleArray = 'sol'
warpByScalar1Display.OSPRayScaleFunction = 'PiecewiseFunction'
warpByScalar1Display.SelectOrientationVectors = 'None'
warpByScalar1Display.ScaleFactor = 0.12986113589722664
warpByScalar1Display.SelectScaleArray = 'None'
warpByScalar1Display.GlyphType = 'Arrow'
warpByScalar1Display.GlyphTableIndexArray = 'None'
warpByScalar1Display.GaussianRadius = 0.006493056794861332
warpByScalar1Display.SetScaleArray = ['POINTS', 'sol']
warpByScalar1Display.ScaleTransferFunction = 'PiecewiseFunction'
warpByScalar1Display.OpacityArray = ['POINTS', 'sol']
warpByScalar1Display.OpacityTransferFunction = 'PiecewiseFunction'
warpByScalar1Display.DataAxesGrid = 'GridAxesRepresentation'
warpByScalar1Display.PolarAxes = 'PolarAxesRepresentation'
warpByScalar1Display.ScalarOpacityFunction = solPWF
warpByScalar1Display.ScalarOpacityUnitDistance = 0.029648755685266925

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
warpByScalar1Display.ScaleTransferFunction.Points = [0.005157507725791254, 0.0, 0.5, 0.0, 0.012219478190625613, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
warpByScalar1Display.OpacityTransferFunction.Points = [0.005157507725791254, 0.0, 0.5, 0.0, 0.012219478190625613, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for solLUT in view renderView1
solLUTColorBar = GetScalarBar(solLUT, renderView1)
solLUTColorBar.WindowLocation = 'Any Location'
solLUTColorBar.Position = [0.15491100856954518, 0.16622340425531915]
solLUTColorBar.Title = ''
solLUTColorBar.ComponentTitle = ''
solLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
solLUTColorBar.TitleFontSize = 22
solLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
solLUTColorBar.LabelFontSize = 22
solLUTColorBar.RangeLabelFormat = '%2.4f'
solLUTColorBar.ScalarBarThickness = 25
solLUTColorBar.ScalarBarLength = 0.4417021276595735

# set color bar visibility
solLUTColorBar.Visibility = 1

# show color legend
warpByScalar1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(warpByScalar1)
# ----------------------------------------------------------------

myview = GetActiveView()
output_name = 'ssw_roll_wave_2d_elevate.png'
SaveScreenshot(output_name, myview, ImageResolution=[2*1517, 2*752])

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')