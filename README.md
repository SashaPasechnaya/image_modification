# Image Modification Project  
This project provides a GUI application for performing image modification tasks such as colorization, image enhancement, and style transfer. The application utilizes pre-trained deep learning models for these tasks.

# Features  
Colorization: Convert grayscale images to color using the Pix2Pix model.  
Image Enhancement: Improve the resolution and quality of images using the Super-Resolution model.  
Style Transfer: Apply artistic styles to images using the CycleGAN model.  
# Installation 
Clone the repository: 
```bash
git clone https://github.com/SashaPasechnaya/image_modification 
cd image_modification
```
# Download Pre-trained Model Weights:  

Download the model weights from [this link](https://drive.google.com/drive/u/0/folders/1r51zLYyVSANfB-zXt7ram04rkV6msQIR).
Save the downloaded weights in the appropriate directory within the project.
# Load Model Files: 

Ensure the following model files are in the same directory:   
model1.py  
model2.py  
model3.py  
final_model.py (which integrates all three models)  
Run the Application: 
```bash
python final_model.py 
```
# Model Architecture  
For those interested in the underlying architecture of the models used:  

Uncontrolled Style Transfer: The CycleGAN architecture is detailed in cyclegan-final.ipynb.  
Colorization: The Pix2Pix architecture is detailed in pix2pix.ipynb.  
Image Enhancement: The Super-Resolution model is detailed in super-resolution.ipynb.  
# Demo  
To see the application in action, watch the [demo video](https://drive.google.com/file/d/1-MIipetYYuXljr0LFZF2awZfHvrXnvdC/view?usp=sharing).  

# Contributing  
Contributions are welcome! If you encounter any issues or have suggestions, feel free to create an issue or submit a pull request.  
