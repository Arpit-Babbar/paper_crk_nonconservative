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
renderView1.ViewSize = [500, 500]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [1.0, 1.0, 0.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [2.4934495385678006, 2.466610843196875, 10000.0]
renderView1.CameraFocalPoint = [2.4934495385678006, 2.466610843196875, 0.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 2.4995671876542787
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
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
sol = XMLRectilinearGridReader(registrationName='sol*', FileName=[os.path.join(dir_path, 'shock_diffraction_results', 'sol100.vtr')])
sol.TimeArray = 'None'

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=sol)
calculator1.Function = 'sqrt(vx^2 + vy^2)/sqrt(1.4 * pressure/sol)'

# create a new 'Clip'
clip2 = Clip(registrationName='Clip2', Input=calculator1)
clip2.ClipType = 'Plane'
clip2.HyperTreeGridClipper = 'Plane'
clip2.Scalars = ['POINTS', 'pressure']
clip2.Value = 499.096465025585

# init the 'Plane' selected for 'ClipType'
clip2.ClipType.Origin = [1.0, 2.0, 0.0]
clip2.ClipType.Normal = [0.0, -1.0, 0.0]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip2.HyperTreeGridClipper.Origin = [1.0, 1.0, 0.0]

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=calculator1)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', 'pressure']
clip1.Value = 499.096465025585

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [1.0, 1.0, 0.0]
clip1.ClipType.Normal = [-1.0, 0.0, 0.0]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [1.0, 1.0, 0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from clip1
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'Result'
resultLUT = GetColorTransferFunction('Result')
resultLUT.RGBPoints = [4.5307028892689585e-18, 0.231373, 0.298039, 0.752941, 2.0867832732738867, 0.865003, 0.865003, 0.865003, 4.173566546547773, 0.705882, 0.0156863, 0.14902]
resultLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Result'
resultPWF = GetOpacityTransferFunction('Result')
resultPWF.Points = [4.5307028892689585e-18, 0.0, 0.5, 0.0, 4.173566546547773, 1.0, 0.5, 0.0]
resultPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'Result']
clip1Display.LookupTable = resultLUT
clip1Display.SelectTCoordArray = 'None'
clip1Display.SelectNormalArray = 'None'
clip1Display.SelectTangentArray = 'None'
clip1Display.OSPRayScaleArray = 'pressure'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 0.1997222694102675
clip1Display.SelectScaleArray = 'None'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'None'
clip1Display.GaussianRadius = 0.009986113470513374
clip1Display.SetScaleArray = ['POINTS', 'pressure']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'pressure']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = resultPWF
clip1Display.ScalarOpacityUnitDistance = 0.06024178439562586
clip1Display.OpacityArrayName = ['POINTS', 'pressure']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [25.774859835410588, 0.0, 0.5, 0.0, 972.4180702157595, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [25.774859835410588, 0.0, 0.5, 0.0, 972.4180702157595, 1.0, 0.5, 0.0]

# show data from clip2
clip2Display = Show(clip2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip2Display.Representation = 'Surface'
clip2Display.ColorArrayName = ['POINTS', 'Result']
clip2Display.LookupTable = resultLUT
clip2Display.SelectTCoordArray = 'None'
clip2Display.SelectNormalArray = 'None'
clip2Display.SelectTangentArray = 'None'
clip2Display.OSPRayScaleArray = 'pressure'
clip2Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip2Display.SelectOrientationVectors = 'None'
clip2Display.ScaleFactor = 0.1997222694102675
clip2Display.SelectScaleArray = 'None'
clip2Display.GlyphType = 'Arrow'
clip2Display.GlyphTableIndexArray = 'None'
clip2Display.GaussianRadius = 0.009986113470513374
clip2Display.SetScaleArray = ['POINTS', 'pressure']
clip2Display.ScaleTransferFunction = 'PiecewiseFunction'
clip2Display.OpacityArray = ['POINTS', 'pressure']
clip2Display.OpacityTransferFunction = 'PiecewiseFunction'
clip2Display.DataAxesGrid = 'GridAxesRepresentation'
clip2Display.PolarAxes = 'PolarAxesRepresentation'
clip2Display.ScalarOpacityFunction = resultPWF
clip2Display.ScalarOpacityUnitDistance = 0.05186573461749384
clip2Display.OpacityArrayName = ['POINTS', 'pressure']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip2Display.ScaleTransferFunction.Points = [54.41999565339069, 0.0, 0.5, 0.0, 972.4180702157595, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip2Display.OpacityTransferFunction.Points = [54.41999565339069, 0.0, 0.5, 0.0, 972.4180702157595, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for resultLUT in view renderView1
resultLUTColorBar = GetScalarBar(resultLUT, renderView1)
resultLUTColorBar.WindowLocation = 'Any Location'
# resultLUTColorBar.Position = [0.8119999999999999, 0.08399999999999996]
resultLUTColorBar.Title = ''
resultLUTColorBar.ComponentTitle = ''
resultLUTColorBar.RangeLabelFormat = '%2.1f'
resultLUTColorBar.LabelColor = [1.0, 1.0, 1.0]


# New one
# change scalar bar placement
resultLUTColorBar.Orientation = 'Horizontal'
resultLUTColorBar.LabelFontSize = 24
resultLUTColorBar.Position = [0.05, 0.8679999999999999]

# change scalar bar placement
resultLUTColorBar.ScalarBarLength = 0.7620000000000005

# set color bar visibility
resultLUTColorBar.Visibility = 1

# show color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# show color legend
clip2Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(clip1)
# ----------------------------------------------------------------

myview = GetActiveView()
output_filename = 'shock_diffraction_mach.png'
SaveScreenshot(output_filename, myview,
        ImageResolution=[2000, 2000])


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')