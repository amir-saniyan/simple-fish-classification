# -*- coding: utf-8 -*-

import json
import sys

import numpy as np
import tensorflow as tf

IMAGE_WIDTH = 224
IMAGE_HEIGHT = 224


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 inference.py <image-file-name>')
        exit()

    print('Loading Model...')
    model = tf.keras.models.load_model('./model/')
    with open('class_names.json') as json_file:
        class_names = json.load(json_file)

    print('Reading Image...')
    image = tf.keras.preprocessing.image.load_img(sys.argv[1], target_size=(IMAGE_HEIGHT, IMAGE_WIDTH))
    image_array = tf.keras.preprocessing.image.img_to_array(image)
    image_array = tf.expand_dims(image_array, 0)

    print('Predicting...')
    prediction = model.predict(image_array).reshape(-1)

    index = int(np.argmax(prediction))
    for class_name, class_index in class_names.items():
        if class_index == index:
            print('Class: {}, Score: {}'.format(class_name, prediction[index]))


if __name__ == '__main__':
    main()
