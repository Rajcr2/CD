import torch
#BATCH_SIZE = 4 # increase / decrease according to GPU memeory  # Original
BATCH_SIZE = 8
RESIZE_TO = 512 # resize the image for training and transforms
#NUM_EPOCHS = 100 # number of epochs to train for  # Original
NUM_EPOCHS = 70
DEVICE = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
# training images and XML files directory
TRAIN_DIR =  r"C:\Users\Raj\Desktop\COD_RCNN\Crime_Detection (Pascal VOC - 280_77)\train"               #'../Crime Detection (Pascal VOC)/train' # Desktop/COD_RCNN (.py)/Crime Detection (Pascal VOC)/test
# validation images and XML files directory
VALID_DIR = r"C:\Users\Raj\Desktop\COD_RCNN\Crime_Detection (Pascal VOC - 280_77)\test"
# classes: 0 index is reserved for background
CLASSES = [
    'background', 'Gun', 'Crime_Activity', 'Weapon'
]
NUM_CLASSES = 4
# whether to visualize images after crearing the data loaders
VISUALIZE_TRANSFORMED_IMAGES = False
# location to save model and plots
OUT_DIR = r"C:\Users\Raj\Desktop\COD_RCNN\outputs"
SAVE_PLOTS_EPOCH = 2 # save loss plots after these many epochs
SAVE_MODEL_EPOCH = 2 # save model after these many epochs