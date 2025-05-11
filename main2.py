import pytesseract
from pdf2image import convert_from_path
import cv2
import numpy as np

def pdf_to_text_with_ocr(pdf_path, output_text_path=None):
    # 1. Конвертируем PDF в изображения (постранично)
    images = convert_from_path(pdf_path, dpi=300)  # Чем выше DPI, тем лучше точность
    
    extracted_text = ""
    
    for i, image in enumerate(images):
        # 2. Преобразуем изображение в чёрно-белое (улучшает распознавание)
        gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
        _, threshold_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)
        
        # 3. Распознаём текст с помощью Tesseract
        text = pytesseract.image_to_string(threshold_image, lang='rus+eng')  # Языки: русский + английский
        extracted_text += f"Страница {i+1}:\n{text}\n\n"
    
    # 4. Сохраняем результат в файл (опционально)
    if output_text_path:
        with open(output_text_path, 'w', encoding='utf-8') as f:
            f.write(extracted_text)
    
    return extracted_text

# Пример использования
pdf_path = "/Users/ivanvinogradov/ai_rec/дз.pdf"
text = pdf_to_text_with_ocr(pdf_path, output_text_path="/Users/ivanvinogradov/ai_rec/распознанныйт.txt")
print(text)
