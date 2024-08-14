import sys
import tensorflow as tf
from PIL import Image
import numpy as np

# Загрузка модели
colorize_model = tf.keras.models.load_model('D:/учебные/python_projects/данные для диплома/веса для моделей/Pix2PixGan.weights.h5')

def preprocess_image(image_file, img_size):
    rgb_image = Image.open(image_file).resize((img_size, img_size))
    gray_image = rgb_image.convert('L').resize((img_size, img_size))
    
    rgb_img_array = np.array(rgb_image) / 255.0
    gray_img_array = np.array(gray_image) / 255.0
    gray_img_array = np.stack([gray_img_array, gray_img_array, gray_img_array], axis=-1)
    
    return gray_img_array, rgb_img_array

def colorize_image(gray_image):
    image = np.expand_dims(gray_image, axis=0)
    predicted_image = colorize_model.predict(image)[0]
    return predicted_image

if __name__ == "__main__":
    image_path = sys.argv[1]
    gray_img_array, _ = preprocess_image(image_path, 256)
    result_image = colorize_image(gray_img_array)
    
    result_image = (result_image * 255).astype(np.uint8)
    result_image_pil = Image.fromarray(result_image)
    result_image_pil.save("result.png")
    print("Результат сохранен в 'result.png'")
