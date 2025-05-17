import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import PIL.Image
import os

# Function to load an image and resize it
def load_img(path_to_img, max_dim=512):
    img = tf.io.read_file(path_to_img)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)

    shape = tf.cast(tf.shape(img)[:-1], tf.float32)
    long_dim = max(shape)
    scale = max_dim / long_dim

    new_shape = tf.cast(shape * scale, tf.int32)

    img = tf.image.resize(img, new_shape)
    img = img[tf.newaxis, :]
    return img

# Function to convert tensor to image
def tensor_to_image(tensor):
    tensor = tensor * 255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor) > 3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]
    return PIL.Image.fromarray(tensor)

# Load content and style images (⚡ directly from main folder)
content_path = 'content1.jpg'
style_path = 'style1.jpg'

content_image = load_img(content_path, max_dim=512)
style_image = load_img(style_path, max_dim=512)

# Load the model
hub_module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

# Stylize the image
stylized_image = hub_module(tf.constant(content_image), tf.constant(style_image))[0]

# Save output
output_path = 'stylized_output.jpg1'
tensor_to_image(stylized_image).save(output_path)

print(f"Stylized image saved as {output_path} ✅")
