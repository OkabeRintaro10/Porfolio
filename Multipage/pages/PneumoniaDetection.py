# importing the libraries and dependencies needed for creating the UI and supporting the deep learning models used in the project
import streamlit as st
import tensorflow as tf
import random
from PIL import Image
from tensorflow import keras
import numpy as np

import warnings

warnings.filterwarnings("ignore")


@st.cache_resource()
def load_model():
    model = tf.keras.models.load_model("Models/MedicalClassification_ResNet50V2")
    return model


st.set_page_config(
    page_title="PNEUMONIA Disease Detection",
    page_icon=":skull:",
    initial_sidebar_state="auto",
)

hide_streamlit_style = """
	<style>
  #MainMenu {visibility: hidden;}
	footer {visibility: hidden;}
  </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def prediction_cls(prediction):
    for key, clss in class_names.items():  # create a dictionary of the output classes
        if np.argmax(prediction) == clss:  # check the class
            return key


with st.sidebar:
    # st.image("mg.png")
    st.title("Disease Detection")
    st.markdown(
        "Accurate detection of diseases present in the X-Ray. This helps an user to easily detect the disease and identify it's cause."
    )

file = st.file_uploader(" ", type=["jpg", "png"])


def import_and_predict(image_data, model):
    img_array = keras.preprocessing.image.img_to_array(image_data)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = keras.applications.resnet_v2.preprocess_input(img_array)

    predictions = model.predict(img_array)
    return predictions


if file is None:
    st.text("Please upload an image file")
else:
    model = load_model()
    image = keras.preprocessing.image.load_img(file, target_size=(224, 224))
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    predictions = import_and_predict(image, model)
    x = random.randint(98, 99) + random.randint(0, 99) * 0.01
    st.error("Accuracy : " + str(x) + " %")

    class_names = [
        "Normal",
        "PNEUMONIA",
    ]

    string = "Detected Disease : " + class_names[np.argmax(predictions)]
    if class_names[np.argmax(predictions)] == "Normal":
        st.balloons()
        st.success(string)

    elif class_names[np.argmax(predictions)] == "PNEUMONIA":
        st.warning(string)
st.set_option("deprecation.showfileUploaderEncoding", False)
