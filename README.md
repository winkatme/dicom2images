# dicom2images
Convert a DICOM file that contains multiple images to single jpg/png/tif images, and save them in a folder.

Most DICOM files contain multiple images in one file.  This code converts the DICOM images into individual image files.

Manually enter the folder, DICOM file name, and optionally, the type of image you want to convert to.

Note that some Gaussian Blur is applied to make the image a little easier on the eyes.  

Based on code from this source: https://pycad.co/how-to-convert-a-dicom-image-into-jpg-or-png/
