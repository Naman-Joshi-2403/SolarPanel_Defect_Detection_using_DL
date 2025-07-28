import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from config import Config_elements
import os 
from pandas import DataFrame

config_items = Config_elements()


def update_backend():
    updated_df = st.session_state['update_ongoing_maintainance']
    print(updated_df)
    updated_df.to_csv(config_items.ongoing_maintainance_path, index=False)


st.set_page_config(layout="wide")

# Load trained AI model 
# model = load_model(r"C:\Users\naman\OneDrive\Desktop\Guvi_Projects\Solar Panel\solar_panel_analyzer.h5")

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        options=["Fault Detection", "Maintainance Status", "Monitoring"],
        menu_icon="cast",
        icons=['search', 'tools', 'bar-chart'],
        default_index=1
    )


st.title("SolarGuard 🌞")

if selected == "Fault Detection":
    st.header("Upload Infomation", divider="red")

    image_input = st.file_uploader(
            "Upload Solar Panel Image",
            accept_multiple_files=False,
            type=['jpg', 'jpeg', 'png']
        )

    col1,  col2 = st.columns(2)

    with col1:
        name = st.text_input("Enter Your Name", max_chars=50)
    with col2:
        customer_id = st.number_input("Enter Your Customer Id", min_value=1, max_value=999, value=None)

    st.button("Submit", type="primary", use_container_width=True)


if selected == "Maintainance Status":
    data_entry = pd.read_csv(config_items.ongoing_maintainance_path)
    
    edited_df = st.data_editor(
        data_entry,
        column_config={
            "Close Status": st.column_config.CheckboxColumn(
                "Close Status",
                help="Toggle if status is closed."
            )
        },
        hide_index=True,
        key="update_ongoing_maintainance",
    )
    
    edited_df.to_csv(config_items.ongoing_maintainance_path, index=False)



if selected == "Monitoring":
    pass




