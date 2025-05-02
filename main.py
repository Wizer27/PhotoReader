import customtkinter as ctk
#from easyocr import Reader
from pypdf import PdfReader
# Настройки темы
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")  # Можно заменить на 'black'

# Главное окно
app = ctk.CTk()
app.geometry("400x300")
app.title("Ввод и вывод текста")

# Функция обработки ввода
def on_click():
    name = input_field.get()
    if 'pdf' in  name:
        reader = PdfReader(name)
        t = ''
        for page in reader.pages:
            t += page.extract_text()
        print(t)
        
    output_label.configure(text= t)

# Поле ввода
input_field = ctk.CTkEntry(app, placeholder_text="Введите текст...")
input_field.pack(pady=20, padx=20)

# Кнопка
submit_button = ctk.CTkButton(app, text="Показать текст", command=on_click)
submit_button.pack(pady=10)

# Поле вывода
output_label = ctk.CTkLabel(app, text="", wraplength=300)
output_label.pack(pady=20)

app.mainloop()
