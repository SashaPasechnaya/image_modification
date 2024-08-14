
import tensorflow as tf
from PIL import Image
import os
import sys

# Путь к модели с сигнатурами
model_path = "D:\учебные\python_projects\данные для диплома\веса для моделей\cycle_gan_model_draft"

try:
    loaded_model = tf.saved_model.load(model_path)
    serving_fn = loaded_model.signatures['serving_default']
except Exception as e:
    print(f"Ошибка при загрузке модели: {e}")
    sys.exit(1)

# Размер изображения
IMAGE_SIZE = (256, 256)

def decode_image(image_path):
    image = tf.io.read_file(image_path)
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, IMAGE_SIZE)
    image = (tf.cast(image, tf.float32) / 127.5) - 1  # Нормализация до диапазона [-1, 1]
    return image

def apply_style(image):
    image = tf.expand_dims(image, axis=0)  # Добавить размер партии
    styled_image = serving_fn(tf.constant(image))
    styled_image = styled_image['output'].numpy()  # Получение массива NumPy
    styled_image = tf.squeeze(styled_image, axis=0)  # Удалить размер партии
    styled_image = (styled_image + 1) * 127.5  # Вернуть диапазон [0, 255]
    styled_image = tf.clip_by_value(styled_image, 0, 255)
    styled_image = tf.cast(styled_image, tf.uint8)
    return styled_image.numpy()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        if not os.path.exists(image_path):
            print(f"Ошибка: Файл {image_path} не существует.")
            sys.exit(1)

        try:
            decoded_image = decode_image(image_path)
            styled_image = apply_style(decoded_image)

            # Конвертировать изображение в формат PIL и сохранить
            styled_image_pil = Image.fromarray(styled_image)
            result_path = "result_styled.png"
            styled_image_pil.save(result_path)
            print(f"Результат сохранён в '{result_path}'")
        except Exception as e:
            print(f"Ошибка при обработке изображения: {e}")
    else:
        print("Ошибка: Не указан путь к изображению.")

