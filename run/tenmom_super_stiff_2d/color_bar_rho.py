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
renderView1.ViewSize = [550, 80]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.31776887857213176, 4.571351292623838, 10000.0]
renderView1.CameraFocalPoint = [0.31776887857213176, 4.571351292623838, 0.0]
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
layout1.SetSize(550, 80)

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

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from avg0
avg0Display = Show(avg0, renderView1, 'UniformGridRepresentation')

# get color transfer function/color map for 'sol'
solLUT = GetColorTransferFunction('sol')
solLUT.RGBPoints = [0.0036281049925972367, 0.23137254902, 0.298039215686, 0.752941176471, 0.9103902645229095, 0.865, 0.865, 0.865, 1.8171524240532217, 0.705882352941, 0.0156862745098, 0.149019607843]
solLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'sol'
solPWF = GetOpacityTransferFunction('sol')
solPWF.Points = [0.0036281049925972367, 0.0, 0.5, 0.0, 1.8171524240532217, 1.0, 0.5, 0.0]
solPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
avg0Display.Representation = 'Surface'
avg0Display.ColorArrayName = ['POINTS', 'sol']
avg0Display.LookupTable = solLUT
avg0Display.SelectTCoordArray = 'None'
avg0Display.SelectNormalArray = 'None'
avg0Display.SelectTangentArray = 'None'
avg0Display.OSPRayScaleArray = 'Exact P11'
avg0Display.OSPRayScaleFunction = 'PiecewiseFunction'
avg0Display.SelectOrientationVectors = 'None'
avg0Display.ScaleFactor = 0.398
avg0Display.SelectScaleArray = 'Exact P11'
avg0Display.GlyphType = 'Arrow'
avg0Display.GlyphTableIndexArray = 'Exact P11'
avg0Display.GaussianRadius = 0.0199
avg0Display.SetScaleArray = ['POINTS', 'Exact P11']
avg0Display.ScaleTransferFunction = 'PiecewiseFunction'
avg0Display.OpacityArray = ['POINTS', 'Exact P11']
avg0Display.OpacityTransferFunction = 'PiecewiseFunction'
avg0Display.DataAxesGrid = 'GridAxesRepresentation'
avg0Display.PolarAxes = 'PolarAxesRepresentation'
avg0Display.ScalarOpacityUnitDistance = 0.16513128189825013
avg0Display.ScalarOpacityFunction = solPWF
avg0Display.OpacityArrayName = ['POINTS', 'Exact P11']
avg0Display.SliceFunction = 'Plane'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
avg0Display.ScaleTransferFunction.Points = [8.999999999999998, 0.0, 0.5, 0.0, 9.001953125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
avg0Display.OpacityTransferFunction.Points = [8.999999999999998, 0.0, 0.5, 0.0, 9.001953125, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for solLUT in view renderView1
solLUTColorBar = GetScalarBar(solLUT, renderView1)
solLUTColorBar.Orientation = 'Horizontal'
solLUTColorBar.WindowLocation = 'Any Location'
solLUTColorBar.Position = [0.0506460481099657, 0.14]
solLUTColorBar.Title = ''
solLUTColorBar.ComponentTitle = ''
solLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
solLUTColorBar.TitleFontSize = 28
solLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
solLUTColorBar.LabelFontSize = 28
solLUTColorBar.RangeLabelFormat = '%2.1f'
solLUTColorBar.ScalarBarLength = 0.9005763836317837

# set color bar visibility
solLUTColorBar.Visibility = 1

# show color legend
avg0Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(avg0)
# ----------------------------------------------------------------

myview = GetActiveView()

ExportView('./tmp_2d_color_bar_rho.pdf', view=myview)

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')