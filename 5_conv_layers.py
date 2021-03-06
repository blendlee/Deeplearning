# -*- coding: utf-8 -*-
"""5. Conv Layers.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_7ypVAQvhDo7bWqNzBCtffWW6tqgapva
"""



"""# 5-1 Conv Layers

## Code 5-1-1 Shapes of Conv Layers
"""

import tensorflow as tf

from tensorflow.keras.layers import Conv2D

N, n_H, n_W, n_C = 32, 28, 28, 5
n_filter =10
k_size=3


images = tf.random.uniform(minval=0, maxval=1, shape=((N,n_H,n_W,n_C)))

conv = Conv2D(filters= n_filter, kernel_size= k_size)

y = conv(images)

W, B = conv.get_weights()

print(images.shape)
print(W.shape)
print(B.shape)
print(y.shape)

"""## Code 5-1-2 Correlation Calculation"""

import numpy as np
import tensorflow as tf

from tensorflow.keras.layers import Conv2D


N, n_H, n_W, n_C = 1, 28, 28, 1
n_filter =1
k_size=3


images = tf.random.uniform(minval=0, maxval=1, shape=((N,n_H,n_W,n_C)))

conv = Conv2D(filters= n_filter, kernel_size= k_size)

y = conv(images)
print("Y(Tensorflow) : \n" , y.numpy().squeeze().shape)
W, B = conv.get_weights()

#####
images = images.numpy().squeeze()
W= W.squeeze()

y_man = np.zeros(shape=(n_H - k_size +1, n_W - k_size +1))

for i in range(n_H -k_size +1):
  for j in range(n_W - k_size +1):
    window = images[i:i+k_size , j : j + k_size]
    y_man[i,j] = np.sum(window+W)+B

print('Y(manual) :  \n' ,y_man)



"""## Code 5-1-3 Correlation with n-channel"""

import numpy as np
import tensorflow as tf

from tensorflow.keras.layers import Conv2D


N, n_H, n_W, n_C = 1, 5, 5, 3
n_filter =1
k_size=3


images = tf.random.uniform(minval=0, maxval=1, shape=((N,n_H,n_W,n_C)))

conv = Conv2D(filters= n_filter, kernel_size= k_size)

y = conv(images)
print("Y(Tensorflow) : \n" , y.numpy().squeeze())
W, B = conv.get_weights()

#####
images = images.numpy().squeeze()
W= W.squeeze()

y_man = np.zeros(shape=(n_H - k_size +1, n_W - k_size +1))

for i in range(n_H -k_size +1):
  for j in range(n_W - k_size +1):
    window = images[i:i+k_size , j : j + k_size :]
    y_man[i,j] = np.sum(window*W)+B

print('Y(manual) :  \n' ,y_man)

"""# 5-2 Conv Layer with Filters

## Code 5-2-1 Shapes with Filters
"""

import tensorflow as tf

from tensorflow.keras.layers import Conv2D

N, n_H,n_W,n_C = 1, 28, 28, 3

n_filter = 5
f_size = 3

images =tf.random.uniform(minval=0,maxval=1 , shape=(N,n_H,n_W,n_C))

conv = Conv2D(filters=n_filter, kernel_size = k_size)
Y = conv(images)
W, B = conv.get_weights()

print( "Input Image : {} ". format(images.shape))
print("W/B {} / {} ". format(W.shape, B.shape))
print( "Output Umage : {}" . format(Y.shape))

"""## Code 5-2-2 Computations with Filters"""

import numpy as np
import tensorflow as tf

from tensorflow.keras.layers import Conv2D


N, n_H,n_W,n_C = 1, 5, 5, 3

n_filter = 4
k_size = 4

# foward propagtion(Tensorflow)
images =tf.random.uniform(minval=0,maxval=1 , shape=(N,n_H,n_W,n_C))

conv = Conv2D(filters=n_filter, kernel_size = k_size)
Y = conv(images)

print(Y.shape)
print(Y.numpy().shape)
print(Y.numpy().squeeze().shape)

Y = np.transpose(Y.numpy().squeeze(), (2,0,1))
print("Y(Tensorflow) :  \n" , Y)


# Forward Propagation Manual

W , B = conv.get_weights()
print(images.shape)
images = images.numpy().squeeze()
print(W.shape, B.shape)

Y_man = np.zeros(shape=(n_H -k_size +1 , n_W -k_size +1, n_filter))
for c in range(n_filter):
  c_W = W[:, :, :, c]
  c_b = B[c]

  print(c_W.shape,c_b.shape)

  for h in range(n_H -k_size +1):
    for j in range(n_W -k_size +1):
      window = images[h:h+k_size, j:j+k_size, :]
      conv = np.sum(window*c_W) +c_b
      Y_man[h,j,c] = conv

print('Y(Manual) : \n', np.transpose(Y_man,(2,0,1)))

import numpy as np


images = np.random.randint(low=0, high=10, size = (2,3,4))

for c in range(4):
  print(images[:,:,c])

print('\n')

tmp = np.transpose(images, (2,0,1)) # ?????? ????????????
print(temp.shape)
for c in range(4):
  print(tmp[c, :, :])

"""# 5-3 Conv Layers with Activation Functions

## Code 5-3-1 Conv Layers with Activation Functions
"""

import numpy as np
import tensorflow as tf

from tensorflow.keras.layers import Conv2D


N, n_H,n_W,n_C = 1, 5, 5, 3

n_filter = 4
k_size = 4

# foward propagtion(Tensorflow)
images =tf.random.uniform(minval=0,maxval=1 , shape=(N,n_H,n_W,n_C))

conv = Conv2D(filters=n_filter, kernel_size = k_size, activation='sigmoid')
Y = conv(images)

print(Y.shape)
print(Y.numpy().shape)
print(Y.numpy().squeeze().shape)

Y = np.transpose(Y.numpy().squeeze(), (2,0,1))
print("Y(Tensorflow) :  \n" , Y)


# Forward Propagation Manual

W , B = conv.get_weights()
print(images.shape)
images = images.numpy().squeeze()
print(W.shape, B.shape)

Y_man = np.zeros(shape=(n_H -k_size +1 , n_W -k_size +1, n_filter))
for c in range(n_filter):
  c_W = W[:, :, :, c]
  c_b = B[c]

  print(c_W.shape,c_b.shape)

  for h in range(n_H -k_size +1):
    for j in range(n_W -k_size +1):
      window = images[h:h+k_size, j:j+k_size, :]
      conv = np.sum(window*c_W) +c_b
      conv = 1/(1+np.exp(-conv))
      Y_man[h,j,c] = conv

print('Y(Manual) : \n', np.transpose(Y_man,(2,0,1)))

"""# 5-4 Models with Conv Layers

## Code 5-4-1 Models with Sequential Method
"""

import tensorflow as tf
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.models import Sequential

n_neurons = [10,20,30]

model = Sequential()
model.add(Conv2D(filters = n_neurons[0], kernel_size=3, activation='relu'))
model.add(Conv2D(filters = n_neurons[1], kernel_size=3,activation='relu'))
model.add(Conv2D(filters = n_neurons[2], kernel_size=3,activation='relu'))

x= tf.random.normal(shape=(32,28,28,3))
predictions = model(x)

print('Input: {} '.format(x.shape))
print('Output: {} '.format(predictions.shape))


for layer in model.layers:
  W, B = layer.get_weights()
  print(W.shape, B.shape)
  print(layer)
trainable_variables = model.trainable_variables

for train_var in trainable_variables:
  print(type(train_var))

"""## Code 5-4-2 Models with Model Sub-classing"""

import tensorflow as tf

from tensorflow.keras.layers import Conv2D
from tensorflow.keras.models import Model
n_neurons = [10,20,30]

class TestModel(Model):
  def __init__(self):
    super(TestModel,self).__init__()
    global n_neurons

    self.conv_layers = []

    for n_neuron in n_neurons:
      self.conv_layers.append(Conv2D(filters = n_neuron, kernel_size=3,activation='relu'))

  def call(self,x):
    print('Input : ' , x.shape)

    print('\n ======== Conv Layers ======== \n')
    for conv_layer in self.conv_layers:
      x= conv_layer(x)
      W, B = conv_layer.get_weights()
      print(' W/B : {} / {} '.format(W.shape, B.shape))
      print('X; {} \n' . format(x.shape))
    return x

model=TestModel()
x= tf.random.normal(shape=(32,28,28,3))
predictions = model(x)

