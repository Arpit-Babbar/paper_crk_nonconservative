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
renderView1.ViewSize = [300, 550]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [0.5, 0.0, 0.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.50106660241838, -0.007221253600899848, 10000.0]
renderView1.CameraFocalPoint = [0.50106660241838, -0.007221253600899848, 0.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.9186119650757256
renderView1.UseColorPaletteForBackground = 0
renderView1.Background = [1.0, 1.0, 1.0]

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(300, 550)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Rectilinear Grid Reader'

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_no', type=str, default='000')
args = parser.parse_args()

input_no = args.input_no
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(dir_path, 'output_khi_64_N3_amax0.3', f'sol{input_no}.vtr')
# input_file = f'./output_khi_64_N3_amax0.3/sol{input_no}.vtr'
# create a new 'XML Rectilinear Grid Reader'
sol = XMLRectilinearGridReader(registrationName='sol0*', FileName=[input_file])

# sol = XMLRectilinearGridReader(registrationName='sol*', FileName=['/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol000.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol001.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol002.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol003.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol004.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol005.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol006.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol007.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol008.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol009.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol010.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol011.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol012.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol013.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol014.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol015.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol016.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol017.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol018.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol019.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol020.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol021.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol022.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol023.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol024.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol025.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol026.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol027.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol028.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol029.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol030.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol031.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol032.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol033.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol034.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol035.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol036.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol037.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol038.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol039.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol040.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol041.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol042.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol043.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol044.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol045.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol046.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol047.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol048.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol049.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol050.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol051.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol052.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol053.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol054.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol055.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol056.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol057.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol058.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol059.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol060.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol061.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol062.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol063.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol064.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol065.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol066.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol067.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol068.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol069.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol070.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol071.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol072.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol073.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol074.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol075.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol076.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol077.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol078.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol079.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol080.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol081.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol082.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol083.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol084.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol085.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol086.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol087.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol088.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol089.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol090.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol091.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol092.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol093.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol094.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol095.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol096.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol097.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol098.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol099.vtr', '/Users/arpitbabbar/repositories/paper_crk_noncons/run/khi/output_khi_64_N3/sol100.vtr'])
sol.PointArrayStatus = ['B1', 'B2', 'B3', 'rho_1', 'v1_1', 'v2_1', 'v3_1', 'p_1', 'rho_2', 'v1_2', 'v2_2', 'v3_2', 'p_2', 'psi']
sol.TimeArray = 'None'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from sol
solDisplay = Show(sol, renderView1, 'UniformGridRepresentation')

# get color transfer function/color map for 'rho_1'
rho_1LUT = GetColorTransferFunction('rho_1')
rho_1LUT.RGBPoints = [0.38906524114414304, 0.001462, 0.000466, 0.013866, 0.3897104260189053, 0.002267, 0.00127, 0.01857, 0.39035544638962, 0.003299, 0.002249, 0.024239, 0.39100063126438234, 0.004547, 0.003392, 0.030909, 0.391645651635097, 0.006006, 0.004692, 0.038558, 0.3922908365098593, 0.007676, 0.006136, 0.046836, 0.392935856880574, 0.009561, 0.007713, 0.055143, 0.39358104175533626, 0.011663, 0.009417, 0.06346, 0.39422622663009854, 0.013995, 0.011225, 0.071862, 0.3948712470008132, 0.016561, 0.013136, 0.080282, 0.39551643187557556, 0.019373, 0.015133, 0.088767, 0.39616145224629024, 0.022447, 0.017199, 0.097327, 0.3968066371210525, 0.025793, 0.019331, 0.10593, 0.3974516574917672, 0.029432, 0.021503, 0.114621, 0.3980968423665295, 0.033385, 0.023702, 0.123397, 0.3987420272412918, 0.037668, 0.025921, 0.132232, 0.3993870476120065, 0.042253, 0.028139, 0.141141, 0.4000322324867688, 0.046915, 0.030324, 0.150164, 0.40067725285748346, 0.051644, 0.032474, 0.159254, 0.40132243773224574, 0.056449, 0.034569, 0.168414, 0.4019674581029604, 0.06134, 0.03659, 0.177642, 0.4026126429777227, 0.066331, 0.038504, 0.186962, 0.40325782785248504, 0.071429, 0.040294, 0.196354, 0.4039028482231997, 0.076637, 0.041905, 0.205799, 0.404548033097962, 0.081962, 0.043328, 0.215289, 0.4051930534686767, 0.087411, 0.044556, 0.224813, 0.40583823834343896, 0.09299, 0.045583, 0.234358, 0.40648325871415364, 0.098702, 0.046402, 0.243904, 0.407128443588916, 0.104551, 0.047008, 0.25343, 0.40777346395963066, 0.110536, 0.047399, 0.262912, 0.40841864883439294, 0.116656, 0.047574, 0.272321, 0.4090638337091552, 0.122908, 0.047536, 0.281624, 0.40970885407986996, 0.129285, 0.047293, 0.290788, 0.41035403895463224, 0.135778, 0.046856, 0.299776, 0.4109990593253469, 0.142378, 0.046242, 0.308553, 0.4116442442001092, 0.149073, 0.045468, 0.317085, 0.4122892645708239, 0.15585, 0.044559, 0.325338, 0.41293444944558616, 0.162689, 0.043554, 0.333277, 0.41357963432034844, 0.169575, 0.042489, 0.340874, 0.4142246546910631, 0.176493, 0.041402, 0.348111, 0.41486983956582546, 0.183429, 0.040329, 0.354971, 0.41551485993654014, 0.190367, 0.039309, 0.361447, 0.4161600448113024, 0.197297, 0.0384, 0.367535, 0.4168050651820171, 0.204209, 0.037632, 0.373238, 0.41745025005677944, 0.211095, 0.03703, 0.378563, 0.4180954349315417, 0.217949, 0.036615, 0.383522, 0.4187404553022564, 0.224763, 0.036405, 0.388129, 0.4193856401770187, 0.231538, 0.036405, 0.3924, 0.42003066054773336, 0.238273, 0.036621, 0.396353, 0.42067584542249564, 0.244967, 0.037055, 0.400007, 0.4213208657932103, 0.25162, 0.037705, 0.403378, 0.4219660506679726, 0.258234, 0.038571, 0.406485, 0.42261123554273494, 0.26481, 0.039647, 0.409345, 0.4232562559134496, 0.271347, 0.040922, 0.411976, 0.4239014407882119, 0.27785, 0.042353, 0.414392, 0.4245464611589266, 0.284321, 0.043933, 0.416608, 0.4251916460336889, 0.290763, 0.045644, 0.418637, 0.4258366664044036, 0.297178, 0.04747, 0.420491, 0.4264818512791659, 0.303568, 0.049396, 0.422182, 0.42712703615392816, 0.309935, 0.051407, 0.423721, 0.42777205652464284, 0.316282, 0.05349, 0.425116, 0.4284172413994051, 0.32261, 0.055634, 0.426377, 0.42906226177011986, 0.328921, 0.057827, 0.427511, 0.42970744664488214, 0.335217, 0.06006, 0.428524, 0.4303524670155968, 0.3415, 0.062325, 0.429425, 0.4309976518903591, 0.347771, 0.064616, 0.430217, 0.4316428367651214, 0.354032, 0.066925, 0.430906, 0.43228785713583606, 0.360284, 0.069247, 0.431497, 0.4329330420105984, 0.366529, 0.071579, 0.431994, 0.433578062381313, 0.372768, 0.073915, 0.4324, 0.43422324725607536, 0.379001, 0.076253, 0.432719, 0.43486826762679004, 0.385228, 0.078591, 0.432955, 0.4355134525015523, 0.391453, 0.080927, 0.433109, 0.4361586373763146, 0.397674, 0.083257, 0.433183, 0.43680365774702934, 0.403894, 0.08558, 0.433179, 0.43744884262179157, 0.410113, 0.087896, 0.433098, 0.4380938629925063, 0.416331, 0.090203, 0.432943, 0.4387390478672686, 0.422549, 0.092501, 0.432714, 0.43938406823798326, 0.428768, 0.09479, 0.432412, 0.44002925311274554, 0.434987, 0.097069, 0.432039, 0.4406742734834602, 0.441207, 0.099338, 0.431594, 0.44131945835822256, 0.447428, 0.101597, 0.43108, 0.44196464323298484, 0.453651, 0.103848, 0.430498, 0.4426096636036995, 0.459875, 0.106089, 0.429846, 0.44325484847846186, 0.4661, 0.108322, 0.429125, 0.4438998688491765, 0.472328, 0.110547, 0.428334, 0.4445450537239388, 0.478558, 0.112764, 0.427475, 0.4451900740946535, 0.484789, 0.114974, 0.426548, 0.4458352589694158, 0.491022, 0.117179, 0.425552, 0.44648044384417807, 0.497257, 0.119379, 0.424488, 0.44712546421489274, 0.503493, 0.121575, 0.423356, 0.447770649089655, 0.50973, 0.123769, 0.422156, 0.4484156694603697, 0.515967, 0.12596, 0.420887, 0.449060854335132, 0.522206, 0.12815, 0.419549, 0.4497058747058467, 0.528444, 0.130341, 0.418142, 0.450351059580609, 0.534683, 0.132534, 0.416667, 0.4509962444553713, 0.54092, 0.134729, 0.415123, 0.451641264826086, 0.547157, 0.136929, 0.413511, 0.4522864497008483, 0.553392, 0.139134, 0.411829, 0.452931470071563, 0.559624, 0.141346, 0.410078, 0.45357665494632526, 0.565854, 0.143567, 0.408258, 0.45422167531703994, 0.572081, 0.145797, 0.406369, 0.4548668601918022, 0.578304, 0.148039, 0.404411, 0.4555120450665645, 0.584521, 0.150294, 0.402385, 0.4561570654372792, 0.590734, 0.152563, 0.40029, 0.4568022503120415, 0.59694, 0.154848, 0.398125, 0.45744727068275615, 0.603139, 0.157151, 0.395891, 0.4580924555575185, 0.60933, 0.159474, 0.393589, 0.45873747592823316, 0.615513, 0.161817, 0.391219, 0.4593826608029955, 0.621685, 0.164184, 0.388781, 0.4600278456777578, 0.627847, 0.166575, 0.386276, 0.46067286604847246, 0.633998, 0.168992, 0.383704, 0.46131805092323475, 0.640135, 0.171438, 0.381065, 0.4619630712939494, 0.64626, 0.173914, 0.378359, 0.4626082561687117, 0.652369, 0.176421, 0.375586, 0.4632532765394264, 0.658463, 0.178962, 0.372748, 0.46389846141418867, 0.66454, 0.181539, 0.369846, 0.464543646288951, 0.670599, 0.184153, 0.366879, 0.4651886666596657, 0.676638, 0.186807, 0.363849, 0.46583385153442797, 0.682656, 0.189501, 0.360757, 0.46647887190514264, 0.688653, 0.192239, 0.357603, 0.467124056779905, 0.694627, 0.195021, 0.354388, 0.4677690771506196, 0.700576, 0.197851, 0.351113, 0.46841426202538194, 0.7065, 0.200728, 0.347777, 0.46905944690014423, 0.712396, 0.203656, 0.344383, 0.4697044672708589, 0.718264, 0.206636, 0.340931, 0.4703496521456212, 0.724103, 0.20967, 0.337424, 0.47099467251633587, 0.729909, 0.212759, 0.333861, 0.47163985739109815, 0.735683, 0.215906, 0.330245, 0.4722848777618129, 0.741423, 0.219112, 0.326576, 0.47293006263657517, 0.747127, 0.222378, 0.322856, 0.47357508300728984, 0.752794, 0.225706, 0.319085, 0.4742202678820521, 0.758422, 0.229097, 0.315266, 0.4748654527568144, 0.76401, 0.232554, 0.311399, 0.47551047312752914, 0.769556, 0.236077, 0.307485, 0.4761556580022914, 0.775059, 0.239667, 0.303526, 0.4768006783730061, 0.780517, 0.243327, 0.299523, 0.4774458632477684, 0.785929, 0.247056, 0.295477, 0.47809088361848306, 0.791293, 0.250856, 0.29139, 0.4787360684932454, 0.796607, 0.254728, 0.287264, 0.47938125336800763, 0.801871, 0.258674, 0.283099, 0.48002627373872236, 0.807082, 0.262692, 0.278898, 0.48067145861348465, 0.812239, 0.266786, 0.274661, 0.48131647898419927, 0.817341, 0.270954, 0.27039, 0.4819616638589616, 0.822386, 0.275197, 0.266085, 0.4826066842296763, 0.827372, 0.279517, 0.26175, 0.48325186910443857, 0.832299, 0.283913, 0.257383, 0.4838970539792009, 0.837165, 0.288385, 0.252988, 0.4845420743499156, 0.841969, 0.292933, 0.248564, 0.48518725922467787, 0.846709, 0.297559, 0.244113, 0.48583227959539255, 0.851384, 0.30226, 0.239636, 0.4864774644701549, 0.855992, 0.307038, 0.235133, 0.48712248484086956, 0.860533, 0.311892, 0.230606, 0.4877676697156318, 0.865006, 0.316822, 0.226055, 0.4884128545903941, 0.869409, 0.321827, 0.221482, 0.48905787496110886, 0.873741, 0.326906, 0.216886, 0.4897030598358711, 0.878001, 0.33206, 0.212268, 0.49034808020658577, 0.882188, 0.337287, 0.207628, 0.4909932650813481, 0.886302, 0.342586, 0.202968, 0.4916382854520628, 0.890341, 0.347957, 0.198286, 0.49228347032682507, 0.894305, 0.353399, 0.193584, 0.49292865520158735, 0.898192, 0.358911, 0.18886, 0.49357367557230203, 0.902003, 0.364492, 0.184116, 0.4942188604470643, 0.905735, 0.37014, 0.17935, 0.494863880817779, 0.90939, 0.375856, 0.174563, 0.49550906569254133, 0.912966, 0.381636, 0.169755, 0.49615408606325595, 0.916462, 0.387481, 0.164924, 0.4967992709380183, 0.919879, 0.393389, 0.16007, 0.4974444558127806, 0.923215, 0.399359, 0.155193, 0.49808947618349525, 0.92647, 0.405389, 0.150292, 0.4987346610582576, 0.929644, 0.411479, 0.145367, 0.49937968142897227, 0.932737, 0.417627, 0.140417, 0.5000248663037345, 0.935747, 0.423831, 0.13544, 0.5006698866744492, 0.938675, 0.430091, 0.130438, 0.5013150715492115, 0.941521, 0.436405, 0.125409, 0.5019602564239738, 0.944285, 0.442772, 0.120354, 0.5026052767946885, 0.946965, 0.449191, 0.115272, 0.5032504616694509, 0.949562, 0.45566, 0.110164, 0.5038954820401654, 0.952075, 0.462178, 0.105031, 0.5045406669149278, 0.954506, 0.468744, 0.099874, 0.5051856872856424, 0.956852, 0.475356, 0.094695, 0.5058308721604048, 0.959114, 0.482014, 0.089499, 0.5064758925311195, 0.961293, 0.488716, 0.084289, 0.5071210774058817, 0.963387, 0.495462, 0.079073, 0.507766262280644, 0.965397, 0.502249, 0.073859, 0.5084112826513587, 0.967322, 0.509078, 0.068659, 0.509056467526121, 0.969163, 0.515946, 0.063488, 0.5097014878968357, 0.970919, 0.522853, 0.058367, 0.510346672771598, 0.97259, 0.529798, 0.053324, 0.5109916931423126, 0.974176, 0.53678, 0.048392, 0.511636878017075, 0.975677, 0.543798, 0.043618, 0.5122820628918372, 0.977092, 0.55085, 0.03905, 0.512927083262552, 0.978422, 0.557937, 0.034931, 0.5135722681373143, 0.979666, 0.565057, 0.031409, 0.514217288508029, 0.980824, 0.572209, 0.028508, 0.5148624733827912, 0.981895, 0.579392, 0.02625, 0.5155074937535059, 0.982881, 0.586606, 0.024661, 0.5161526786282682, 0.983779, 0.593849, 0.02377, 0.5167978635030306, 0.984591, 0.601122, 0.023606, 0.5174428838737452, 0.985315, 0.608422, 0.024202, 0.5180880687485074, 0.985952, 0.61575, 0.025592, 0.5187330891192221, 0.986502, 0.623105, 0.027814, 0.5193782739939845, 0.986964, 0.630485, 0.030908, 0.5200232943646992, 0.987337, 0.63789, 0.034916, 0.5206684792394614, 0.987622, 0.64532, 0.039886, 0.5213136641142238, 0.987819, 0.652773, 0.045581, 0.5219586844849384, 0.987926, 0.66025, 0.05175, 0.5226038693597007, 0.987945, 0.667748, 0.058329, 0.5232488897304154, 0.987874, 0.675267, 0.065257, 0.5238940746051777, 0.987714, 0.682807, 0.072489, 0.5245390949758924, 0.987464, 0.690366, 0.07999, 0.5251842798506547, 0.987124, 0.697944, 0.087731, 0.525829464725417, 0.986694, 0.70554, 0.095694, 0.5264744850961316, 0.986175, 0.713153, 0.103863, 0.5271196699708939, 0.985566, 0.720782, 0.112229, 0.5277646903416087, 0.984865, 0.728427, 0.120785, 0.528409875216371, 0.984075, 0.736087, 0.129527, 0.5290548955870855, 0.983196, 0.743758, 0.138453, 0.5297000804618479, 0.982228, 0.751442, 0.147565, 0.5303452653366102, 0.981173, 0.759135, 0.156863, 0.5309902857073249, 0.980032, 0.766837, 0.166353, 0.5316354705820872, 0.978806, 0.774545, 0.176037, 0.5322804909528018, 0.977497, 0.782258, 0.185923, 0.5329256758275641, 0.976108, 0.789974, 0.196018, 0.5335706961982788, 0.974638, 0.797692, 0.206332, 0.5342158810730412, 0.973088, 0.805409, 0.216877, 0.5348610659478035, 0.971468, 0.813122, 0.227658, 0.535506086318518, 0.969783, 0.820825, 0.238686, 0.5361512711932803, 0.968041, 0.828515, 0.249972, 0.5367962915639951, 0.966243, 0.836191, 0.261534, 0.5374414764387574, 0.964394, 0.843848, 0.273391, 0.5380864968094721, 0.962517, 0.851476, 0.285546, 0.5387316816842344, 0.960626, 0.859069, 0.29801, 0.539376702054949, 0.95872, 0.866624, 0.31082, 0.5400218869297113, 0.956834, 0.874129, 0.323974, 0.5406670718044737, 0.954997, 0.881569, 0.337475, 0.5413120921751883, 0.953215, 0.888942, 0.351369, 0.5419572770499506, 0.951546, 0.896226, 0.365627, 0.5426022974206652, 0.950018, 0.903409, 0.380271, 0.5432474822954276, 0.948683, 0.910473, 0.395289, 0.5438925026661422, 0.947594, 0.917399, 0.410665, 0.5445376875409046, 0.946809, 0.924168, 0.426373, 0.5451828724156669, 0.946392, 0.930761, 0.442367, 0.5458278927863816, 0.946403, 0.937159, 0.458592, 0.5464730776611438, 0.946903, 0.943348, 0.47497, 0.5471180980318585, 0.947937, 0.949318, 0.491426, 0.5477632829066208, 0.949545, 0.955063, 0.50786, 0.5484083032773355, 0.95174, 0.960587, 0.524203, 0.5490534881520979, 0.954529, 0.965896, 0.540361, 0.54969867302686, 0.957896, 0.971003, 0.556275, 0.5503436933975747, 0.961812, 0.975924, 0.571925, 0.5509888782723371, 0.966249, 0.980678, 0.587206, 0.5516338986430518, 0.971162, 0.985282, 0.602154, 0.552279083517814, 0.976511, 0.989753, 0.61676, 0.5529241038885289, 0.982257, 0.994109, 0.631017, 0.553569288763291, 0.988362, 0.998364, 0.644924]
rho_1LUT.NanColor = [0.0, 1.0, 0.0]
rho_1LUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'rho_1'
rho_1PWF = GetOpacityTransferFunction('rho_1')
rho_1PWF.Points = [0.38906524114414304, 0.0, 0.5, 0.0, 0.553569288763291, 1.0, 0.5, 0.0]
rho_1PWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
solDisplay.Representation = 'Surface'
solDisplay.ColorArrayName = ['POINTS', 'rho_1']
solDisplay.LookupTable = rho_1LUT
solDisplay.SelectTCoordArray = 'None'
solDisplay.SelectNormalArray = 'None'
solDisplay.SelectTangentArray = 'None'
solDisplay.OSPRayScaleArray = 'B1'
solDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
solDisplay.SelectOrientationVectors = 'None'
solDisplay.ScaleFactor = 0.19978302548686572
solDisplay.SelectScaleArray = 'B1'
solDisplay.GlyphType = 'Arrow'
solDisplay.GlyphTableIndexArray = 'B1'
solDisplay.GaussianRadius = 0.009989151274343286
solDisplay.SetScaleArray = ['POINTS', 'B1']
solDisplay.ScaleTransferFunction = 'PiecewiseFunction'
solDisplay.OpacityArray = ['POINTS', 'B1']
solDisplay.OpacityTransferFunction = 'PiecewiseFunction'
solDisplay.DataAxesGrid = 'GridAxesRepresentation'
solDisplay.PolarAxes = 'PolarAxesRepresentation'
solDisplay.ScalarOpacityUnitDistance = 0.04404861553964964
solDisplay.ScalarOpacityFunction = rho_1PWF
solDisplay.OpacityArrayName = ['POINTS', 'B1']
solDisplay.SliceFunction = 'Plane'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
solDisplay.ScaleTransferFunction.Points = [0.05000000000000002, 0.0, 0.5, 0.0, 0.05000763013958931, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
solDisplay.OpacityTransferFunction.Points = [0.05000000000000002, 0.0, 0.5, 0.0, 0.05000763013958931, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
solDisplay.SliceFunction.Origin = [0.5, 0.0, 0.0]

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(sol)
# ----------------------------------------------------------------

myview = GetActiveView()
output_name = f'./khi{input_no}.png'
SaveScreenshot(output_name, myview,
        ImageResolution=[1200, 2200])

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')