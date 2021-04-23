# -*- coding: utf-8 -*-

import tensorflow as tf

# ----------------------------------------------------------------------------------------------------


RANDOM_MEAN = 0
RANDOM_STDDEV = 0.01


def build_model(input_width=224, input_height=224, input_channels=3, num_classes=1000, dropout_rate=0.5):
    model = tf.keras.Sequential()
    # Layer 1: Use BatchNormalization instead of Local Response Normalization.
    model.add(tf.keras.layers.Conv2D(filters=96,
                                     kernel_size=(11, 11),
                                     strides=(4, 4),
                                     padding='valid',
                                     kernel_initializer=tf.keras.initializers.RandomNormal(mean=RANDOM_MEAN,
                                                                                           stddev=RANDOM_STDDEV),
                                     bias_initializer=tf.keras.initializers.Zeros(),
                                     activation=tf.keras.activations.relu,
                                     input_shape=(input_width, input_height, input_channels),
                                     data_format='channels_last'))
    model.add(tf.keras.layers.BatchNormalization())
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(3, 3), strides=(2, 2), padding='valid'))
    # Layer 2: Use Batch Normalization instead of Local Response Normalization.
    model.add(tf.keras.layers.Conv2D(filters=256,
                                     kernel_size=(5, 5),
                                     strides=(1, 1),
                                     padding='same',
                                     kernel_initializer=tf.keras.initializers.RandomNormal(mean=RANDOM_MEAN,
                                                                                           stddev=RANDOM_STDDEV),
                                     bias_initializer=tf.keras.initializers.Ones(),
                                     activation=tf.keras.activations.relu))
    model.add(tf.keras.layers.BatchNormalization())
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(3, 3), strides=(2, 2), padding='valid'))
    # Layer 3.
    model.add(tf.keras.layers.Conv2D(filters=384,
                                     kernel_size=(3, 3),
                                     strides=(1, 1),
                                     padding='same',
                                     kernel_initializer=tf.keras.initializers.RandomNormal(mean=RANDOM_MEAN,
                                                                                           stddev=RANDOM_STDDEV),
                                     bias_initializer=tf.keras.initializers.Zeros(),
                                     activation=tf.keras.activations.relu))
    # Layer 4.
    model.add(tf.keras.layers.Conv2D(filters=384,
                                     kernel_size=(3, 3),
                                     strides=(1, 1),
                                     padding='same',
                                     kernel_initializer=tf.keras.initializers.RandomNormal(mean=RANDOM_MEAN,
                                                                                           stddev=RANDOM_STDDEV),
                                     bias_initializer=tf.keras.initializers.Ones(),
                                     activation=tf.keras.activations.relu))
    # Layer 5.
    model.add(tf.keras.layers.Conv2D(filters=256,
                                     kernel_size=(3, 3),
                                     strides=(1, 1),
                                     padding='same',
                                     kernel_initializer=tf.keras.initializers.RandomNormal(mean=RANDOM_MEAN,
                                                                                           stddev=RANDOM_STDDEV),
                                     bias_initializer=tf.keras.initializers.Ones(),
                                     activation=tf.keras.activations.relu))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(3, 3), strides=(2, 2), padding='valid'))
    # Flatten
    model.add(tf.keras.layers.Flatten())
    # Layer 6.
    model.add(tf.keras.layers.Dense(units=4096,
                                    kernel_initializer=tf.keras.initializers.RandomNormal(mean=RANDOM_MEAN,
                                                                                          stddev=RANDOM_STDDEV),
                                    bias_initializer=tf.keras.initializers.Ones(),
                                    activation=tf.keras.activations.relu))
    model.add(tf.keras.layers.Dropout(dropout_rate))
    # Layer 7.
    model.add(tf.keras.layers.Dense(units=4096,
                                    kernel_initializer=tf.keras.initializers.RandomNormal(mean=RANDOM_MEAN,
                                                                                          stddev=RANDOM_STDDEV),
                                    bias_initializer=tf.keras.initializers.Ones(),
                                    activation=tf.keras.activations.relu))
    model.add(tf.keras.layers.Dropout(dropout_rate))
    # Layer 8.
    model.add(tf.keras.layers.Dense(units=num_classes,
                                    kernel_initializer=tf.keras.initializers.RandomNormal(mean=RANDOM_MEAN,
                                                                                          stddev=RANDOM_STDDEV),
                                    bias_initializer=tf.keras.initializers.Zeros(),
                                    activation=tf.keras.activations.softmax))
    return model


# ----------------------------------------------------------------------------------------------------


# Batch size: 128.
def train_model(model, train_data_generator, validation_data_generator, epochs, learning_rate=0.01, momentum=0.9,
                decay=0.0005, log_dir=None):
    callbacks = []
    if log_dir is not None:
        tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir)
        callbacks.append(tensorboard_callback)
    model.compile(loss=tf.keras.losses.categorical_crossentropy,
                  optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate, momentum=momentum, decay=decay),
                  metrics=[tf.keras.metrics.CategoricalAccuracy()])
    model.fit_generator(generator=train_data_generator, validation_data=validation_data_generator, epochs=epochs,
                        callbacks=callbacks)


# ----------------------------------------------------------------------------------------------------


def evaluate_model(model, data_generator):
    metrics_names = model.metrics_names
    values = model.evaluate_generator(data_generator)
    dictionary = dict(zip(metrics_names, values))
    return dictionary

# ----------------------------------------------------------------------------------------------------
