import pydicom
import numpy as np
from PIL import Image, ImageFilter
import os

# Manually change these variables:

# Enter the folder that contains the DICOM file to convert:
location = 'C:\My Downloads\DICOM_Files'

# Enter the file name of the DICOM file:
Dicom_file = 'Jane_Doe_Brain_MRI_DICOM.dcm'

# Type of image to save as:  .tif, .jpg, .png,...
Image_Type = 'tif'



# Set directory where DICOM file is located
os.chdir(location)

# Read DICOM file and scale image pixel values
ds = pydicom.dcmread(Dicom_file)
new_image = ds.pixel_array.astype(float)
scaled_image = (np.maximum(new_image, 0) / new_image.max()) * 255

# Iterate conversion to image type, Save in folder \Images
os.makedirs('Images', exist_ok=True)
for i in range(0,len(scaled_image[:])):
    image_number = i+1
    scaled_image_copy = scaled_image[i,:,:]
    img = Image.fromarray(scaled_image_copy)
    img = img.convert(mode='L')   # For some reason I had to convert it to 8-bit mode L for gaussian to work (Modes: https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes)
    img = img.filter(ImageFilter.GaussianBlur(radius=0.6))
    
    img.save(f'Images\image_{image_number}.{Image_Type}')

