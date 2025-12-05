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
sol.PointArrayStatus = ['sol', 'pressure', 'vx', 'vy', 'reaction_mass']
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

# get color transfer function/color map for 'sol'
solLUT = GetColorTransferFunction('sol')
solLUT.RGBPoints = [0.029002813570593526, 0.0, 0.0, 0.34902, 0.3835195047215312, 0.039216, 0.062745, 0.380392, 0.7380361958724692, 0.062745, 0.117647, 0.411765, 1.0925528870234071, 0.090196, 0.184314, 0.45098, 1.4470695781743446, 0.12549, 0.262745, 0.501961, 1.8015862693252822, 0.160784, 0.337255, 0.541176, 2.15610296047622, 0.2, 0.396078, 0.568627, 2.5106196516271586, 0.239216, 0.454902, 0.6, 2.8651363427780954, 0.286275, 0.521569, 0.65098, 3.2196530339290326, 0.337255, 0.592157, 0.701961, 3.5741697250799715, 0.388235, 0.654902, 0.74902, 3.928686416230908, 0.466667, 0.737255, 0.819608, 4.283203107381848, 0.572549, 0.819608, 0.878431, 4.637719798532783, 0.654902, 0.866667, 0.909804, 4.992236489683724, 0.752941, 0.917647, 0.941176, 5.34675318083466, 0.823529, 0.956863, 0.968627, 5.701269871985597, 0.988235, 0.960784, 0.901961, 5.701269871985597, 0.941176, 0.984314, 0.988235, 5.928160554322198, 0.988235, 0.945098, 0.85098, 6.155051236658798, 0.980392, 0.898039, 0.784314, 6.410303254287473, 0.968627, 0.835294, 0.698039, 6.764819945438412, 0.94902, 0.733333, 0.588235, 7.119336636589347, 0.929412, 0.65098, 0.509804, 7.473853327740287, 0.909804, 0.564706, 0.435294, 7.828370018891225, 0.878431, 0.458824, 0.352941, 8.18288671004216, 0.839216, 0.388235, 0.286275, 8.537403401193101, 0.760784, 0.294118, 0.211765, 8.891920092344039, 0.701961, 0.211765, 0.168627, 9.246436783494973, 0.65098, 0.156863, 0.129412, 9.600953474645916, 0.6, 0.094118, 0.094118, 9.955470165796855, 0.54902, 0.066667, 0.098039, 10.309986856947788, 0.501961, 0.05098, 0.12549, 10.664503548098727, 0.45098, 0.054902, 0.172549, 11.019020239249667, 0.4, 0.054902, 0.192157, 11.373536930400602, 0.34902, 0.070588, 0.211765]
solLUT.ColorSpace = 'Lab'
solLUT.NanColor = [0.25, 0.0, 0.0]
solLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'sol'
solPWF = GetOpacityTransferFunction('sol')
solPWF.Points = [0.029002813570593526, 0.0, 0.5, 0.0, 11.373536930400602, 1.0, 0.5, 0.0]
solPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'sol']
clip1Display.LookupTable = solLUT
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
clip1Display.ScalarOpacityFunction = solPWF
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
clip2Display.ColorArrayName = ['POINTS', 'sol']
clip2Display.LookupTable = solLUT
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
clip2Display.ScalarOpacityFunction = solPWF
clip2Display.ScalarOpacityUnitDistance = 0.05186573461749384
clip2Display.OpacityArrayName = ['POINTS', 'pressure']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip2Display.ScaleTransferFunction.Points = [54.41999565339069, 0.0, 0.5, 0.0, 972.4180702157595, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip2Display.OpacityTransferFunction.Points = [54.41999565339069, 0.0, 0.5, 0.0, 972.4180702157595, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for solLUT in view renderView1
solLUTColorBar = GetScalarBar(solLUT, renderView1)
solLUTColorBar.WindowLocation = 'Any Location'
solLUTColorBar.Title = ''
solLUTColorBar.ComponentTitle = ''
solLUTColorBar.RangeLabelFormat = '%2.2f'


# New one
# change scalar bar placement
solLUTColorBar.Orientation = 'Horizontal'
solLUTColorBar.LabelFontSize = 24
solLUTColorBar.Position = [0.05, 0.8679999999999999]

solLUTColorBar.LabelColor = [1.0, 1.0, 1.0]

# change scalar bar placement
solLUTColorBar.ScalarBarLength = 0.7620000000000005

# set color bar visibility
solLUTColorBar.Visibility = 1

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
SetActiveSource(None)
# ----------------------------------------------------------------

myview = GetActiveView()
output_filename = 'shock_diffraction_density.png'
SaveScreenshot(output_filename, myview,
        ImageResolution=[2000, 2000])

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')