# what do these do?
from __future__ import absolute_import, division, print_function, unicode_literals

# I assume this is importing and abbreviating the prefix for tensorflow
import tensorflow as tf

# importing the high-level api for the low-level system?
from tensorflow import keras

# from the high-level api, get the structure for layers in the network
from tensorflow.keras import layers

#########################################################################################
# build a simple model

# a model is (usually) a bunch of layers
model = tf.keras.Sequential()

# add a densely-connected layer with 64 units
model.add(layers.Dense(64, activation='relu'))

# add another layer of the same type
model.add(layers.Dense(64, activation='relu'))

# add an output layer with 10 units
model.add(layers.Dense(10))

#########################################################################################
# set up training

model.compile(  optimizer = tf.keras.optimizers.Adam(0.01),
                loss = tf.keras.losses.CategoricalCrossentropy(from_logits=True),
                metrics = ['accuracy'])
