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
renderView1.ViewSize = [500, 80]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-4.750513061638713, 5.200798659898304, 10.873562214124133]
renderView1.CameraFocalPoint = [-4.750513061638713, 5.200798659898304, 0.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 2.8142849891224593
renderView1.UseColorPaletteForBackground = 0
renderView1.Background = [1.0, 1.0, 1.0]

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(500, 80)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Rectilinear Grid Reader'
avg0 = XMLRectilinearGridReader(registrationName='avg0*', FileName=['/Users/arpitbabbar/misc/temp/tmp_super_stiff_2d/avg000.vtr', '/Users/arpitbabbar/misc/temp/tmp_super_stiff_2d/avg001.vtr', '/Users/arpitbabbar/misc/temp/tmp_super_stiff_2d/avg002.vtr', '/Users/arpitbabbar/misc/temp/tmp_super_stiff_2d/avg003.vtr', '/Users/arpitbabbar/misc/temp/tmp_super_stiff_2d/avg004.vtr', '/Users/arpitbabbar/misc/temp/tmp_super_stiff_2d/avg005.vtr', '/Users/arpitbabbar/misc/temp/tmp_super_stiff_2d/avg006.vtr', '/Users/arpitbabbar/misc/temp/tmp_super_stiff_2d/avg007.vtr', '/Users/arpitbabbar/misc/temp/tmp_super_stiff_2d/avg008.vtr', '/Users/arpitbabbar/misc/temp/tmp_super_stiff_2d/avg009.vtr', '/Users/arpitbabbar/misc/temp/tmp_super_stiff_2d/avg010.vtr'])
avg0.PointArrayStatus = ['sol', 'rho', 'vx', 'vy', 'P11', 'P12', 'P22', 'Exact rho', 'Exact vx', 'Exact vy', 'Exact P11', 'Exact P12', 'Exact P22']
avg0.TimeArray = 'None'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from avg0
avg0Display = Show(avg0, renderView1, 'UniformGridRepresentation')

# get color transfer function/color map for 'vx'
vxLUT = GetColorTransferFunction('vx')
vxLUT.RGBPoints = [-3.999932662993491, 0.23137254902, 0.298039215686, 0.752941176471, 0.0, 0.865, 0.865, 0.865, 3.999932662993491, 0.705882352941, 0.0156862745098, 0.149019607843]
vxLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'vx'
vxPWF = GetOpacityTransferFunction('vx')
vxPWF.Points = [-3.999932662993491, 0.0, 0.5, 0.0, 3.999932662993491, 1.0, 0.5, 0.0]
vxPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
avg0Display.Representation = 'Surface'
avg0Display.ColorArrayName = ['POINTS', 'vx']
avg0Display.LookupTable = vxLUT
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
avg0Display.ScalarOpacityFunction = vxPWF
avg0Display.OpacityArrayName = ['POINTS', 'Exact P11']
avg0Display.SliceFunction = 'Plane'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
avg0Display.ScaleTransferFunction.Points = [8.999999999999998, 0.0, 0.5, 0.0, 9.001953125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
avg0Display.OpacityTransferFunction.Points = [8.999999999999998, 0.0, 0.5, 0.0, 9.001953125, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for vxLUT in view renderView1
vxLUTColorBar = GetScalarBar(vxLUT, renderView1)
vxLUTColorBar.Orientation = 'Horizontal'
vxLUTColorBar.WindowLocation = 'Any Location'
vxLUTColorBar.Position = [0.05812500000000002, 0.22950000000000004]
vxLUTColorBar.Title = ''
vxLUTColorBar.ComponentTitle = ''
vxLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
vxLUTColorBar.TitleFontSize = 20
vxLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
vxLUTColorBar.LabelFontSize = 20
vxLUTColorBar.RangeLabelFormat = '%2.1f'
vxLUTColorBar.ScalarBarLength = 0.8909999999999998

# set color bar visibility
vxLUTColorBar.Visibility = 1

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

ExportView('./tmp_2d_color_bar_vx.pdf', view=myview)

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')