from pydantic import BaseSettings
from dotenv import load_dotenv
import os
from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator

load_dotenv()

# class Settings(BaseSettings):
    #### 60 minutes * 24 hours = 1 days
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    # BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    # POSTGRES_HOST: str = os.environ['DB_HOST']
    # POSTGRES_PORT: str = os.environ['DB_PORT']
    # POSTGRES_USER: str = os.environ['DB_USER']
    # POSTGRES_PASSWORD: str = os.environ['DB_PW']
    # POSTGRES_DB: str = os.environ['DB_DB']
    # SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None
    
class DefaultSetting():
    def __init__(self,input_name : str, input_dir : str,trainmodel_dir : str, out : str, user_name : str = ''):
        #workspace:
        self.not_cuda : int = 0 ### action = 'store_true', help = 'disables cuda'

        #load, input, save configurations:
        self.netG : str = '' ### help= p'ath to netG (to continue training)'
        self.netD :str = '' ### help= 'path to netD (to continue training)'
        self.manualSeed : int = None ### help = 'manual seed'
        self.nc_z : int = 3 ### help='noise # channels'
        self.nc_im : int = 3 ### help='image # channels'
        self.out : str = out ### help='output folder'
        self.name : str = user_name ### help='user name'
        self.input_name : str = input_name ### help='input image name'
        self.trainmodel_dir : str = trainmodel_dir ### help='trained model directory'
        self.input_dir : str = input_dir ### help='input image directory' 

        #networks hyper parameters:
        self.nfc : int = 32
        self.min_nfc : int = 32
        self.kernel_size : int = 3
        self.num_layer : int = 5
        self.stride : int = 1
        self.padd_size : int = 0

        #pyramid parameters:
        self.scale_factor : float = 0.75 ### help='pyramid scale factor' #pow(0.5,1/6))
        self.noise_amp : float = 0.1 ### help='addative noise cont weight'
        self.min_size : int = 25 ### help='image minimal size at the coarser scale'
        self.max_size : int = 200 ### help='image minimal size at the coarser scale'

        #optimization hyper parameters:
        self.niter : int = 300 ### help='number of epochs to train per scale'
        self.gamma : float = 0.1 ### help='scheduler gamma'
        self.lr_g : float = 5e-4 ### help='learning rate'
        self.lr_d : float = 5e-4 ### help='learning rate'
        self.beta1 : float = 0.5 ### help='beta1 for Adam optimizer.'
        self.Gsteps : int = 3 ### help='Generator inner steps'
        self.Dsteps : int = 3 ### help='Discriminator inner steps'
        self.lambda_grad : float = 0.1 ### help='gradient penelty weight'
        self.alpha : float = 10 ### help='reconstruction loss weight'
        self.optimizer : str = 'AdamW' ### help='optimizer : [AdamW(default)|Adam|Adamax|NAdam|RAdam]'


class TrainingSetting(DefaultSetting):
    def __init__(self, input_name : str, input_dir : str,trainmodel_dir :str, out : str,user_name : str = ''):
        # super().__init__(input_name = self.input_name,input_dir = self.input_dir,out=self.out, trainmodel_dir = self.trainmodel_dir, user_name = self.user_name)
        super().__init__(input_name,input_dir,trainmodel_dir,out,user_name)
        self.mode = 'train'

class MakingSetting(DefaultSetting):
    def __init__(self, height : int, width : int ,input_name : str, input_dir : str,trainmodel_dir : str, out : str,user_name : str = ''):
        # super().__init__(input_name = self.input_name,input_dir = self.input_dir,out=self.out, trainmodel_dir = self.trainmodel_dir, user_name = self.user_name)
        super().__init__(input_name,input_dir,trainmodel_dir,out,user_name)
        self.mode : str = 'random_samples_arbitrary_sizes'
        self.gen_start_scale : int = 0 ### help='generation start scale'
        self.height : int = height
        self.width : int = width
        self.scale_h : float = round(self.width/self.height,2) ### help='horizontal resize factor for random samples'
        self.scale_v : float = 1 ### help='vertical resize factor for random samples'