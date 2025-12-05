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

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
# create a new 'XML Rectilinear Grid Reader'
sol100vtr = XMLRectilinearGridReader(registrationName='sol100.vtr', FileName=[os.path.join(dir_path, 'output_orszag_tang', 'sol100.vtr')])
sol100vtr.PointArrayStatus = ['rho', 'v1', 'v2', 'v3', 'p', 'B1', 'B2', 'B3', 'psi']
sol100vtr.TimeArray = 'None'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from sol100vtr
sol100vtrDisplay = Show(sol100vtr, renderView1, 'UniformGridRepresentation')

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')
pLUT.RGBPoints = [0.02670363718528087, 0.0, 0.0, 0.34902, 0.04249380830182982, 0.039216, 0.062745, 0.380392, 0.05828397941837877, 0.062745, 0.117647, 0.411765, 0.07407415053492772, 0.090196, 0.184314, 0.45098, 0.08986432165147668, 0.12549, 0.262745, 0.501961, 0.10565449276802563, 0.160784, 0.337255, 0.541176, 0.12144466388457456, 0.2, 0.396078, 0.568627, 0.13723483500112352, 0.239216, 0.454902, 0.6, 0.15302500611767247, 0.286275, 0.521569, 0.65098, 0.16881517723422143, 0.337255, 0.592157, 0.701961, 0.1846053483507704, 0.388235, 0.654902, 0.74902, 0.20039551946731932, 0.466667, 0.737255, 0.819608, 0.21618569058386827, 0.572549, 0.819608, 0.878431, 0.23197586170041723, 0.654902, 0.866667, 0.909804, 0.24776603281696616, 0.752941, 0.917647, 0.941176, 0.2635562039335151, 0.823529, 0.956863, 0.968627, 0.27934637505006404, 0.988235, 0.960784, 0.901961, 0.27934637505006404, 0.941176, 0.984314, 0.988235, 0.2894520845646554, 0.988235, 0.945098, 0.85098, 0.2995577940792467, 0.980392, 0.898039, 0.784314, 0.31092671728316196, 0.968627, 0.835294, 0.698039, 0.3267168883997109, 0.94902, 0.733333, 0.588235, 0.34250705951625987, 0.929412, 0.65098, 0.509804, 0.35829723063280877, 0.909804, 0.564706, 0.435294, 0.37408740174935773, 0.878431, 0.458824, 0.352941, 0.3898775728659067, 0.839216, 0.388235, 0.286275, 0.40566774398245564, 0.760784, 0.294118, 0.211765, 0.4214579150990046, 0.701961, 0.211765, 0.168627, 0.43724808621555356, 0.65098, 0.156863, 0.129412, 0.4530382573321025, 0.6, 0.094118, 0.094118, 0.4688284284486514, 0.54902, 0.066667, 0.098039, 0.48461859956520037, 0.501961, 0.05098, 0.12549, 0.5004087706817494, 0.45098, 0.054902, 0.172549, 0.5161989417982983, 0.4, 0.054902, 0.192157, 0.5319891129148473, 0.34902, 0.070588, 0.211765]
pLUT.ColorSpace = 'Lab'
pLUT.NanColor = [0.25, 0.0, 0.0]
pLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')
pPWF.Points = [0.02670363718528087, 0.0, 0.5, 0.0, 0.5319891129148473, 1.0, 0.5, 0.0]
pPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
sol100vtrDisplay.Representation = 'Surface'
sol100vtrDisplay.ColorArrayName = ['POINTS', 'p']
sol100vtrDisplay.LookupTable = pLUT
sol100vtrDisplay.SelectTCoordArray = 'None'
sol100vtrDisplay.SelectNormalArray = 'None'
sol100vtrDisplay.SelectTangentArray = 'None'
sol100vtrDisplay.OSPRayScaleArray = 'B1'
sol100vtrDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
sol100vtrDisplay.SelectOrientationVectors = 'None'
sol100vtrDisplay.ScaleFactor = 0.0999542340711896
sol100vtrDisplay.SelectScaleArray = 'B1'
sol100vtrDisplay.GlyphType = 'Arrow'
sol100vtrDisplay.GlyphTableIndexArray = 'B1'
sol100vtrDisplay.GaussianRadius = 0.00499771170355948
sol100vtrDisplay.SetScaleArray = ['POINTS', 'B1']
sol100vtrDisplay.ScaleTransferFunction = 'PiecewiseFunction'
sol100vtrDisplay.OpacityArray = ['POINTS', 'B1']
sol100vtrDisplay.OpacityTransferFunction = 'PiecewiseFunction'
sol100vtrDisplay.DataAxesGrid = 'GridAxesRepresentation'
sol100vtrDisplay.PolarAxes = 'PolarAxesRepresentation'
sol100vtrDisplay.ScalarOpacityUnitDistance = 0.013913921719800347
sol100vtrDisplay.ScalarOpacityFunction = pPWF
sol100vtrDisplay.OpacityArrayName = ['POINTS', 'B1']
sol100vtrDisplay.SliceFunction = 'Plane'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
sol100vtrDisplay.ScaleTransferFunction.Points = [-0.7397262148667599, 0.0, 0.5, 0.0, 0.7397262148670037, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
sol100vtrDisplay.OpacityTransferFunction.Points = [-0.7397262148667599, 0.0, 0.5, 0.0, 0.7397262148670037, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
sol100vtrDisplay.SliceFunction.Origin = [0.5, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for pLUT in view renderView1
pLUTColorBar = GetScalarBar(pLUT, renderView1)
pLUTColorBar.WindowLocation = 'Any Location'
pLUTColorBar.Position = [0.8781818181818181, 0.029999999999999943]
pLUTColorBar.Title = '$p$'
pLUTColorBar.ComponentTitle = ''
pLUTColorBar.HorizontalTitle = 1
pLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
pLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
pLUTColorBar.RangeLabelFormat = '%2.2f'
pLUTColorBar.ScalarBarLength = 0.8720000000000004

# set color bar visibility
pLUTColorBar.Visibility = 1

# show color legend
sol100vtrDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(sol100vtr)
# ----------------------------------------------------------------

myview = GetActiveView()
SaveScreenshot('./tang_pressure.png', myview,
        ImageResolution=[2200, 2000])

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')