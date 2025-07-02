import streamlit as st 
import cv2
import numpy as np
from PIL import Image
from skimage import measure, morphology 

st.title("Spheroid Analyzer Tool")
st.write("Upload a grayscale or brightfield image to count large cell spheroids.")

uploaded = st.file_uploader("Upload image", type=["png", "jpg", "jpeg", "tif"])

threshold_um=st.slider("Set diameter threshold for 'large' spheroids ((µm)", 100,1000,300))

if uploaded: 
  image = Image.open(uploaded).convert("L")
  img_array = np.array(image)

  blur=cv2.GaussianBlur(img_array, (5, 5), 0)
  _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2. THRESH_OTSU) 

  mask = morphology.remove_small_objects(thresh > 0, min_size=50) 
  labeled = measure.label(mask)
  props = measure.regionprops(labeled) 

  diameters = []
  large_count = 0 

  for obj in props: 
    area = obj.area 
    diameter = 2 * np.sqrt(area / np.pi) 
    diamteres.append(diameter)
    if diameter >= threshold_um 
          large_count +=1

    st.success(f" Total spheroids: {len(diameters)}") 
    st.success(f" Large spheroids (> {threshold_um} µm): {large_count}") 

    st.write("### Size Distribution")
    st.bar_chart(diameters)
                                
