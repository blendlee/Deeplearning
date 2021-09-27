# -*- coding: utf-8 -*-
"""2.Dense layers.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11Tc7E9BYvpU8kUwdoHZJg6tYyRIZJg-B

# 2-1 Dense Layers

## Code 2-1-1 Shapes of Dense Layers
"""

import tensorflow as tf

from tensorflow.keras.layers import Dense

N, n_feature = 8, 10
X = tf.random.normal(shape=(N,n_feature))

n_neuron = 3
dense = Dense(units=n_neuron, activation = 'sigmoid')
Y= dense(X)

W,B = dense.get_weights()

print('======= Input/Weight/Bias =======')

print('X : ',  X.shape)
print('W : ',  W.shape)
print('B : ',  B.shape)
print('Y : ',  Y.shape)

print(X)
print(W)



"""## Code 2-1-2 Output Calculation"""

import tensorflow as tf
import numpy as np

from tensorflow.math import exp
from tensorflow.linalg import matmul
from tensorflow.keras.layers import Dense

N, n_feature = 4, 10
X = tf.random.normal(shape=(N,n_feature))

n_neuron = 3
dense = Dense(units=n_neuron, activation = 'sigmoid')
Y_tf= dense(X)

W,B = dense.get_weights()

print("Y(Tensorflow) : \n" , Y_tf.numpy())

# calculate with matrix multiplication
Z = matmul(X, W) +B
Y_man_matmul = 1/(1+exp(-Z))
print("Y(with matrix multiplication : \n" , Y_man_matmul.numpy())

#cacluate with dot products
Y_man_vec = np.zeros(shape=(N,n_neuron))
print(Y_man_vec)

for x_idx in range(N):
  x = X[x_idx]

  for nu_idx in range(n_neuron):
    w,b = W[:,nu_idx] , B[nu_idx]

    z = tf.reduce_sum(x*w) +b
    a = 1/(1+exp(-z))
    Y_man_vec[x_idx,nu_idx] = a

print('Y(with dot products: \n' , Y_man_vec)

"""# 2-2 Cascaded Dense Layers

## Code 2-2-1 Shapes of Cascaded Dense Layers
"""

import tensorflow as tf

from tensorflow.keras.layers import Dense

N,n_feature = 4,10

X= tf.random.normal(shape=(N,n_feature))

n_neurons = [3,5] # 두개의 뉴런
dense1=Dense(units=n_neurons[0], activation= 'sigmoid')

dense2=Dense(units=n_neurons[1], activation= 'sigmoid')

#forward propagation
A1=dense1(X)
Y= dense2(A1)

#get weight,bias

W1, B1 = dense1.get_weights()
W2, B2 = dense2.get_weights()

print('X: {}\n'.format(X.shape))

print('W1 :' , W1.shape)
print('B1 :' , B1.shape)
print('A1: {}\n'.format(A1.shape))

print('W2 :', W2.shape)
print('B2 :' ,B2.shape)
print('Y: {}\n'.format(Y.shape))

"""## Code 2-2-2 Dense Layers with Python List"""

import tensorflow as tf

from tensorflow.keras.layers import Dense

N,n_feature = 4,10

X= tf.random.normal(shape=(N,n_feature))

n_neurons = [10,20,30,40,50,60,70,80,90,100]

dense_layers=list()

for n_neuron in n_neurons:
  dense = Dense(units=n_neuron, activation='relu')
  dens_layers.append(dense)

print('Input :' , X.shape)
for dense_idx,dense in enumerate(dense_layers):
  X = dense(X)
  print('After dense layer : ', dense_idx)
  print(X.shape, '\n')

Y=X

"""## Code 2-2-3 Output Calculations"""

import tensorflow as tf

from tensorflow.math import exp
from tensorflow.linalg import matmul
from tensorflow.keras.layers import Dense

N,n_feature = 4,10

X= tf.random.normal(shape=(N,n_feature))
X_cp = tf.identity(X)
n_neurons = [10,20,30]

dense_layers=list()
for n_neuron in n_neurons:
  dense = Dense(units=n_neuron, activation='sigmoid')
  dense_layers.append(dense)


print('Input :' , X.shape)

#fowrd propagetion(Tensorflow)
W,B =list(), list()
for dense_idx,dense in enumerate(dense_layers):
  X = dense(X)
  w,b = dense.get_weights()

  W.append(w)
  B.append(b)

print("Y(Tensorflow) \n: ",X.numpy())

#fowrd propagation(Manual)

for layer_idx in range(len(n_neurons)):
  w, b = W[layer_idx] , B[layer_idx]

  X_cp = matmul(X_cp,w)+b
  X_cp = 1/(1+exp(-X_cp))
print("Y(Manual) \n: ",X.numpy())

"""#2-3 Model Implementation

## Code 2-3-1 Model Implementation with Sequential Method
"""

from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

n_nerons= [10,20]

model = Sequential() #dense layer를 쌓을 틀 형성
for n_neuron in n_nuerons :
  model.add(Dense(units=n_neuron , activation='sigmoid')) # 첫번째 layer에 뉴련 10개 삽입

"""## Code 2-3-2 Model Implementation with Model-subclassing"""

from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Model

class TestModel(Model):
  def __init__(self):
    super(TestModel, self).__init__()

    self.dense1=Dense(units=n_neuron , activation='sigmoid')
    self.dense2=Dense(units=n_neuron , activation='sigmoid')

model = TestModel()
print(model.dense1)
print(model.dense2)

"""## Code 2-3-3 Foward Propagtion Models

"""

import tensorflow as tf
from tensorflow.keras.models import Model


from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential


X = tf.random.normal(shape=(4,10))

#### Sequential Method
n_nerons= [10,20]
model = Sequential() #dense layer를 쌓을 틀 형성
for n_neuron in n_nuerons :
  model.add(Dense(units=n_neuron , activation='sigmoid'))

Y = model(X)
print(Y.numpy())


#### Subclassing Method
class TestModel(Model):
  def __init__(self):
    super(TestModel, self).__init__()
    self.dense1=Dense(units=n_neuron , activation='sigmoid')
    self.dense2=Dense(units=n_neuron , activation='sigmoid')

  def call(self,x):
    x = self.dense1(x)
    x = self.dense2(x)
    return x


model = TestModel()
Y = model(X)

class TestModel(Model):
  def __init__(self, n_neurons):
    super(TestModel, self).__init__()
    self.n_neurons = n_neuron

    self.dense_layers = list()
    for n_neuron in self.n_neurons :
      self.dense_layers.append(Dense(units=n_neuron , activation='sigmoid'))

  def call(self,x):
    for dense in self.dense_layers:
      x = dense(x)

    return x


n_neurons = [3,4,5]
model = TestModel(n_neurons)
Y = model(X)

"""## Code 2-3-4  Layers in Models"""

import tensorflow as tf

from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

X= tf.random.normal(shape=(4,10))

model = Sequential()
model.add(Dense(units=10, activation='sigmoid'))
model.add(Dense(units=20, activation='sigmoid'))

Y=model(X)

print(type(model.layers))
print(model.layers)

dense1 = model.layers[0]

for tmp in dir(dense1):
  print(tmp)

"""## Code 2-3-5 Trainable Variables in Models"""

import tensorflow as tf

from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

X= tf.random.normal(shape=(4,10))

model = Sequential()
model.add(Dense(units=10, activation='sigmoid'))
model.add(Dense(units=20, activation='sigmoid'))

Y=model(X)


print(type(model.trainable_variables))
print(len(model.trainable_variables))

for train_var in model.trainable_variables:
  print(train_var.shape)
  ### model 안의 weight, bias