import streamlit as st
import util

import base64
from PIL import Image
import io


st.write("""
# Facial Hair Classifier

Upload an image of face with facial hair and let us classify them!

""")




def predict():


    imagefile = st.sidebar.file_uploader("Upload the image",type=["png","jpg","jpeg"])

    if imagefile != None:

        image_b64 = base64.b64encode(imagefile.read())




        util.load_saved_artifacts()



        predicted = util.classify_image(image_b64, None)

    else:
        predicted = 0

    return predicted

st.subheader("Prediction")
st.write(predict())