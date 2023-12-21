from PIL import Image
import os

path = './images-in' # path to folder with pngs
pathOut = './images-out' # path to folder where jpgs will be saved
quality_setting = 80 # preffered quality setting

# convert to jpg and reduce size if necessary
for filename in os.listdir(path):
    # Check if file is a png
    if filename.endswith('.png'):
        # Open image and convert to RGB
        im = Image.open(f'{path}/{filename}')
        rgb_im = im.convert('RGB')

        # Get original size
        original_size = os.path.getsize(f'{path}/{filename}')
        
        # Save with quality setting
        rgb_im.save(f'{pathOut}/{filename[:-4]}.jpg', quality=quality_setting)
        
        # Get new size
        new_size = os.path.getsize(f'{pathOut}/{filename[:-4]}.jpg')
        
        # If the new file is not smaller by more than 10%, keep it anyway
        if new_size >= original_size * 0.9:
            print(f'{filename} converted to jpg, size reduction not significant')
        else:
            print(f'{filename} converted to jpg with reduced size')
    else:
        print(f'{filename} is not a png')