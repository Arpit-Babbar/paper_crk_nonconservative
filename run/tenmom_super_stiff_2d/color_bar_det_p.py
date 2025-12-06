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
renderView1.ViewSize = [600, 80]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.11533180572257956, 13.181430463700188, 10000.0]
renderView1.CameraFocalPoint = [0.11533180572257956, 13.181430463700188, 0.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 1.7434870882563087
renderView1.UseColorPaletteForBackground = 0
renderView1.Background = [1.0, 1.0, 1.0]

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(600, 80)

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
avg0 = XMLRectilinearGridReader(registrationName='avg0*', FileName=[os.path.join(dir_path, 'tmp_super_stiff_2d_nx400', f'avg{str(i).zfill(3)}.vtr') for i in range(11)])
avg0.PointArrayStatus = ['sol', 'rho', 'vx', 'vy', 'P11', 'P12', 'P22', 'Exact rho', 'Exact vx', 'Exact vy', 'Exact P11', 'Exact P12', 'Exact P22']
avg0.TimeArray = 'None'

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=avg0)
calculator1.Function = 'P11*P22-P12^2'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from calculator1
calculator1Display = Show(calculator1, renderView1, 'UniformGridRepresentation')

# get color transfer function/color map for 'Result'
resultLUT = GetColorTransferFunction('Result')
resultLUT.RGBPoints = [24.645233096544956,
0.231373, 0.298039, 0.752941,
5472.859853760244, 0.865003, 0.865003, 0.865003, 1215334.2133777349, 0.705882, 0.0156863, 0.14902]
resultLUT.UseLogScale = 1
resultLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Result'
resultPWF = GetOpacityTransferFunction('Result')
resultPWF.Points = [24.645233096544963, 0.0, 0.5, 0.0, 1215334.2133777358, 1.0, 0.5, 0.0]
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
resultLUTColorBar.Orientation = 'Horizontal'
resultLUTColorBar.WindowLocation = 'Any Location'
resultLUTColorBar.Position = [0.1, 0.04]
resultLUTColorBar.Title = ''
resultLUTColorBar.ComponentTitle = ''
resultLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
resultLUTColorBar.TitleFontSize = 32
resultLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
resultLUTColorBar.LabelFontSize = 32
resultLUTColorBar.ScalarBarLength = 0.8

resultLUTColorBar.ScalarBarThickness = 24

# set color bar visibility
resultLUTColorBar.Visibility = 1

# Properties modified on resultLUTColorBar
resultLUTColorBar.DrawTickLabels = 0

# Properties modified on resultLUTColorBar
resultLUTColorBar.DrawTickLabels = 1
resultLUTColorBar.UseCustomLabels = 1
resultLUTColorBar.CustomLabels = [0.0]

# Properties modified on resultLUTColorBar
resultLUTColorBar.CustomLabels = [1000.0, 10000.0]

# show color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------



# ----------------------------------------------------------------
# restore active source
SetActiveSource(calculator1)
# ----------------------------------------------------------------

myview = GetActiveView()

ExportView('./tmp_2d_color_bar_det_p.pdf', view=myview)


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')