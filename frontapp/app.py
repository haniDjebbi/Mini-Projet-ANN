from pydoc import doc
import tensorflow as tf
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import streamlit as st
import h5py
image = Image.open('doc2.jpg')
st.image(image)
st.title("Mammogram image classification system using deep learning")
st.header("Convolutional neural networks Model")
st.text("Made by Abidi Raja & Zohra Trabelsi & Djebbi Hani")
# Load the model
def teachable_machine_classification(img, keras_model):
    model = load_model('cnn_model-softmaxoutput1.h5')
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch
    prediction = model.predict(img_array)
    score = tf.nn.softmax(prediction[0])
    return score # return position of the highest probability


uploaded_file = st.file_uploader("Upload the FNA biopsied image ...", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded image', use_column_width=True)
    with st.spinner('Wait for it...'):
        score = teachable_machine_classification(image, 'cnn_model-softmaxoutput1.h5')
    class_names=['benign', 'malignant', 'normal']
    result = "This image most likely belongs to {} with a {:.2f} percent confidence.".format(class_names[np.argmax(score)], 100 * np.max(score))
    st.info(result, icon="ℹ️")
    st.balloons()
        