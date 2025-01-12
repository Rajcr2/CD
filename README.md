# Crime Detection with PyTorch Faster RCNN.

## Introduction

This model aims to do real-time crime detection using OpenCV and FasterRCNN_resnet50_fpn. The main motive is to loop over each image that passed through this model and if model detects a **"Crime_Activity"** just bound that detection in bbox.

### Prerequisites
To run this project, you need to install the following libraries:
### Required Libraries

- **Python 3.12+**
- **Open-CV**: Open-CV is a poweful library for computer vision and image processing tasks.
- **Torch**: This library is primarily used for building and training deep learning models.
- **Torchvision**: It is a companion library for PyTorch mainly used for fine-tuning deep learning models for vision applications like object detection and segmentation.
- **Numpy**: It provides support for creating and manipulating multi-dimensional arrays and matrices.

Other Utility Libraries : **Matplotlib**, **glob2**, **tqdm**, **albumentations**.

### Installation

   ```
   pip install opencv-python
   pip install numpy
   pip install torch torchvision
   pip install matplotlib
   pip install glob2
   pip install tqdm
   pip install albumentations
   ```

### Procedure

1.   Create new directory **'COD'**.
2.   Inside that directory/folder create new environment.
   
   ```
   python -m venv cod
   ```

  Now, activate this **'cod'** venv.
  
4.   Clone this Repository :

   ```
   https://github.com/Rajcr2/CD.git
   ```
5.   Now, Install all mentioned required libraries in your environment.
6.   After, that Run **'engine.py'** file from Terminal. To train the model it will take time but make sure that model is not overfitting.
   ```
   python engine.py
   ``` 
7.   After, Model Training completed just Run the **'inference.py'** that will load trained model and will give us predicted output results.
   ```
   python inference.py
   ```




### Output

https://github.com/user-attachments/assets/26efebec-64fb-4fff-944d-8177aec6a812



