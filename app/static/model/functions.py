import numpy as np

import cv2

from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

#import tensorflow as tf
#from keras.models import Sequential

#from keras.applications.resnet50 import ResNet50
#from keras.applications.resnet50 import preprocess_input, decode_predictions
#from keras.layers import GlobalAveragePooling2D, Dense


def face_detector(img_path):


    # extract pre-trained face detector
    face_cascade = cv2.CascadeClassifier(
    'haarcascades/haarcascade_frontalface_alt.xml')

    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    return len(faces) > 0


'''def path_to_tensor(img_path):
    # loads RGB image as PIL.Image.Image type
    img = image.load_img(img_path, target_size=(224, 224))
    # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    x = image.img_to_array(img)
    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    return np.expand_dims(x, axis=0)


def paths_to_tensor(img_paths):
    list_of_tensors = [path_to_tensor(img_path)
                       for img_path in tqdm(img_paths)]
    return np.vstack(list_of_tensors)


def ResNet50_predict_labels(img_path):
    # returns prediction vector for image located at img_path
    img = preprocess_input(path_to_tensor(img_path))
    return np.argmax(ResNet50_model.predict(img))

### returns "True" if a dog is detected in the image stored at img_path
def dog_detector(img_path):
    prediction = ResNet50_predict_labels(img_path)
    return ((prediction <= 268) & (prediction >= 151))





# SKYNET


Skynet = Sequential()
Skynet.add(GlobalAveragePooling2D(input_shape=train_res50.shape[1:]))
Skynet.add(Dense(133, activation='softmax'))
Skynet.compile(loss='categorical_crossentropy',
               optimizer='rmsprop', metrics=['accuracy'])

Skynet.load_weights('saved_models/weights.best.res50.hdf5')

def skynet_predict_breed(img_path):
    # extract bottleneck features
    bottleneck_feature = extract_Resnet50(path_to_tensor(img_path))
    # obtain predicted vector
    predicted_vector = Skynet.predict(bottleneck_feature)
    # return dog breed that is predicted by the model
    return dog_names[np.argmax(predicted_vector)]




# JARVIS


def Jarvis(img_path, img_size):

    if dog_detector(img_path):
        print('DOG FOUND!')
        pred = skynet_predict_breed(img_path)
        pic = img_resize(img_path)
        display(pic)
        breed = pred.split('.')[1]
        breed = breed.replace('_', ' ').title()
    elif face_detector(img_path):
        print('HUMAN FOUND!')
        pred = skynet_predict_breed(img_path)
        pic = img_resize(img_path)
        display(pic)
        breed = pred.split('.')[1]
        breed = breed.replace('_', ' ').title()
    else:
        pic = img_resize('images/Error images/FaceLess.jpg')
        display(pic)
'''