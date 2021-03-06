# -*- coding: utf-8 -*-
"""6. Pooling layer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fPCqAZG3cZ2T16TH2lYhF-WhN_aw9BMe
"""



"""# 6-1 Max/Avg Pooling

## Code 6-1-1 Max Pooling
"""

import numpy as np
import tensorflow as tf


from tensorflow.keras.layers import MaxPooling1D

L, f ,s = 10, 2, 1

x=tf.random.normal(shape=(1,L,1))
pool_max = MaxPooling1D(pool_size =f, strides=s)
pooled_max = pool_max(x)

print('x: {} \n{}' . format(x.shape, x.numpy().flatten()))
print('pooled_max(Tensorflow): {} \n {} ' .format(pooled_max.shape,pooled_max.numpy().flatten()))


x=x.numpy().flatten()
pooled_max_man = np.zeros((L-f+1, ))
for i in range(L-f+1):
  window = x[i:i+f]
  pooled_max_man[i]= np.max(window)

print('pooled_max(Manual): {} \n {}' .format(pooled_max_man.shape, pooled_max_man))

"""## Code 6-1-2 Average Pooling"""

import numpy as np
import tensorflow as tf


from tensorflow.keras.layers import AveragePooling1D

L, f ,s = 10, 2, 1

x=tf.random.normal(shape=(1,L,1))
pool_avg = AveragePooling1D(pool_size =f, strides=s)
pooled_avg = pool_avg(x)

print('x: {} \n{}' . format(x.shape, x.numpy().flatten()))
print('pooled_avg(Tensorflow): {} \n {} ' .format(pooled_avg.shape,pooled_avg.numpy().flatten()))


x=x.numpy().flatten()
pooled_avg_man = np.zeros((L-f+1, ))
for i in range(L-f+1):
  window = x[i:i+f]
  pooled_avg_man[i]= np.mean(window)

print('pooled_avg(Manual): {} \n {}' .format(pooled_avg_man.shape, pooled_avg_man))

"""#6-2 2D Max/Avg Pooling

## Code 6-2-1 2D Max Pooling
"""

import numpy as np
import tensorflow as tf

from tensorflow.keras.layers import MaxPooling2D

N,n_H,n_W,n_C = 1, 5, 5, 1

f, s=2,1

x=tf.random.normal(shape=(N,n_H,n_W,n_C))
pool_max = MaxPooling2D(pool_size =f , strides =s)
pooled_max = pool_max(x)

print('x: {} \n{}' . format(x.shape, x.numpy().squeeze()))
print('pooled_max(Tensorflow): {} \n {} ' .format(pooled_max.shape,pooled_max.numpy().squeeze()))


x= x.numpy().squeeze()
pooled_max_man =np.zeros(shape=(n_H -f +1, n_W -f +1))

for i in range(n_H-f+1):
  for j in range(n_W -f +1):
    window = x[i:i+f,j:j+f]
    pooled_max_man[i,j]=np.max(window)

print('pooled_max(Manual): {} \n {}' .format(pooled_max_man.shape, pooled_max_man))

"""## Code 6-2-2 2D Average Pooling"""

import numpy as np
import tensorflow as tf

from tensorflow.keras.layers import AveragePooling2D

N,n_H,n_W,n_C = 1, 5, 5, 1

f, s=2,1

x=tf.random.normal(shape=(N,n_H,n_W,n_C))
pool_avg = AveragePooling2D(pool_size =f , strides =s)
pooled_avg = pool_max(x)

print('x: {} \n{}' . format(x.shape, x.numpy().squeeze()))
print('pooled_avg(Tensorflow): {} \n {} ' .format(pooled_avg.shape,pooled_avg.numpy().squeeze()))


x= x.numpy().squeeze()
pooled_avg_man =np.zeros(shape=(n_H -f +1, n_W -f +1))

for i in range(n_H-f+1):
  for j in range(n_W -f +1):
    window = x[i:i+f,j:j+f]
    pooled_avg_man[i,j]=np.mean(window)

print('pooled_avg(Manual): {} \n {}' .format(pooled_avg_man.shape, pooled_avg_man))

"""#6-3 3D Max/Avg Pooling

## Code 6-3-1 3D Max Pooling
"""

import math
import numpy as np
import tensorflow as tf

from tensorflow.keras.layers import MaxPooling2D

N, n_H, n_W, n_C =1,5,5,3

f, s = 2, 2

x = tf.random.normal(shape=(N, n_H, n_W, n_C))
print('x : {}\n {}' .format(x.shape,np.transpose(x.numpy().squeeze(), (2,0,1))))

pool_max = MaxPooling2D(pool_size=f, strides=s)
pooled_max =pool_max(x)

pooled_max_t = np.transpose(pooled_max.numpy().squeeze(), (2,0,1))

print('Pooled_max(Tensorflow): {} \n {}' .format(pooled_max.shape, pooled_max_t))

###

x= x.numpy().squeeze()

n_H_ = math.floor((n_H-f)/s +1)
n_W_ = math.floor((n_W-f)/s +1)

pooled_max_man = np.zeros(shape=(n_H_,n_W_,n_C))

for c in range(n_C):
  c_image = x[:,:,c]

  h_ =0
  for h in range(0,n_H-f+1,s):
    w_ =0
    for w in range(0,n_W-f+1,s):
      window= c_image[h:h+f,w:w+f]
      pooled_max_man[h_,w_,c] = np.max(window)

      w_ +=1
    h_ +=1
pooled_max_t = np.transpose(pooled_max_man, (2,0,1))
print('pooled_max(Manual): {} \n {}' .format(pooled_max_man.shape,pooled_max_t))

"""# 6-4 Padding

## Code 6-4-1 ZeroPadding 2D Layer
"""

import tensorflow as tf
from tensorflow.keras.layers import ZeroPadding2D

images = tf.random.normal(shape=(1,3,3,3))
print(images.shape)
print(np.transpose(images.numpy().squeeze(),(2,0,1)))


zero_padding =ZeroPadding2D(padding=1)

y= zero_padding(images)
print(y.shape)
print(np.transpose(y.numpy().squeeze(),(2,0,1)))

"""## Code 6-4-2 ZeroPadding with Conv2D Layer"""

import tensorflow as tf

from tensorflow.keras.layers import Conv2D

images = tf.random.normal(shape=(1,3,3,3))
conv =Conv2D(filters=1, kernel_size=3,padding='same')
y = conv(images)
print(y.shape)

"""# 6-5 Strides

## Code 6-5-1 Strides in Conv2D Layers
"""

import tensorflow as tf

from tensorflow.keras.layers import Conv2D


images = tf.random.normal(shape=(1,3,3,3))
conv =Conv2D(filters=1, kernel_size=3,padding='valid' , strides=2)

y=conv(images)

print(images.shape)
print(y.shape)

"""## Code 6-5-2 Strides in Pooling Layers"""

import tensorflow as tf

from tensorflow.keras.layers import MaxPooling2D


images = tf.random.normal(shape=(1,3,3,3))
pool =MaxPooling2D(pool_size =3, strides=2)

y=pool(images)

print(images.shape)
print(y.shape)

