from PIL import Image
import numpy as np
import streamlit as st
st.set_option('deprecation.showfileUploaderEncoding', False)

uploaded_file = st.file_uploader("Choose a image file", type=['png', 'jpg', 'jpeg'] )

if uploaded_file is not None:
    # Convert the file to an opencv image.

    image = Image.open(uploaded_file)
    show = st.image(image,width=300)  


if st.button("Click Here"):
    st.write("Process somethimg")
    # show.image(image,width=600)  
    st.image(image,width=600)  