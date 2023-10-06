
# 예측에 필요한 라이브러리
from tensorflow.keras.applications.vgg16 import preprocess_input
import tensorflow as tf
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.imagenet_utils import decode_predictions

def prediction_model():
    img = Image.open('./sample_data/cat_224x224.jpg')
    print(type(img))
    model = tf.keras.models.load_model('vgg16.h5')
    # resize
    target_size = 224
    img = img.resize((target_size, target_size)) 

    #numpy array로 변경
    np_img = image.img_to_array(img)

    #4차원으로 변경 
    img_batch = np.expand_dims(np_img, axis=0)
    #feature normalization
    pre_processed = preprocess_input(img_batch)
    
    # 예측
    y_preds = model.predict(pre_processed)
    np.set_printoptions(suppress=True, precision=5) #소수 5자리까지 
    # 1위 예측 반환
    result = decode_predictions(y_preds, top=1)
    result = {"predicted_label" : str(result[0][0][1]), "prediction_score" :  str(result[0][0][2])}
    return result
