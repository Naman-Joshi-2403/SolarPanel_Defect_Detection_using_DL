import pandas as pd 
import os
from PIL import Image
from config import input_folder_path, img_tager_size, background_color_padding, preprocess_image_path, image_extension

def data_collection(folder_path, output_folder_path):
    try:
        ## Ensure output dir is present
        os.makedirs(output_folder_path, exist_ok=True)
        ## Catagories Folder
        for file in os.listdir(folder_path):
            ## Ensure output catagory folder present
            os.makedirs(os.path.join(output_folder_path, file), exist_ok=True)
            ## Images in folder
            for img in os.listdir(os.path.join(folder_path, file)):
                if img.lower().endswith(image_extension): 
                    with Image.open(os.path.join(folder_path, file, img)) as img_file:
                        current_dimension = img_file.size
                        ratio = min(img_tager_size[0] / current_dimension[0], img_tager_size[1] / current_dimension[1])
                        new_dimension = (int(current_dimension[0] * ratio), int(current_dimension[1] * ratio))
                        resize_image = img_file.resize(size=new_dimension, resample=Image.LANCZOS)

                        ## Creating new Canvas
                        padded_image = Image.new('RGB', size=img_tager_size, color=background_color_padding)

                        ## calculating center of canvas
                        x_coordinate = (img_tager_size[0] - new_dimension[0]) // 2 
                        y_coordinate = (img_tager_size[1] - new_dimension[1]) // 2 

                        padded_image.paste(im=resize_image, box=(x_coordinate, y_coordinate))

                        padded_image.save(os.path.join(output_folder_path, file, img))

                        print(f'Successfully saved image to path {os.path.join(output_folder_path, file, img)}')

    except Exception as e:
        print(f"Error Occured while pre processiing the images. Error: {e}")

data_collection(input_folder_path, preprocess_image_path)