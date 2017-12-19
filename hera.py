# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import glob
import os
from os.path import join, exists, expanduser
from keras.preprocessing.image import ImageDataGenerator
from keras.applications import resnet50
from keras.models import Sequential, Model
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils.np_utils import to_categorical
from PIL import Image, ImageOps
from scipy.misc import imresize
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer, LabelEncoder

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory


train_data_dir = 'input/train'
test_data_dir = 'input/test'

img_width, img_height = 197, 197

z = glob.glob(train_data_dir + '/*/*.png')
ori_label = []
ori_imgs = []
for fn in z:
    if fn[-3:] != 'png':
        continue
    ori_label.append(fn.split('/')[-2])
    new_img = Image.open(fn)
    ori_imgs.append(ImageOps.fit(new_img, (img_width, img_height), Image.ANTIALIAS).convert('RGB'))

z = glob.glob(test_data_dir + '/*.png')
ori_test_names = []
ori_test_imgs = []
for fn in z:
    if fn[-3:] != 'png':
        continue
    ori_test_names.append(fn.split('/')[-1])
    new_img = Image.open(fn)
    ori_test_imgs.append(ImageOps.fit(new_img, (img_width, img_height), Image.ANTIALIAS).convert('RGB'))

test_imgs = np.array([np.array(im) for im in ori_test_imgs])
test_imgs = test_imgs.reshape(test_imgs.shape[0], img_width, img_height, 3) / 255

imgs = np.array([np.array(im) for im in ori_imgs])


lb = LabelBinarizer().fit(ori_label)
label = lb.transform(ori_label) 

trainX, validX, trainY, validY = train_test_split(imgs, label, test_size=0.05, random_state=42)

uni_labs = np.unique(ori_label, return_counts=True)

datagen = ImageDataGenerator(
    featurewise_center=True,
    featurewise_std_normalization=True,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True)

datagen.fit(trainX)

trainY = to_categorical(trainY)
print(trainY.shape)

base_model = resnet50.ResNet50(include_top=False, weights='imagenet', input_tensor=None, input_shape=(img_width, img_height, 3), pooling='avg', classes=12)

add_model = Sequential()
add_model.add(Flatten(input_shape=(img_width, img_height, 3)))

add_model.add(Dense(256))
add_model.add(Activation("relu"))

add_model.add(Dense(12))
add_model.add(Activation("softmax"))

model = Model(inputs=base_model.input, outputs=add_model(base_model.output))
model.compile(loss='categorical_crossentropy',
             optimizer='Adam',
             metrics=['accuracy'])

model.fit_generator(datagen.flow(trainX, trainY, batch_size=32), steps_per_epoch=len(trainX) /32, epochs=32)

test = model.fit(imgs, label, validation_split=0.2, epochs=10, batch_size=10)

prediction = model.predict_classes(test_imgs)

counter = 0
test = uni_labs[0]
result = pd.DataFrame(columns=['file', 'species'])
for i in ori_test_names:
    pred = prediction[counter]
    result = result.append({'file': i, 'species': test[pred]}, ignore_index=True)
    counter = counter + 1
    
result.to_csv('submission.csv', index=False)
