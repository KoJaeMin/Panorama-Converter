from datatype.singan import MakingSetting
from core.utils import ResizeImg
from core.SinGAN.manipulate import *
from core.SinGAN.training import *
from core.SinGAN.imresize import imresize
import core.SinGAN.functions as functions

def make(height : int, width : int ,input_name : str, input_dir : str,trainmodel_dir: str, out : str,user_name : str = ''):
    opt = MakingSetting(height = height, width = width ,input_name =input_name,input_dir =input_dir, trainmodel_dir = trainmodel_dir, out = out,user_name = user_name)
    opt = functions.post_config(opt)
    Gs = []
    Zs = []
    reals = []
    NoiseAmp = []
    dir2save = functions.generate_dir2save(opt)
    
    if dir2save is None:
        print('task does not exist')
    elif (os.path.exists(dir2save)):
        print('random samples for image %s at size: scale_h=%f, scale_v=%f, already exist' % (opt.input_name, opt.scale_h, opt.scale_v))
    else:
        try:
            os.makedirs(dir2save)
        except OSError:
            pass

        
        real = functions.read_image(opt)
        functions.adjust_scales2image(real, opt)
        Gs, Zs, reals, NoiseAmp = functions.load_trained_pyramid(opt)
        in_s = functions.generate_in2coarsest(reals,opt.scale_v,opt.scale_h,opt)
        SinGAN_generate(Gs, Zs, reals, NoiseAmp, opt, in_s, scale_v=opt.scale_v, scale_h=opt.scale_h)
        ResizeImg(img_path= '%s/%s.png' % (opt.dir2save, opt.input_name[:-4]) ,height=height, width= width)