from core.config import TrainingSetting
from core.SinGAN.manipulate import *
from core.SinGAN.training import *
import core.SinGAN.functions as functions

def trainer(input_name : str, input_dir : str,trainmodel_dir : str, out : str,user_name : str = ''):
    opt = TrainingSetting(input_name = input_name,input_dir = input_dir,trainmodel_dir = trainmodel_dir,out=out, user_name = user_name)
    opt = functions.post_config(opt)
    Gs = []
    Zs = []
    reals = []
    NoiseAmp = []
    dir2save = functions.generate_dir2save(opt)

    if (os.path.exists(dir2save)):
        print('trained model already exist')
    else:
        try:
            os.makedirs(dir2save)
        except OSError:
            pass
        
        
        real = functions.read_image(opt)
        functions.adjust_scales2image(real, opt)
        train(opt, Gs, Zs, reals, NoiseAmp)
        SinGAN_generate(Gs,Zs,reals,NoiseAmp,opt)