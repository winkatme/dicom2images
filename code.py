import pydicom
import numpy as np
import os
# Note: Pillow version 9.2.0 is required
from PIL import Image, ImageFilter


# Manually change these variables:

# Enter the folder that contains the DICOM file to convert:
location = 'C:\My Documents\Dicom_Files'

# Enter the file name of the DICOM file:
Dicom_file = 'AB33M3.dcm'

# Type of image to save as:  tif, jpg, png,...
Image_Type = 'tif'

# Rotate 180 degrees?  1=yes, 0 = no
Rotate_180 = 1

# FLip left to right?  1=yes, 0=no
flip_L_to_R = 1


'''
___________________________________________
'''

# Name
Name = Dicom_file.split('.')
Name = Name[0]

# Size: enter a tuple, ie - (512, 512).  For default value, enter 'default' with quotes
size = (512, 512)

# Sets directory where DICOM file is located
os.chdir(location)

# Read DICOM file and scale image pixel values
ds = pydicom.dcmread(Dicom_file)
new_image = ds.pixel_array.astype(float)
scaled_image = (np.maximum(new_image, 0) / new_image.max()) * 255

# Iterate conversion to image type, Save in folder \Images
# Note: It appears that the images need to be manually converted to 8-bit (Mode='L') for the Gaussian blur to work correctly.
# Other modes: https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes
os.makedirs('Images', exist_ok=True)
for i in range(0,len(scaled_image[:])):
    image_number = i+1
    scaled_image_copy = scaled_image[i,:,:]
    img = Image.fromarray(scaled_image_copy)
    img = img.convert(mode='L')
    img = img.filter(ImageFilter.GaussianBlur(radius=0.6))
    if flip_L_to_R == 1:
        img = img.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
    if Rotate_180 == 1:    
        img = img.rotate(180)
    if size != 'default':
        img = img.resize(size)
    img.save(f'Images\{Name}_{image_number}.{Image_Type}')
