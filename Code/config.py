import os 

base_user_dir = os.path.expanduser('~')

input_folder_path = os.path.join(base_user_dir, r'OneDrive\Desktop\Guvi_Projects\Solar Panel\Faulty_solar_panel_raw_data')
preprocess_image_path = os.path.join(base_user_dir, r'OneDrive\Desktop\Guvi_Projects\Solar Panel\Faulty_solar_panel')
img_tager_size = (256, 256)
background_color_padding = (0,0,0)
image_extension = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')