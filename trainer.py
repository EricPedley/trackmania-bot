import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

width=160
height=int(9/16*width)

model = keras.Sequential()#layers=[
#model.add(layers.Input(shape=(height,width,1)))
model.add(layers.Conv2D(32, 2, input_shape=(height,width,1), activation="relu",strides=2, padding="same"))
#model.add(layers.MaxPooling2D(pool_size=(2,2)))
model.add(layers.Flatten())
model.add(layers.Dense(4,activation="sigmoid"))

model.compile(
    optimizer=keras.optimizers.Adam(0.0001),
    loss=keras.losses.MeanSquaredError(),
    metrics=["accuracy"]
)
print(model.summary())
data = np.load("data.npy")

inputs = np.reshape(data[:,4:],(len(data),height,width))
inputs = np.expand_dims(inputs,axis=3)
outputs = data[:,0:4]
print(inputs.shape)
# import cv2 as cv
# for screenshot in outputs:
#     cv.imshow("bruh",screenshot/255)
#     if cv.waitKey(0) == ord('q'):
#         cv.destroyAllWindows()
#         break

train_dataset = tf.data.Dataset.from_tensors((inputs,outputs))
BATCH_SIZE = 10
SHUFFLE_BUFFER_SIZE = 10

train_dataset = train_dataset.shuffle(SHUFFLE_BUFFER_SIZE).batch(BATCH_SIZE)

model.fit(inputs,outputs,epochs=5)#train_dataset,epochs=5)

