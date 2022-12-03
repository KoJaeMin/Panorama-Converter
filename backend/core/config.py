from pydantic import BaseSettings
from dotenv import load_dotenv
import os
from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator

load_dotenv()

class Settings(BaseSettings):
    #### 60 minutes * 24 hours = 1 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    POSTGRES_HOST: str = os.environ['DB_HOST']
    POSTGRES_PORT: str = os.environ['DB_PORT']
    POSTGRES_USER: str = os.environ['DB_USER']
    POSTGRES_PASSWORD: str = os.environ['DB_PW']
    POSTGRES_DB: str = os.environ['DB_DB']
    # SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None
    
class DefaultSetting():
    MODEL : str = 'SinGAN'
    
    #workspace:
    not_cuda : int = 0 ### action = 'store_true', help = 'disables cuda'
    
    #load, input, save configurations:
    netG : str = '' ### help = p'ath to netG (to continue training)'
    netD :str = '' ### help = 'path to netD (to continue training)'
    manualSeed : int ### help = 'manual seed'
    nc_z : int = 3 ### help='noise # channels'
    nc_im : int = 3 ### help='image # channels'
    out : str = '' ### help='output folder'
    name : str = '' ### help='username'
    
    #networks hyper parameters:
    nfc : int = 32
    min_nfc : int = 32
    kernel_size : int = 3
    num_layer : int = 5
    stride : int = 1
    padd_size : int = 0
    
    #pyramid parameters:
    scale_factor : float = 0.75 ### help='pyramid scale factor' #pow(0.5,1/6))
    noise_amp : float = 0.1 ### help='addative noise cont weight'
    min_size : int = 25 ### help='image minimal size at the coarser scale'
    max_size : int = 200 ### help='image minimal size at the coarser scale'

    #optimization hyper parameters:
    niter : int = 300 ### help='number of epochs to train per scale'
    gamma : float = 0.1 ### help='scheduler gamma'
    lr_g : float = 5e-4 ### help='learning rate'
    lr_d : float = 5e-4 ### help='learning rate'
    beta1 : float = 0.5 ### help='beta1 for Adam optimizer.'
    Gsteps : int = 3 ### help='Generator inner steps'
    Dsteps : int = 3 ### help='Discriminator inner steps'
    lambda_grad : float = 0.1 ### help='gradient penelty weight'
    alpha : float = 10 ### help='reconstruction loss weight'
    optimizer : str = 'Adam' ### help='optimizer : [Adam(default)|AdamW|Adamax|NAdam|RAdam]'

class TrainingSetting(DefaultSetting):
    input_name :str = ''

class MakingSetting(DefaultSetting):
    input_name :str = ''

settings = Settings()
opt = TrainingSetting()