import sys
import tensorflow as tf
from PIL import Image
import numpy as np
import os

def preprocess_image(image_file, img_size):
    image = Image.open(image_file).convert("RGB")  # Преобразуем изображение в RGB
    image = image.resize((img_size, img_size))
    image = np.array(image) / 255.0  # Нормализуем изображение к диапазону [0, 1]
    return image

def postprocess_image(image_array):
    image_array = np.clip(image_array * 255, 0, 255).astype(np.uint8)  # Обратно в диапазон [0, 255]
    return Image.fromarray(image_array)

def load_model(model_path):
    # Загрузка модели (пример, используйте путь к вашей модели)
    return tf.keras.models.load_model(model_path)

def enhance_image(image):
    # Применяем модель улучшения качества (пример: суперразрешение)
    # Модель ожидает входные данные в форме (1, img_size, img_size, 3)
    img_batch = np.expand_dims(image, axis=0)
    enhanced_image = model.predict(img_batch)
    # Предполагается, что модель возвращает результат в диапазоне [0, 1]
    return enhanced_image[0]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python model3.py <image_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    
    if not os.path.exists(image_path):
        print(f"Image file {image_path} does not exist.")
        sys.exit(1)

    # Параметры
    img_size = 256  # Задайте размер изображения для предобработки
    model_path = "D:/учебные/python_projects/данные для диплома/веса для моделей/Pix2PixSR.h5"  # Укажите путь к вашей модели

    # Предобработка изображения
    input_image = preprocess_image(image_path, img_size)
    
    # Загрузка модели
    model = load_model(model_path)
    
    # Улучшение изображения
    enhanced_image = enhance_image(input_image)
    
    # Постобработка и сохранение результата
    result_image = postprocess_image(enhanced_image)
    result_image.save("result.png")
    print("Enhanced image saved as result.png")
