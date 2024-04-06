import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt

# Load the model
model = load_model('D:/Pycharm_Projects/Data_Science_Internship/Data Science/Week11/All Models/CNN1/fracture_detection_model.h5')  # Load the model you saved

# Define the classes
classes = ['fractured', 'not fractured']

def predict(image_path):
    print("Loading and preprocessing image...")
    img = image.load_img('C:/Users/meetp/Downloads/download.jpeg', target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize the image
    print("Image loaded and preprocessed. Shape:", img_array.shape)

    print("Making prediction...")
    prediction = model.predict(img_array)
    print("Prediction received. Shape:", prediction.shape)

    predicted_class = classes[int(np.round(prediction)[0][0])]
    return predicted_class


# Streamlit app
def main():
        img = Image.open('C:/Users/meetp/Downloads/download.jpeg') # image path

        # Make a prediction
        predicted_class = predict(img)
        print('Prediction:', predicted_class)
        plt.imshow(img)

if __name__ == '__main__':
    main()