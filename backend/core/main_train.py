from config import get_arguments
from SinGAN.manipulate import *
from SinGAN.training import *
import SinGAN.functions as functions
from SinGAN.logger import custom_logger
import time

if __name__ == '__main__':
    parser = get_arguments()
    parser.add_argument('--input_dir', help='input image dir', default='./Input')
    parser.add_argument('--input_name', help='input image name', required=True)
    parser.add_argument('--mode', help='task to be done', default='train')
    parser.add_argument('--trainmodel_dir', help='trained model dir',default= './TrainedModels')
    opt = parser.parse_args()
    opt = functions.post_config(opt)
    Gs = []
    Zs = []
    reals = []
    NoiseAmp = []
    dir2save = functions.generate_dir2save(opt)
    train_log = custom_logger("trainer",'DEBUG')

    if (os.path.exists(dir2save)):
        print('trained model already exist')
    else:
        try:
            os.makedirs(dir2save)
        except OSError:
            pass
        train_log.debug("Training ... \n")
        start = time.time()
        real = functions.read_image(opt)
        functions.adjust_scales2image(real, opt)
        train(opt, Gs, Zs, reals, NoiseAmp)
        SinGAN_generate(Gs,Zs,reals,NoiseAmp,opt)
        train_log.debug(f"Total time :  {time.time() - start}s")
        train_log.debug(f"Option :  {opt}")
        train_log.debug("-"*30)