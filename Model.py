from keras.layers import Conv2D, Dense, \
    MaxPooling2D, UpSampling2D, merge, Reshape
from keras.models import Sequential
from keras.layers.advanced_activations import LeakyReLU
import numpy as np

class Model:

    def __init__(self, n_in, out_dim, n_dense = 4, dense_activation = 'sigmoid', n_conv = 4, conv_activation = LeakyReLU, n_upsample = 4):
        self.model = Sequential()

        self.model.add(Dense(512, input_shape = (n_in,) ))
        
        for _ in range(n_dense):
            self.model.add(Dense(529, activation = dense_activation))
        self.model.add(Reshape((23,23,1)))
        for i in range(n_conv):
            if i < n_upsample:
                self.model.add(UpSampling2D())
            self.model.add(Conv2D(filters = out_dim[-1], kernel_size = (5,5), padding = 'same', strides = (1,1)))
            self.model.add(Conv2D(filters = out_dim[-1], kernel_size = (3,3), padding = 'same', strides = (1,1)))
            
        self.model.compile(optimizer = 'adagrad', loss = 'mean_squared_error')
    
    def train(self, inputs, outputs, n_iterations = 100):
        inputs = np.array([inputs])
        outputs = np.array([outputs])
        self.model.fit(inputs, outputs, epochs = n_iterations)
    def generate(self, inputs):
        inputs = np.array([inputs])
        return self.model.predict(inputs)
