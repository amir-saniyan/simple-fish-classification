# Simple Fish Classification

In the name of God

This repository contains implementation of `Simple Fish Classification`.

![Dataset](./dataset.jpg)

## Install Requirements

To install requirements run the following command:

```shell
$ pip install -r requirements.txt
```

## Training

To train the model run the following command:

```shell
$ python3 train.py
```

Output:

```shell
Reading Dataset...
Found 4516 images belonging to 30 classes.
Found 488 images belonging to 30 classes.
Found 3040 images belonging to 30 classes.

Building Model...

Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 54, 54, 96)        34944     
_________________________________________________________________
batch_normalization (BatchNo (None, 54, 54, 96)        384       
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 26, 26, 96)        0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 26, 26, 256)       614656    
_________________________________________________________________
batch_normalization_1 (Batch (None, 26, 26, 256)       1024      
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 12, 12, 256)       0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 12, 12, 384)       885120    
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 12, 12, 384)       1327488   
_________________________________________________________________
conv2d_4 (Conv2D)            (None, 12, 12, 256)       884992    
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 5, 5, 256)         0         
_________________________________________________________________
flatten (Flatten)            (None, 6400)              0         
_________________________________________________________________
dense (Dense)                (None, 4096)              26218496  
_________________________________________________________________
dropout (Dropout)            (None, 4096)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 4096)              16781312  
_________________________________________________________________
dropout_1 (Dropout)          (None, 4096)              0         
_________________________________________________________________
dense_2 (Dense)              (None, 30)                122910    
=================================================================
Total params: 46,871,326
Trainable params: 46,870,622
Non-trainable params: 704
_________________________________________________________________

Training...
Epoch 1/100
142/142 [==============================] - 23s 151ms/step - loss: 4.2017 - categorical_accuracy: 0.0351 - val_loss: 3.2447 - val_categorical_accuracy: 0.0861
Epoch 2/100
142/142 [==============================] - 21s 149ms/step - loss: 3.1782 - categorical_accuracy: 0.1065 - val_loss: 2.7572 - val_categorical_accuracy: 0.1660
Epoch 3/100
142/142 [==============================] - 21s 150ms/step - loss: 2.8229 - categorical_accuracy: 0.1693 - val_loss: 2.4470 - val_categorical_accuracy: 0.2582
Epoch 4/100
142/142 [==============================] - 21s 149ms/step - loss: 2.5298 - categorical_accuracy: 0.2641 - val_loss: 2.6050 - val_categorical_accuracy: 0.2336
Epoch 5/100
142/142 [==============================] - 21s 149ms/step - loss: 2.4260 - categorical_accuracy: 0.2820 - val_loss: 2.1825 - val_categorical_accuracy: 0.3217
Epoch 6/100
142/142 [==============================] - 21s 149ms/step - loss: 2.1832 - categorical_accuracy: 0.3448 - val_loss: 1.9746 - val_categorical_accuracy: 0.3955
Epoch 7/100
142/142 [==============================] - 21s 149ms/step - loss: 1.9981 - categorical_accuracy: 0.4008 - val_loss: 1.9451 - val_categorical_accuracy: 0.4180
Epoch 8/100
142/142 [==============================] - 21s 149ms/step - loss: 1.8939 - categorical_accuracy: 0.4325 - val_loss: 1.7076 - val_categorical_accuracy: 0.4775
Epoch 9/100
142/142 [==============================] - 21s 149ms/step - loss: 1.7176 - categorical_accuracy: 0.4882 - val_loss: 1.5508 - val_categorical_accuracy: 0.5328
Epoch 10/100
142/142 [==============================] - 21s 150ms/step - loss: 1.5934 - categorical_accuracy: 0.5234 - val_loss: 1.3783 - val_categorical_accuracy: 0.5922
Epoch 11/100
142/142 [==============================] - 21s 148ms/step - loss: 1.4108 - categorical_accuracy: 0.5730 - val_loss: 1.5432 - val_categorical_accuracy: 0.5451
Epoch 12/100
142/142 [==============================] - 21s 150ms/step - loss: 1.3683 - categorical_accuracy: 0.5827 - val_loss: 1.4381 - val_categorical_accuracy: 0.5717
Epoch 13/100
142/142 [==============================] - 21s 149ms/step - loss: 1.1930 - categorical_accuracy: 0.6403 - val_loss: 1.1328 - val_categorical_accuracy: 0.6598
Epoch 14/100
142/142 [==============================] - 21s 149ms/step - loss: 1.1431 - categorical_accuracy: 0.6543 - val_loss: 1.3218 - val_categorical_accuracy: 0.5902
Epoch 15/100
142/142 [==============================] - 21s 149ms/step - loss: 1.0611 - categorical_accuracy: 0.6838 - val_loss: 1.0032 - val_categorical_accuracy: 0.7213
Epoch 16/100
142/142 [==============================] - 21s 148ms/step - loss: 1.0064 - categorical_accuracy: 0.7077 - val_loss: 1.0873 - val_categorical_accuracy: 0.6721
Epoch 17/100
142/142 [==============================] - 21s 151ms/step - loss: 0.8885 - categorical_accuracy: 0.7318 - val_loss: 1.1665 - val_categorical_accuracy: 0.6516
Epoch 18/100
142/142 [==============================] - 21s 148ms/step - loss: 0.8580 - categorical_accuracy: 0.7416 - val_loss: 1.3422 - val_categorical_accuracy: 0.6189
Epoch 19/100
142/142 [==============================] - 21s 151ms/step - loss: 0.7657 - categorical_accuracy: 0.7661 - val_loss: 0.9310 - val_categorical_accuracy: 0.7254
Epoch 20/100
142/142 [==============================] - 21s 148ms/step - loss: 0.7636 - categorical_accuracy: 0.7663 - val_loss: 0.9545 - val_categorical_accuracy: 0.7254
Epoch 21/100
142/142 [==============================] - 21s 148ms/step - loss: 0.7167 - categorical_accuracy: 0.7810 - val_loss: 2.0675 - val_categorical_accuracy: 0.5123
Epoch 22/100
142/142 [==============================] - 21s 150ms/step - loss: 0.7267 - categorical_accuracy: 0.7771 - val_loss: 0.8755 - val_categorical_accuracy: 0.7602
Epoch 23/100
142/142 [==============================] - 21s 150ms/step - loss: 0.6096 - categorical_accuracy: 0.8148 - val_loss: 0.8583 - val_categorical_accuracy: 0.7500
Epoch 24/100
142/142 [==============================] - 21s 150ms/step - loss: 0.6072 - categorical_accuracy: 0.8027 - val_loss: 1.0653 - val_categorical_accuracy: 0.6947
Epoch 25/100
142/142 [==============================] - 21s 148ms/step - loss: 0.5238 - categorical_accuracy: 0.8333 - val_loss: 0.8082 - val_categorical_accuracy: 0.7664
Epoch 26/100
142/142 [==============================] - 21s 148ms/step - loss: 0.4837 - categorical_accuracy: 0.8478 - val_loss: 0.8317 - val_categorical_accuracy: 0.7787
Epoch 27/100
142/142 [==============================] - 21s 149ms/step - loss: 0.4733 - categorical_accuracy: 0.8507 - val_loss: 0.7722 - val_categorical_accuracy: 0.7889
Epoch 28/100
142/142 [==============================] - 21s 150ms/step - loss: 0.4505 - categorical_accuracy: 0.8638 - val_loss: 1.0144 - val_categorical_accuracy: 0.7234
Epoch 29/100
142/142 [==============================] - 21s 148ms/step - loss: 0.4062 - categorical_accuracy: 0.8775 - val_loss: 0.7430 - val_categorical_accuracy: 0.7930
Epoch 30/100
142/142 [==============================] - 21s 151ms/step - loss: 0.3826 - categorical_accuracy: 0.8777 - val_loss: 0.7592 - val_categorical_accuracy: 0.8033
Epoch 31/100
142/142 [==============================] - 21s 150ms/step - loss: 0.3469 - categorical_accuracy: 0.8936 - val_loss: 0.8341 - val_categorical_accuracy: 0.7828
Epoch 32/100
142/142 [==============================] - 21s 149ms/step - loss: 0.3707 - categorical_accuracy: 0.8889 - val_loss: 0.7790 - val_categorical_accuracy: 0.7951
Epoch 33/100
142/142 [==============================] - 21s 148ms/step - loss: 0.3524 - categorical_accuracy: 0.8899 - val_loss: 0.8675 - val_categorical_accuracy: 0.7807
Epoch 34/100
142/142 [==============================] - 21s 149ms/step - loss: 0.2767 - categorical_accuracy: 0.9139 - val_loss: 0.7443 - val_categorical_accuracy: 0.7992
Epoch 35/100
142/142 [==============================] - 21s 149ms/step - loss: 0.2534 - categorical_accuracy: 0.9240 - val_loss: 0.8301 - val_categorical_accuracy: 0.8094
Epoch 36/100
142/142 [==============================] - 21s 148ms/step - loss: 0.2473 - categorical_accuracy: 0.9245 - val_loss: 0.7537 - val_categorical_accuracy: 0.8094
Epoch 37/100
142/142 [==============================] - 21s 149ms/step - loss: 0.2546 - categorical_accuracy: 0.9224 - val_loss: 0.7974 - val_categorical_accuracy: 0.8074
Epoch 38/100
142/142 [==============================] - 21s 148ms/step - loss: 0.2373 - categorical_accuracy: 0.9283 - val_loss: 0.8844 - val_categorical_accuracy: 0.7684
Epoch 39/100
142/142 [==============================] - 21s 149ms/step - loss: 0.2118 - categorical_accuracy: 0.9339 - val_loss: 0.7851 - val_categorical_accuracy: 0.7992
Epoch 40/100
142/142 [==============================] - 21s 149ms/step - loss: 0.1998 - categorical_accuracy: 0.9359 - val_loss: 0.8647 - val_categorical_accuracy: 0.7848
Epoch 41/100
142/142 [==============================] - 21s 149ms/step - loss: 0.1900 - categorical_accuracy: 0.9364 - val_loss: 0.7802 - val_categorical_accuracy: 0.7992
Epoch 42/100
142/142 [==============================] - 21s 148ms/step - loss: 0.1360 - categorical_accuracy: 0.9647 - val_loss: 0.7895 - val_categorical_accuracy: 0.8012
Epoch 43/100
142/142 [==============================] - 21s 148ms/step - loss: 0.1558 - categorical_accuracy: 0.9491 - val_loss: 0.8000 - val_categorical_accuracy: 0.8135
Epoch 44/100
142/142 [==============================] - 21s 147ms/step - loss: 0.1304 - categorical_accuracy: 0.9621 - val_loss: 0.7597 - val_categorical_accuracy: 0.8258
Epoch 45/100
142/142 [==============================] - 21s 147ms/step - loss: 0.1165 - categorical_accuracy: 0.9672 - val_loss: 0.8527 - val_categorical_accuracy: 0.8053
Epoch 46/100
142/142 [==============================] - 21s 148ms/step - loss: 0.1129 - categorical_accuracy: 0.9668 - val_loss: 0.9115 - val_categorical_accuracy: 0.7705
Epoch 47/100
142/142 [==============================] - 21s 145ms/step - loss: 0.1505 - categorical_accuracy: 0.9600 - val_loss: 0.7738 - val_categorical_accuracy: 0.8156
Epoch 48/100
142/142 [==============================] - 21s 147ms/step - loss: 0.1084 - categorical_accuracy: 0.9687 - val_loss: 0.8109 - val_categorical_accuracy: 0.7992
Epoch 49/100
142/142 [==============================] - 21s 148ms/step - loss: 0.1010 - categorical_accuracy: 0.9716 - val_loss: 0.9517 - val_categorical_accuracy: 0.7910
Epoch 50/100
142/142 [==============================] - 21s 147ms/step - loss: 0.1291 - categorical_accuracy: 0.9584 - val_loss: 0.8211 - val_categorical_accuracy: 0.8135
Epoch 51/100
142/142 [==============================] - 21s 147ms/step - loss: 0.1050 - categorical_accuracy: 0.9693 - val_loss: 0.8769 - val_categorical_accuracy: 0.8033
Epoch 52/100
142/142 [==============================] - 21s 149ms/step - loss: 0.3399 - categorical_accuracy: 0.9074 - val_loss: 0.8510 - val_categorical_accuracy: 0.8135
Epoch 53/100
142/142 [==============================] - 21s 149ms/step - loss: 0.0948 - categorical_accuracy: 0.9741 - val_loss: 0.8492 - val_categorical_accuracy: 0.8053
Epoch 54/100
142/142 [==============================] - 21s 148ms/step - loss: 0.1126 - categorical_accuracy: 0.9689 - val_loss: 0.7841 - val_categorical_accuracy: 0.8217
Epoch 55/100
142/142 [==============================] - 21s 149ms/step - loss: 0.0766 - categorical_accuracy: 0.9804 - val_loss: 0.8844 - val_categorical_accuracy: 0.8115
Epoch 56/100
142/142 [==============================] - 21s 147ms/step - loss: 0.0795 - categorical_accuracy: 0.9804 - val_loss: 0.8034 - val_categorical_accuracy: 0.8299
Epoch 57/100
142/142 [==============================] - 21s 147ms/step - loss: 0.0746 - categorical_accuracy: 0.9786 - val_loss: 0.8492 - val_categorical_accuracy: 0.8053
Epoch 58/100
142/142 [==============================] - 21s 148ms/step - loss: 0.0617 - categorical_accuracy: 0.9874 - val_loss: 0.8359 - val_categorical_accuracy: 0.8176
Epoch 59/100
142/142 [==============================] - 21s 147ms/step - loss: 0.0582 - categorical_accuracy: 0.9897 - val_loss: 0.8316 - val_categorical_accuracy: 0.8299
Epoch 60/100
142/142 [==============================] - 21s 145ms/step - loss: 0.0546 - categorical_accuracy: 0.9881 - val_loss: 0.8847 - val_categorical_accuracy: 0.8176
Epoch 61/100
142/142 [==============================] - 21s 147ms/step - loss: 0.0939 - categorical_accuracy: 0.9740 - val_loss: 0.8310 - val_categorical_accuracy: 0.8176
Epoch 62/100
142/142 [==============================] - 21s 147ms/step - loss: 0.0452 - categorical_accuracy: 0.9928 - val_loss: 0.8542 - val_categorical_accuracy: 0.8135
Epoch 63/100
142/142 [==============================] - 21s 147ms/step - loss: 0.0591 - categorical_accuracy: 0.9833 - val_loss: 0.8388 - val_categorical_accuracy: 0.8299
Epoch 64/100
142/142 [==============================] - 21s 148ms/step - loss: 0.0454 - categorical_accuracy: 0.9902 - val_loss: 0.8488 - val_categorical_accuracy: 0.8238
Epoch 65/100
142/142 [==============================] - 21s 149ms/step - loss: 0.0539 - categorical_accuracy: 0.9843 - val_loss: 0.9010 - val_categorical_accuracy: 0.8156
Epoch 66/100
142/142 [==============================] - 21s 148ms/step - loss: 0.0467 - categorical_accuracy: 0.9884 - val_loss: 0.8505 - val_categorical_accuracy: 0.8156
Epoch 67/100
142/142 [==============================] - 21s 148ms/step - loss: 0.0368 - categorical_accuracy: 0.9930 - val_loss: 0.8093 - val_categorical_accuracy: 0.8258
Epoch 68/100
142/142 [==============================] - 21s 148ms/step - loss: 0.0382 - categorical_accuracy: 0.9918 - val_loss: 0.8629 - val_categorical_accuracy: 0.8197
Epoch 69/100
142/142 [==============================] - 21s 146ms/step - loss: 0.0449 - categorical_accuracy: 0.9918 - val_loss: 0.8279 - val_categorical_accuracy: 0.8258
Epoch 70/100
142/142 [==============================] - 21s 148ms/step - loss: 0.0483 - categorical_accuracy: 0.9893 - val_loss: 0.8423 - val_categorical_accuracy: 0.8299
Epoch 71/100
142/142 [==============================] - 21s 150ms/step - loss: 0.0379 - categorical_accuracy: 0.9908 - val_loss: 0.8416 - val_categorical_accuracy: 0.8197
Epoch 72/100
142/142 [==============================] - 21s 150ms/step - loss: 0.0365 - categorical_accuracy: 0.9924 - val_loss: 0.9425 - val_categorical_accuracy: 0.8074
Epoch 73/100
142/142 [==============================] - 21s 148ms/step - loss: 0.0422 - categorical_accuracy: 0.9885 - val_loss: 0.8726 - val_categorical_accuracy: 0.8115
Epoch 74/100
142/142 [==============================] - 21s 149ms/step - loss: 0.0355 - categorical_accuracy: 0.9914 - val_loss: 0.8510 - val_categorical_accuracy: 0.8279
Epoch 75/100
142/142 [==============================] - 21s 148ms/step - loss: 0.0353 - categorical_accuracy: 0.9935 - val_loss: 0.8953 - val_categorical_accuracy: 0.8197
Epoch 76/100
142/142 [==============================] - 21s 146ms/step - loss: 0.0341 - categorical_accuracy: 0.9925 - val_loss: 0.9212 - val_categorical_accuracy: 0.8156
Epoch 77/100
142/142 [==============================] - 21s 147ms/step - loss: 0.0275 - categorical_accuracy: 0.9948 - val_loss: 0.8837 - val_categorical_accuracy: 0.8135
Epoch 78/100
142/142 [==============================] - 21s 148ms/step - loss: 0.0359 - categorical_accuracy: 0.9915 - val_loss: 0.8645 - val_categorical_accuracy: 0.8217
Epoch 79/100
142/142 [==============================] - 21s 147ms/step - loss: 0.0353 - categorical_accuracy: 0.9898 - val_loss: 0.8496 - val_categorical_accuracy: 0.8279
Epoch 80/100
142/142 [==============================] - 21s 137ms/step - loss: 0.0285 - categorical_accuracy: 0.9932 - val_loss: 0.8276 - val_categorical_accuracy: 0.8238
Epoch 81/100
142/142 [==============================] - 21s 147ms/step - loss: 0.0284 - categorical_accuracy: 0.9959 - val_loss: 0.8818 - val_categorical_accuracy: 0.8217
Epoch 82/100
142/142 [==============================] - 21s 149ms/step - loss: 0.0296 - categorical_accuracy: 0.9941 - val_loss: 0.8593 - val_categorical_accuracy: 0.8238
Epoch 83/100
142/142 [==============================] - 21s 149ms/step - loss: 0.0383 - categorical_accuracy: 0.9905 - val_loss: 0.8230 - val_categorical_accuracy: 0.8361
Epoch 84/100
142/142 [==============================] - 21s 149ms/step - loss: 0.0294 - categorical_accuracy: 0.9928 - val_loss: 0.8321 - val_categorical_accuracy: 0.8238
Epoch 85/100
142/142 [==============================] - 21s 148ms/step - loss: 0.0274 - categorical_accuracy: 0.9941 - val_loss: 1.0051 - val_categorical_accuracy: 0.8012
Epoch 86/100
142/142 [==============================] - 21s 149ms/step - loss: 0.0369 - categorical_accuracy: 0.9902 - val_loss: 0.8993 - val_categorical_accuracy: 0.8320
Epoch 87/100
142/142 [==============================] - 21s 148ms/step - loss: 0.0232 - categorical_accuracy: 0.9970 - val_loss: 0.8539 - val_categorical_accuracy: 0.8197
Epoch 88/100
142/142 [==============================] - 21s 148ms/step - loss: 0.0432 - categorical_accuracy: 0.9889 - val_loss: 0.8972 - val_categorical_accuracy: 0.8258
Epoch 89/100
142/142 [==============================] - 21s 147ms/step - loss: 0.0286 - categorical_accuracy: 0.9941 - val_loss: 0.9795 - val_categorical_accuracy: 0.8135
Epoch 90/100
142/142 [==============================] - 21s 147ms/step - loss: 0.0285 - categorical_accuracy: 0.9942 - val_loss: 0.8922 - val_categorical_accuracy: 0.8238
Epoch 91/100
142/142 [==============================] - 21s 149ms/step - loss: 0.0248 - categorical_accuracy: 0.9961 - val_loss: 0.8703 - val_categorical_accuracy: 0.8361
Epoch 92/100
142/142 [==============================] - 21s 148ms/step - loss: 0.0218 - categorical_accuracy: 0.9975 - val_loss: 0.8755 - val_categorical_accuracy: 0.8361
Epoch 93/100
142/142 [==============================] - 21s 147ms/step - loss: 0.0212 - categorical_accuracy: 0.9959 - val_loss: 0.8724 - val_categorical_accuracy: 0.8197
Epoch 94/100
142/142 [==============================] - 21s 149ms/step - loss: 0.0228 - categorical_accuracy: 0.9951 - val_loss: 0.8799 - val_categorical_accuracy: 0.8279
Epoch 95/100
142/142 [==============================] - 21s 148ms/step - loss: 0.0168 - categorical_accuracy: 0.9979 - val_loss: 0.8700 - val_categorical_accuracy: 0.8381
Epoch 96/100
142/142 [==============================] - 21s 146ms/step - loss: 0.0172 - categorical_accuracy: 0.9978 - val_loss: 0.9005 - val_categorical_accuracy: 0.8258
Epoch 97/100
142/142 [==============================] - 21s 146ms/step - loss: 0.0202 - categorical_accuracy: 0.9955 - val_loss: 0.8830 - val_categorical_accuracy: 0.8299
Epoch 98/100
142/142 [==============================] - 21s 148ms/step - loss: 0.0180 - categorical_accuracy: 0.9959 - val_loss: 0.9417 - val_categorical_accuracy: 0.8258
Epoch 99/100
142/142 [==============================] - 21s 148ms/step - loss: 0.0200 - categorical_accuracy: 0.9945 - val_loss: 0.9080 - val_categorical_accuracy: 0.8217
Epoch 100/100
142/142 [==============================] - 21s 148ms/step - loss: 0.0184 - categorical_accuracy: 0.9963 - val_loss: 0.9156 - val_categorical_accuracy: 0.8135

Evaluating...
{'loss': 1.4345703125, 'categorical_accuracy': 0.7154605388641357}

Saving Model...

Training Done
```

## Predicting

To predict the model run the following command:

```shell
$ python3 predict.py <image-file-name>
```

for example:

```shell
$ python3 predict.py image.jpg
```

Output:

![Gold Fish](./image.jpg)

```shell
Loading Model...
Reading Image...
Predicting...
Class: gold, Score: 1.0
```


## Links

* AlexNet: https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf
* Dataset: https://www.kaggle.com/khaledelsayedibrahim/fishclassifierfinal
