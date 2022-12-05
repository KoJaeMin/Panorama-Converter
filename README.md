# Panorama-Converter
Panorama Converter with SinGAN


## 연구배경

제품 또는 서비스의 첫인상은 사용 여부를 결정짓는다. 첫인상의 요소 중 하나를 꼽자면 배경이다. 이에 많은 제품 또는 서비스에 자연스럽고 알맞은 배경 이미지를 사용한다. 하지만 규격에 맞으며 원하는 사진을 찾기란 어렵다. 원하는 사진을 찾아도 규격에 안 맞는 경우가 많다. 원하는 이미지에 자연스럽게 늘려 추가적인 이미지 제작 또는 수정 작업을 할 경우 비용이 증가한다.

최근 새로운 이미지를 생성하는 딥러닝 기술인 GAN(Generative Adversarial Networks)에 대한 연구와 응용이 활발히 이루어지고 있다. 파노라마 이미지를 제작하는 다양한 방법 중 하나로 하나의 이미지만을 사용하여 학습하고 새로운 이미지를 만들어내는 SinGAN을 이용하려한다. 이를 사용자들이 편하게 이용하기 위하여 웹을 이용하여 서비스를 제공하고자 한다. 이전에는 딥러닝을 이용하여 서비스를 제공하는 경우 미리 학습된 모델을 이용하여야 한다. 하지만 SinGAN으로 파노라마 이미지 제작하는 과정의 특성상 Train Input 이미지와 생성하기 위한 Input 이미지가 같아 입력값을 받고 학습이 진행된 후 이미지 생성을 시작할 수 있다. 이 경우 많은 시간이 소요되기에 평소 성능 증긴 목적의 연구들과는 다르게 최적화를 진행해야 한다. 이를 통하여 웹에서 한 장의 이미지를 사용하여 원하는 파노라마 이미지 제작이 가능해 질 것이다.


## 연구 내용

### 기존 연구와의 차별성

기존 연구들은 모델들은 이미지를 생성 및 학습에 맞추어져 있으며 성능에 대한 연구들이다. 사용자가 이용하기에 전문적인 지식 및 개발 능력을 요구한다. 이를 해결하기 위해서 웹으로 서비스를 한다고 하더라도 이전에 딥러닝을 이용한 서비스들은 미리 학습된 모델을 이용하여야 한다. 하지만 SinGAN으로 파노라마 이미지 제작하는 과정의 특성상 Train Input 이미지와 생성하기 위한 Input 이미지가 같아 입력값을 받는 동시에 학습하고 이미지 생성을 시작할 수 있다. 이 경우 많은 시간이 소요되기에 평소 성능 증긴 목적의 연구들과는 다르게 최적화를 진행해야 한다.

웹과 SinGAN을 결합하여 사용자들에게 사용자들이 한 장의 배경 이미지로 원하는 규격의 파노라마 이미지를 제공받을 수 있는 웹 서비스로 사용자들이 사용하기 용이하며 편리함 제공하여 시공간의 제약을 줄인다. 또한 다양한 하이퍼파라미터를 조정하며 웹 서비스에 맞도록 최적하하여 서비스 제공 시간을 단축시키며 실제와 같은 이미지를 제공한다.

### 제안 방법

  - HyperParameter 조정
  
    - Epoch 조정(100~1000) 100단위
  
    - Max Size 조정(150, 200)
  
  - Optimizer 변경
  
    - Adam
    
    - Adamax
    
    - AdamW
    
    - SGD
    
    - ASGD
    
### 검증
<img src="https://user-images.githubusercontent.com/77095298/205572409-2e8ced17-6188-4d80-acad-66d203a8f362.png" width="500" height="500">
<img src="https://user-images.githubusercontent.com/77095298/205572431-58f9e53e-6862-4fad-9d90-553276cc5a49.png" width="500" height="500">
<img src="https://user-images.githubusercontent.com/77095298/205572452-aacfec80-8a3a-43fd-9042-7a42c6bc89ae.png" width="500" height="500">
<img src="https://user-images.githubusercontent.com/77095298/205572467-49710e16-fe9b-47c8-99fd-7db33c79dabc.png" width="500" height="500">

## 참고문헌

  [1] Tamar Rott Shaham Technion, SinGAN: Learning a Generative Model from a Single Natural Image

  [2] Ian J. Goodfellow, Generative Adversarial Nets

