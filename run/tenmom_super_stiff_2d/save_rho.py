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
renderView1.ViewSize = [600, 600]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-0.14684774835556558, 0.04086357859170551, 10000.0]
renderView1.CameraFocalPoint = [-0.14684774835556558, 0.04086357859170551, 0.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 1.8385832971541163
renderView1.UseColorPaletteForBackground = 0
renderView1.Background = [1.0, 1.0, 1.0]

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

# create a new 'XML Rectilinear Grid Reader'
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
sol0 = XMLRectilinearGridReader(registrationName='sol0*', FileName=[os.path.join(dir_path, 'output_tmp_super_stiff_2d', 'sol000.vtr'), os.path.join(dir_path, 'output_tmp_super_stiff_2d', 'sol001.vtr'), os.path.join(dir_path, 'output_tmp_super_stiff_2d', 'sol002.vtr'), os.path.join(dir_path, 'output_tmp_super_stiff_2d', 'sol003.vtr'), os.path.join(dir_path, 'output_tmp_super_stiff_2d', 'sol004.vtr'), os.path.join(dir_path, 'output_tmp_super_stiff_2d', 'sol005.vtr'), os.path.join(dir_path, 'output_tmp_super_stiff_2d', 'sol006.vtr'), os.path.join(dir_path, 'output_tmp_super_stiff_2d', 'sol007.vtr'), os.path.join(dir_path, 'output_tmp_super_stiff_2d', 'sol008.vtr'), os.path.join(dir_path, 'output_tmp_super_stiff_2d', 'sol009.vtr'), os.path.join(dir_path, 'output_tmp_super_stiff_2d', 'sol010.vtr')])
sol0.PointArrayStatus = ['sol', 'rho', 'vx', 'vy', 'P11', 'P12', 'P22', 'Exact rho', 'Exact vx', 'Exact vy', 'Exact P11', 'Exact P12', 'Exact P22']
sol0.TimeArray = 'None'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from sol0
sol0Display = Show(sol0, renderView1, 'UniformGridRepresentation')

# get color transfer function/color map for 'sol'
solLUT = GetColorTransferFunction('sol')
solLUT.RGBPoints = [0.0036281049925972367, 0.0, 0.0, 0.34902, 0.06030073996324175, 0.039216, 0.062745, 0.380392, 0.11697337493388626, 0.062745, 0.117647, 0.411765, 0.1736460099045308, 0.090196, 0.184314, 0.45098, 0.2303186448751753, 0.12549, 0.262745, 0.501961, 0.28699127984581985, 0.160784, 0.337255, 0.541176, 0.34366391481646436, 0.2, 0.396078, 0.568627, 0.40033654978710886, 0.239216, 0.454902, 0.6, 0.4570091847577534, 0.286275, 0.521569, 0.65098, 0.5136818197283979, 0.337255, 0.592157, 0.701961, 0.5703544546990424, 0.388235, 0.654902, 0.74902, 0.6270270896696869, 0.466667, 0.737255, 0.819608, 0.6836997246403315, 0.572549, 0.819608, 0.878431, 0.7403723596109759, 0.654902, 0.866667, 0.909804, 0.7970449945816205, 0.752941, 0.917647, 0.941176, 0.8537176295522649, 0.823529, 0.956863, 0.968627, 0.9103902645229095, 0.988235, 0.960784, 0.901961, 0.9103902645229095, 0.941176, 0.984314, 0.988235, 0.946660750904122, 0.988235, 0.945098, 0.85098, 0.9829312372853345, 0.980392, 0.898039, 0.784314, 1.0237355344641985, 0.968627, 0.835294, 0.698039, 1.080408169434843, 0.94902, 0.733333, 0.588235, 1.1370808044054876, 0.929412, 0.65098, 0.509804, 1.193753439376132, 0.909804, 0.564706, 0.435294, 1.2504260743467766, 0.878431, 0.458824, 0.352941, 1.3070987093174211, 0.839216, 0.388235, 0.286275, 1.3637713442880657, 0.760784, 0.294118, 0.211765, 1.4204439792587102, 0.701961, 0.211765, 0.168627, 1.4771166142293546, 0.65098, 0.156863, 0.129412, 1.5337892491999991, 0.6, 0.094118, 0.094118, 1.5904618841706437, 0.54902, 0.066667, 0.098039, 1.6471345191412883, 0.501961, 0.05098, 0.12549, 1.7038071541119326, 0.45098, 0.054902, 0.172549, 1.7604797890825772, 0.4, 0.054902, 0.192157, 1.8171524240532217, 0.34902, 0.070588, 0.211765]
solLUT.ColorSpace = 'Lab'
solLUT.NanColor = [0.25, 0.0, 0.0]
solLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'sol'
solPWF = GetOpacityTransferFunction('sol')
solPWF.Points = [0.0036281049925972367, 0.0, 0.5, 0.0, 1.8171524240532217, 1.0, 0.5, 0.0]
solPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
sol0Display.Representation = 'Surface'
sol0Display.ColorArrayName = ['POINTS', 'sol']
sol0Display.LookupTable = solLUT
sol0Display.SelectTCoordArray = 'None'
sol0Display.SelectNormalArray = 'None'
sol0Display.SelectTangentArray = 'None'
sol0Display.OSPRayScaleArray = 'Exact P11'
sol0Display.OSPRayScaleFunction = 'PiecewiseFunction'
sol0Display.SelectOrientationVectors = 'None'
sol0Display.ScaleFactor = 0.398
sol0Display.SelectScaleArray = 'Exact P11'
sol0Display.GlyphType = 'Arrow'
sol0Display.GlyphTableIndexArray = 'Exact P11'
sol0Display.GaussianRadius = 0.0199
sol0Display.SetScaleArray = ['POINTS', 'Exact P11']
sol0Display.ScaleTransferFunction = 'PiecewiseFunction'
sol0Display.OpacityArray = ['POINTS', 'Exact P11']
sol0Display.OpacityTransferFunction = 'PiecewiseFunction'
sol0Display.DataAxesGrid = 'GridAxesRepresentation'
sol0Display.PolarAxes = 'PolarAxesRepresentation'
sol0Display.ScalarOpacityUnitDistance = 0.16513128189825013
sol0Display.ScalarOpacityFunction = solPWF
sol0Display.OpacityArrayName = ['POINTS', 'Exact P11']
sol0Display.SliceFunction = 'Plane'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
sol0Display.ScaleTransferFunction.Points = [8.999999999999998, 0.0, 0.5, 0.0, 9.001953125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
sol0Display.OpacityTransferFunction.Points = [8.999999999999998, 0.0, 0.5, 0.0, 9.001953125, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for solLUT in view renderView1
solLUTColorBar = GetScalarBar(solLUT, renderView1)
solLUTColorBar.WindowLocation = 'Any Location'
solLUTColorBar.Position = [0.01288659793814433, 0.08014241210502894]
solLUTColorBar.Title = ''
solLUTColorBar.ComponentTitle = ''
solLUTColorBar.TitleFontSize = 20
solLUTColorBar.LabelFontSize = 20
solLUTColorBar.RangeLabelFormat = '%2.3f'
solLUTColorBar.ScalarBarLength = 0.8653805073431239

# set color bar visibility
solLUTColorBar.Visibility = 1

# show color legend
sol0Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(None)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')