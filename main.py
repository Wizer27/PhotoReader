import pytesseract
from pdf2image import convert_from_path
import numpy as np
import cv2
import streamlit as st
import tempfile
import os
os.environ["OPENCV_IO_ENABLE_OPENEXR"] = "1" 

 
result_text = ''
st.title("Text from any pdf (ONLY FOR PDF)")


a = st.file_uploader("Chose a file")

if a is not None:
    name = a.name
    print(f"Name: {name}")
    n = name.split('.')
    if n[1] == 'pdf':
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(a.getvalue())  # Сохраняем содержимое загруженного файла
            pdf_path = tmp_file.name 
        try:
                
            images = convert_from_path(pdf_path,dpi = 300)
            
            
            for i, image in enumerate(images):
                gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
                _, threshold_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)
                
                # 3. Распознаём текст с помощью Tesseract
                text = pytesseract.image_to_string(threshold_image, lang='rus+eng')  # Языки: русский + английский
                result_text += f"Страница {i+1}:\n{text}\n\n" 
            r = st.text_area('Result',value = result_text)
            st.success('All done !')
        except FileNotFoundError:    
            st.error("This file doesnt exist on your computer")    

print(a)
print(result_text)
