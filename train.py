# -*- coding: utf-8 -*-

import json

import alexnet
import datagenerator

IMAGE_WIDTH = 224
IMAGE_HEIGHT = 224
BATCH_SIZE = 32
EPOCHS = 100


def main():
    print('Reading Dataset...')
    train, validation, test = datagenerator.get_dataset('fish-dataset',
                                                        image_width=IMAGE_WIDTH,
                                                        image_height=IMAGE_HEIGHT,
                                                        batch_size=BATCH_SIZE,
                                                        validation_split=0.1)

    print('Building Model...')
    model = alexnet.build_model(input_width=train.image_shape[0],
                                input_height=train.image_shape[1],
                                input_channels=train.image_shape[2],
                                num_classes=train.num_classes,
                                dropout_rate=0.5)

    model.summary()

    print('Training...')
    alexnet.train_model(model=model,
                        train_data_generator=train,
                        validation_data_generator=validation,
                        epochs=EPOCHS,
                        learning_rate=0.001,  # Original value: 0.01
                        momentum=0.9)

    print('Evaluating...')
    print(alexnet.evaluate_model(model=model, data_generator=test))

    print('Saving Model...')
    model.save('./model/')
    with open('class_names.json', 'w') as json_file:
        json.dump(train.class_indices, json_file, indent=4)

    print('Training Done')


if __name__ == '__main__':
    main()
