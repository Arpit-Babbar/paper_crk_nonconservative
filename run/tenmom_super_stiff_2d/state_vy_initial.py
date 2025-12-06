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
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.021054801676150363, 0.002308385154950479, 10000.0]
renderView1.CameraFocalPoint = [0.021054801676150363, 0.002308385154950479, 0.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 2.118748371006171
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
avg0 = XMLRectilinearGridReader(registrationName='avg0*', FileName=[os.path.join(dir_path, 'tmp_super_stiff_2d_nx400', f'avg{str(i).zfill(3)}.vtr') for i in range(11)])
avg0.PointArrayStatus = ['sol', 'rho', 'vx', 'vy', 'P11', 'P12', 'P22', 'Exact rho', 'Exact vx', 'Exact vy', 'Exact P11', 'Exact P12', 'Exact P22']
avg0.TimeArray = 'None'

# create a new 'Calculator'
calculator2 = Calculator(registrationName='Calculator2', Input=avg0)
calculator2.Function = 'vx*iHat + vy*jHat'

# create a new 'Glyph'
glyph1 = Glyph(registrationName='Glyph1', Input=calculator2,
    GlyphType='Arrow')
glyph1.OrientationArray = ['POINTS', 'Result']
glyph1.ScaleArray = ['POINTS', 'No scale array']
glyph1.ScaleFactor = 0.1393
glyph1.GlyphTransform = 'Transform2'
glyph1.GlyphMode = 'Uniform Spatial Distribution (Surface Sampling)'
glyph1.MaximumNumberOfSamplePoints = 1000
glyph1.Stride = 10

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from calculator2
calculator2Display = Show(calculator2, renderView1, 'UniformGridRepresentation')

# get color transfer function/color map for 'Result'
resultLUT = GetColorTransferFunction('Result')
resultLUT.RGBPoints = [-3.99993266299349, 0.23137254902, 0.298039215686, 0.752941176471, 4.440892098500626e-16, 0.865, 0.865, 0.865, 3.999932662993491, 0.705882352941, 0.0156862745098, 0.149019607843]
resultLUT.ScalarRangeInitialized = 1.0
resultLUT.VectorComponent = 1
resultLUT.VectorMode = 'Component'

# get opacity transfer function/opacity map for 'Result'
resultPWF = GetOpacityTransferFunction('Result')
resultPWF.Points = [-3.99993266299349, 0.0, 0.5, 0.0, 3.999932662993491, 1.0, 0.5, 0.0]
resultPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator2Display.Representation = 'Surface'
calculator2Display.ColorArrayName = ['POINTS', 'Result']
calculator2Display.LookupTable = resultLUT
calculator2Display.SelectTCoordArray = 'None'
calculator2Display.SelectNormalArray = 'None'
calculator2Display.SelectTangentArray = 'None'
calculator2Display.OSPRayScaleArray = 'Exact P11'
calculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator2Display.SelectOrientationVectors = 'Result'
calculator2Display.ScaleFactor = 0.398
calculator2Display.SelectScaleArray = 'Exact P11'
calculator2Display.GlyphType = 'Arrow'
calculator2Display.GlyphTableIndexArray = 'Exact P11'
calculator2Display.GaussianRadius = 0.0199
calculator2Display.SetScaleArray = ['POINTS', 'Exact P11']
calculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator2Display.OpacityArray = ['POINTS', 'Exact P11']
calculator2Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator2Display.DataAxesGrid = 'GridAxesRepresentation'
calculator2Display.PolarAxes = 'PolarAxesRepresentation'
calculator2Display.ScalarOpacityUnitDistance = 0.16513128189825013
calculator2Display.ScalarOpacityFunction = resultPWF
calculator2Display.OpacityArrayName = ['POINTS', 'Exact P11']
calculator2Display.SliceFunction = 'Plane'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator2Display.ScaleTransferFunction.Points = [8.999999999999998, 0.0, 0.5, 0.0, 9.001953125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator2Display.OpacityTransferFunction.Points = [8.999999999999998, 0.0, 0.5, 0.0, 9.001953125, 1.0, 0.5, 0.0]

# show data from glyph1
glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

# get separate color transfer function/color map for 'Result'
separate_glyph1Display_ResultLUT = GetColorTransferFunction('Result', glyph1Display, separate=True)
separate_glyph1Display_ResultLUT.AutomaticRescaleRangeMode = 'Never'
separate_glyph1Display_ResultLUT.RGBPoints = [100.0, 1.0, 1.0, 1.0, 100.015625, 0.0, 0.0, 0.0]
separate_glyph1Display_ResultLUT.ColorSpace = 'RGB'
separate_glyph1Display_ResultLUT.NanColor = [1.0, 0.0, 0.0]
separate_glyph1Display_ResultLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', 'Result']
glyph1Display.LookupTable = separate_glyph1Display_ResultLUT
glyph1Display.SelectTCoordArray = 'None'
glyph1Display.SelectNormalArray = 'None'
glyph1Display.SelectTangentArray = 'None'
glyph1Display.OSPRayScaleArray = 'Exact P11'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'Result'
glyph1Display.ScaleFactor = 0.4639666795730591
glyph1Display.SelectScaleArray = 'Exact P11'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'Exact P11'
glyph1Display.GaussianRadius = 0.023198333978652955
glyph1Display.SetScaleArray = ['POINTS', 'Exact P11']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'Exact P11']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [8.999999999999998, 0.0, 0.5, 0.0, 9.001953125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [8.999999999999998, 0.0, 0.5, 0.0, 9.001953125, 1.0, 0.5, 0.0]

# set separate color map
glyph1Display.UseSeparateColorMap = True

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get separate opacity transfer function/opacity map for 'Result'
separate_glyph1Display_ResultPWF = GetOpacityTransferFunction('Result', glyph1Display, separate=True)
separate_glyph1Display_ResultPWF.Points = [100.0, 0.0, 0.5, 0.0, 100.015625, 1.0, 0.5, 0.0]
separate_glyph1Display_ResultPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(glyph1)
# ----------------------------------------------------------------

myview = GetActiveView()
SaveScreenshot('./tmp_2d_vy_initial.png', myview,
        ImageResolution=[2000, 2000])

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')