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
renderView1.ViewSize = [550, 500]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [0.5, 0.5, 0.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.5763868043674105, 0.5008296259105631, 10000.0]
renderView1.CameraFocalPoint = [0.5763868043674105, 0.5008296259105631, 0.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.5309716159373347
renderView1.UseColorPaletteForBackground = 0
renderView1.Background = [1.0, 1.0, 1.0]

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(550, 500)

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
sol100vtr = XMLRectilinearGridReader(registrationName='sol100.vtr', FileName=[os.path.join(dir_path, 'output_orszag_tang', 'sol100.vtr')])
sol100vtr.PointArrayStatus = ['rho', 'v1', 'v2', 'v3', 'p', 'B1', 'B2', 'B3', 'psi']
sol100vtr.TimeArray = 'None'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from sol100vtr
sol100vtrDisplay = Show(sol100vtr, renderView1, 'UniformGridRepresentation')

# get color transfer function/color map for 'rho'
rhoLUT = GetColorTransferFunction('rho')
rhoLUT.RGBPoints = [0.08476666622778967, 0.0, 0.0, 0.34902, 0.0975908866755802, 0.039216, 0.062745, 0.380392, 0.11041510712337074, 0.062745, 0.117647, 0.411765, 0.12323932757116128, 0.090196, 0.184314, 0.45098, 0.13606354801895182, 0.12549, 0.262745, 0.501961, 0.14888776846674234, 0.160784, 0.337255, 0.541176, 0.1617119889145329, 0.2, 0.396078, 0.568627, 0.17453620936232345, 0.239216, 0.454902, 0.6, 0.18736042981011397, 0.286275, 0.521569, 0.65098, 0.2001846502579045, 0.337255, 0.592157, 0.701961, 0.21300887070569505, 0.388235, 0.654902, 0.74902, 0.2258330911534856, 0.466667, 0.737255, 0.819608, 0.23865731160127612, 0.572549, 0.819608, 0.878431, 0.25148153204906665, 0.654902, 0.866667, 0.909804, 0.26430575249685717, 0.752941, 0.917647, 0.941176, 0.27712997294464775, 0.823529, 0.956863, 0.968627, 0.2899541933924383, 0.988235, 0.960784, 0.901961, 0.2899541933924383, 0.941176, 0.984314, 0.988235, 0.2981616944790242, 0.988235, 0.945098, 0.85098, 0.30636919556561015, 0.980392, 0.898039, 0.784314, 0.3156026342880194, 0.968627, 0.835294, 0.698039, 0.3284268547358099, 0.94902, 0.733333, 0.588235, 0.3412510751836004, 0.929412, 0.65098, 0.509804, 0.35407529563139095, 0.909804, 0.564706, 0.435294, 0.36689951607918153, 0.878431, 0.458824, 0.352941, 0.37972373652697206, 0.839216, 0.388235, 0.286275, 0.3925479569747626, 0.760784, 0.294118, 0.211765, 0.4053721774225531, 0.701961, 0.211765, 0.168627, 0.41819639787034363, 0.65098, 0.156863, 0.129412, 0.4310206183181342, 0.6, 0.094118, 0.094118, 0.44384483876592473, 0.54902, 0.066667, 0.098039, 0.45666905921371526, 0.501961, 0.05098, 0.12549, 0.46949327966150584, 0.45098, 0.054902, 0.172549, 0.48231750010929636, 0.4, 0.054902, 0.192157, 0.4951417205570869, 0.34902, 0.070588, 0.211765]
rhoLUT.ColorSpace = 'Lab'
rhoLUT.NanColor = [0.25, 0.0, 0.0]
rhoLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'rho'
rhoPWF = GetOpacityTransferFunction('rho')
rhoPWF.Points = [0.08476666622778967, 0.0, 0.5, 0.0, 0.4951417205570869, 1.0, 0.5, 0.0]
rhoPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
sol100vtrDisplay.Representation = 'Surface'
sol100vtrDisplay.ColorArrayName = ['POINTS', 'rho']
sol100vtrDisplay.LookupTable = rhoLUT
sol100vtrDisplay.SelectTCoordArray = 'None'
sol100vtrDisplay.SelectNormalArray = 'None'
sol100vtrDisplay.SelectTangentArray = 'None'
sol100vtrDisplay.OSPRayScaleArray = 'B1'
sol100vtrDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
sol100vtrDisplay.SelectOrientationVectors = 'None'
sol100vtrDisplay.ScaleFactor = 0.09994575637171643
sol100vtrDisplay.SelectScaleArray = 'B1'
sol100vtrDisplay.GlyphType = 'Arrow'
sol100vtrDisplay.GlyphTableIndexArray = 'B1'
sol100vtrDisplay.GaussianRadius = 0.004997287818585822
sol100vtrDisplay.SetScaleArray = ['POINTS', 'B1']
sol100vtrDisplay.ScaleTransferFunction = 'PiecewiseFunction'
sol100vtrDisplay.OpacityArray = ['POINTS', 'B1']
sol100vtrDisplay.OpacityTransferFunction = 'PiecewiseFunction'
sol100vtrDisplay.DataAxesGrid = 'GridAxesRepresentation'
sol100vtrDisplay.PolarAxes = 'PolarAxesRepresentation'
sol100vtrDisplay.ScalarOpacityUnitDistance = 0.013921806751357665
sol100vtrDisplay.ScalarOpacityFunction = rhoPWF
sol100vtrDisplay.OpacityArrayName = ['POINTS', 'B1']
sol100vtrDisplay.SliceFunction = 'Plane'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
sol100vtrDisplay.ScaleTransferFunction.Points = [-0.7452797075462425, 0.0, 0.5, 0.0, 0.7452797075462314, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
sol100vtrDisplay.OpacityTransferFunction.Points = [-0.7452797075462425, 0.0, 0.5, 0.0, 0.7452797075462314, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
sol100vtrDisplay.SliceFunction.Origin = [0.5, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for rhoLUT in view renderView1
rhoLUTColorBar = GetScalarBar(rhoLUT, renderView1)
rhoLUTColorBar.WindowLocation = 'Any Location'
rhoLUTColorBar.Position = [0.8745454545454546, 0.03199999999999997]
rhoLUTColorBar.Title = '$\\rho$'
rhoLUTColorBar.ComponentTitle = ''
rhoLUTColorBar.HorizontalTitle = 1
rhoLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
rhoLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
rhoLUTColorBar.RangeLabelFormat = '%2.1f'
rhoLUTColorBar.ScalarBarLength = 0.8800000000000001

# set color bar visibility
rhoLUTColorBar.Visibility = 1

# show color legend
sol100vtrDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(None)
# ----------------------------------------------------------------

myview = GetActiveView()
SaveScreenshot('./tang_density.png', myview,
        ImageResolution=[2200, 2000])

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')