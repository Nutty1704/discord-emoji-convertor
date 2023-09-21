import os
import sys
from PIL import Image


def resize(file_path: str, output_directory: str) -> bool:
    '''
    Resize the image to 128x128 and save it to the same folder

    :param file_path: path to the image
    :param output_directory: path to the output directory

    :return: True if the image was resized, False otherwise
    '''
    size = 128, 128
    file, ext = os.path.splitext(file_path)
    file_name = os.path.basename(file)

    if ext != '.jpg':
        return False

    with Image.open(file_path) as img:
        img.thumbnail(size)
        img.save(output_directory + '/' + file_name + "-resized.jpg", 'JPEG')

    return True



# MAIN PROGRAM
path = sys.argv[1]

if os.path.isfile(path):
    resize(path, os.path.dirname(path))
    print("Resized " + os.path.basename(path) + " and saved it to " + os.path.dirname(path))

elif os.path.isdir(path):
    output_directory = os.path.dirname(path) + "/resized_images"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    count = 0

    for file in os.listdir(path):
        result = resize(os.path.join(path, file), output_directory)
        if result:
            count += 1

    print("Resized " + str(count) + " images and saved them to " + output_directory)
