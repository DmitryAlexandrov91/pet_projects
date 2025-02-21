from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

# Укажите путь к tesseract.exe (только для Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image_path):
    """Предобрабатывает изображение для улучшения распознавания."""
    image = Image.open(image_path)

    # Преобразуем в чёрно-белое
    image = image.convert('L')

    # Увеличиваем контрастность
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)

    # Убираем шум
    image = image.filter(ImageFilter.MedianFilter(size=3))

    return image

def recognize_captcha(image_path):
    """Распознаёт текст на изображении с капчей."""
    # Предобработка изображения
    image = preprocess_image(image_path)

    # Распознаём текст
    text = pytesseract.image_to_string(image, lang='eng', config='--psm 6')
    return text.strip()  # Убираем лишние пробелы

# Пример использования
image_path = 'kapcha.png'  # Путь к изображению с капчей
captcha_text = recognize_captcha(image_path)
print("Распознанный текст:", captcha_text)