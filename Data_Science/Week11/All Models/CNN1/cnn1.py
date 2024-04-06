import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Set seed for reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# Define directories
train_dir = 'C:/Users/meetp/Downloads/fracture_dataset/train'
validation_dir = 'C:/Users/meetp/Downloads/fracture_dataset/test'
test_dir = 'C:/Users/meetp/Downloads/fracture_dataset/train'

# Image dimensions
img_width, img_height = 150, 150
input_shape = (img_width, img_height, 3)

# Parameters
epochs = 20
batch_size = 32

# Data augmentation for training images
train_datagen = ImageDataGenerator(rescale=1./255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

# Rescaling for validation and test images
valid_test_datagen = ImageDataGenerator(rescale=1./255)

# Load and augment training images
train_generator = train_datagen.flow_from_directory(train_dir,
                                                    target_size=(img_width, img_height),
                                                    batch_size=batch_size,
                                                    class_mode='binary')

# Load validation images
validation_generator = valid_test_datagen.flow_from_directory(validation_dir,
                                                               target_size=(img_width, img_height),
                                                               batch_size=batch_size,
                                                               class_mode='binary')

# Load test images
test_generator = valid_test_datagen.flow_from_directory(test_dir,
                                                        target_size=(img_width, img_height),
                                                        batch_size=batch_size,
                                                        class_mode='binary')

# Define the CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(train_generator,
          steps_per_epoch=train_generator.samples // batch_size,
          epochs=epochs,
          validation_data=validation_generator,
          validation_steps=validation_generator.samples // batch_size)

# Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(test_generator, steps=test_generator.samples // batch_size)
print("Test Accuracy:", test_accuracy)

# Save the model
model.save('fracture_detection_model.h5')
