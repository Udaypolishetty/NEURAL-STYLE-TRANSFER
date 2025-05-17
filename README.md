# NEURAL-STYLE-TRANSFER

COMPANY: CODETECH IT SOLUTIONS

NAME: POLISHETTY UDAY

INTERN ID: CODF47

DOMAIN: WEB DEVELOPMENT

DURATION: 4-WEEKS

MENTOR:NEELA SANTOSH

# DESCRIPTION:

THIS PROJECT IMPLEMENTS ARTISTIC STYLE TRANSFER ON IMAGES USING PYTHON AND THE POWERFUL LIBRARIES TENSORFLOW AND TENSORFLOW HUB. IT LEVERAGES A PRE-TRAINED STYLE TRANSFER MODEL TO RECREATE A CONTENT IMAGE WITH THE ARTISTIC STYLE OF A STYLE IMAGE.

THE CORE FUNCTIONALITY IS BUILT USING TENSORFLOW FOR TENSOR OPERATIONS, IMAGE MANIPULATION, AND MODEL EXECUTION. TENSORFLOW HUB IS UTILIZED TO LOAD A PRE-EXISTING ARBITRARY IMAGE STYLIZATION MODEL HOSTED BY GOOGLE/MAGENTA, SAVING THE EFFORT OF TRAINING A COMPLEX MODEL FROM SCRATCH. NUMPY IS USED FOR NUMERICAL OPERATIONS, PARTICULARLY WHEN CONVERTING TENSORS TO IMAGES, AND PIL (PYTHON IMAGING LIBRARY) FACILITATES SAVING THE RESULTING STYLIZED IMAGE. THE OS MODULE IS IMPORTED BUT NOT EXPLICITLY USED IN THE PROVIDED SNIPPET.

** KEY FUNCTIONS DEFINED IN THE CODE INCLUDE **:

* `load_img(path_to_img, max_dim=512)`: This function takes the path to an image and an optional maximum dimension as input. It reads the image file, decodes it into a TensorFlow tensor, converts the data type to float32, resizes the image while maintaining aspect ratio (ensuring the longer side does not exceed `max_dim`), and adds a batch dimension to the tensor.
* `tensor_to_image(tensor)`: This function takes a TensorFlow tensor representing an image. It scales the tensor values back to the 0-255 range, converts the data type to unsigned 8-bit integers, removes the batch dimension if present, and then uses PIL to create an image object from the NumPy array representation of the tensor.

THE PROCESS INVOLVED IN THE SCRIPT IS AS FOLLOWS:

1.  Loading Images: The script defines the paths to a 'content' image (`content1.jpg`) and a 'style' image (`style1.jpg`), assuming these files are located in the same directory as the script. It then uses the 
 `load_img` function to load and preprocess both images into TensorFlow tensors.
2. Loading the Model: A pre-trained arbitrary image stylization model is loaded from TensorFlow Hub using its URL. This model is capable of transferring the style from one image to another.
3. Stylizing the Image: The loaded `hub_module` is called with the content and style images (converted to TensorFlow constants). The model processes these images and outputs a tensor representing the stylized image. The `[0]` at the end of the call extracts the stylized image from the output batch.
4. Saving the Output: The `tensor_to_image` function converts the resulting stylized tensor back into a PIL Image object. This image is then saved to a file named `stylized_output.jpg1` in the same directory as the script.
5. Confirmation: A print statement confirms the successful saving of the stylized image and provides the output file path.

THIS PROJECT DEMONSTRATES THE USE OF HIGH-LEVEL LIBRARIES LIKE TENSORFLOW AND TENSORFLOW HUB TO PERFORM COMPLEX TASKS LIKE Neural Style Transfer with minimal code. It showcases the ability to leverage pre-trained models for efficient and effective image processing.

FUTURE EXTENSIONS COULD INCLUDE: Allowing users to specify different content and style images, adjusting style transfer parameters, displaying the input and output images, and potentially deploying the functionality as a web application.

WORKING ON THIS PROJECT HAS STRENGTHENED SKILLS IN IMAGE PROCESSING USING TENSORFLOW, UTILIZING PRE-TRAINED MODELS FROM TENSORFLOW HUB, AND UNDERSTANDING THE FUNDAMENTALS OF Neural Style Transfer. IT PROVIDES A FOUNDATION FOR EXPLORING MORE ADVANCED COMPUTER VISION TECHNIQUES.

#  SAMPLE OUTPUT:
