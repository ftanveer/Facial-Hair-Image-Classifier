import streamlit as st
import util

import base64
from PIL import Image
import io


st.write("""
# Facial Hair Classifier

Upload an image of face with facial hair and let us classify them!

""")

st.subheader("##Prediction")
st.write(predict())

st.write("""
The following styles of facial hair can be recognized at the moment.
More styles will be added in the near future
""")

image_1 = Image.open('Chevron.png')

st.image(image_1, caption='Chevron Moustache')

image_2 = Image.open('handlebar.jpeg')

st.image(image_2, caption='Handlebar Moustache')

image_3 = Image.open('Horseshoe.png')

st.image(image_3, caption='Horseshoe Moustache')

image_4 = Image.open('Toothbrush.png')

st.image(image_4, caption='Toothbrush Moustache')

image_5 = Image.open('Pencil.png')

st.image(image_5, caption='Pencil Moustache')

def predict():


    imagefile = st.sidebar.file_uploader("Upload the image",type=["png","jpg","jpeg"])

    if imagefile != None:

        image_b64 = base64.b64encode(imagefile.read())




        util.load_saved_artifacts()



        predicted = util.classify_image(image_b64, None)

    else:
        predicted = 0

    return predicted

