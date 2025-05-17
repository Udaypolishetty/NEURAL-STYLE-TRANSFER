
# 🎨 Neural Style Transfer with TensorFlow Hub

This project applies artistic styles from one image (style) to another (content) using a pre-trained model from TensorFlow Hub. The result is a new, stylized image that blends the structure of the content image with the aesthetics of the style image.

## 🧠 Model Used
- **TensorFlow Hub**: [Magenta Arbitrary Image Stylization v1-256](https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2)

## 📁 Project Files
- `content1.jpg`: Your input content image.
- `style1.jpg`: The style image to apply.
- `stylized_output.jpg1`: The resulting stylized image.

## 🚀 How It Works
1. Loads content and style images from disk.
2. Resizes and pre-processes the images.
3. Passes them through the Magenta model from TF Hub.
4. Outputs and saves the stylized image.

## 🖼️ Output
A new image that merges your content with the selected artistic style.

## 🛠️ Requirements
- TensorFlow
- TensorFlow Hub
- NumPy
- Pillow

```bash
pip install tensorflow tensorflow-hub numpy pillow
```

## ▶️ Run the Script
Make sure `content1.jpg` and `style1.jpg` are in the same folder as the script.

```bash
python app.py
```

## 📦 Output
Check your folder for `stylized_output.jpg1`. You can rename the file if needed.

---

✅ Built with TensorFlow and Magenta | 🎨 Created with ❤️ for AI + Art fans
