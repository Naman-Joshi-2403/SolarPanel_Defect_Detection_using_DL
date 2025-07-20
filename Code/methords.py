import pandas as pd 
import os
from PIL import Image
from config import input_folder_path

def data_collection(folder_path):
    for file in os.listdir(folder_path):
        for img in os.listdir(os.path.join(folder_path, file)):
            with Image.open(os.path.join(folder_path, file, img)) as img_file:
                current_dimension = img_file.size
                print(current_dimension)

            print(f"{file} : {img}")

    pass

data_collection(input_folder_path)