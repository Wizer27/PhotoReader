import pytesseract
from pdf2image import convert_from_path
import numpy as np
import cv2
import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("400x300")
app.title("Ввод и вывод текста")



def main():
    pdf_path = input_field.get()
    images = convert_from_path(pdf_path,dpi = 300)
    
    
    result_text = ''
    
    
    for i, image in enumerate(images):
        gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
        _, threshold_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)
        
        # 3. Распознаём текст с помощью Tesseract
        text = pytesseract.image_to_string(threshold_image, lang='rus+eng')  # Языки: русский + английский
        result_text += f"Страница {i+1}:\n{text}\n\n"
    output_label.insert("end",result_text)







def test():
    print("Working........")

input_field = ctk.CTkEntry(app, placeholder_text="Введите текст...")
input_field.pack(pady=20, padx=20)

# Кнопка
submit_button = ctk.CTkButton(app, text="Показать текст", command= main)
submit_button.pack(pady=10)

# Поле вывода
output_label = ctk.CTkTextbox(app)
output_label.pack(pady=20)

app.mainloop()
