# -*- coding: utf-8 -*-

import os

import tensorflow as tf


def get_dataset(dataset_name, image_width, image_height, batch_size, validation_split=None):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if validation_split is None:
        train_data_generator = tf.keras.preprocessing.image.ImageDataGenerator()
        train_data_generator = train_data_generator.flow_from_directory(
            directory=dir_path + '/' + dataset_name + '/train',
            target_size=(image_width, image_height),
            batch_size=batch_size)
        validation_data_generator = tf.keras.preprocessing.image.ImageDataGenerator()
        validation_data_generator = validation_data_generator.flow_from_directory(
            directory=dir_path + '/' + dataset_name + '/validation',
            target_size=(image_width, image_height),
            batch_size=batch_size)
    else:
        data_generator = tf.keras.preprocessing.image.ImageDataGenerator(validation_split=validation_split)
        train_data_generator = data_generator.flow_from_directory(directory=dir_path + '/' + dataset_name + '/train',
                                                                  target_size=(image_width, image_height),
                                                                  batch_size=batch_size,
                                                                  subset='training')
        validation_data_generator = data_generator.flow_from_directory(
            directory=dir_path + '/' + dataset_name + '/train',
            target_size=(image_width, image_height),
            batch_size=batch_size,
            subset='validation')
    test_data_generator = tf.keras.preprocessing.image.ImageDataGenerator()
    test_data_generator = test_data_generator.flow_from_directory(directory=dir_path + '/' + dataset_name + '/test',
                                                                  target_size=(image_width, image_height),
                                                                  batch_size=batch_size)
    return train_data_generator, validation_data_generator, test_data_generator
