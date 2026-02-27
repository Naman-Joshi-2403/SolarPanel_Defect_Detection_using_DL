import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from config import Config_elements
from methords import detect_defect, process_img
import os
from pathlib import Path


config_items = Config_elements()

st.set_page_config(layout="wide")


model = load_model(r"Code/solar_panel_analyzer.keras")

with st.sidebar:
    selected = option_menu( 
        "Main Menu",
        options=["Fault Detection", "Maintainance Status", "Monitoring"],
        menu_icon="cast",
        icons=['search', 'tools', 'bar-chart'],
        default_index=0
    )

st.title("SolarGuard 🌞")

if selected == "Fault Detection":
    img_array = None  
    st.header("Upload Infomation", divider="red")   

    image_input = st.file_uploader(
            "Upload Solar Panel Image",
            accept_multiple_files=False, 
            type=['jpg', 'jpeg', 'png'],
        )
    
    col1,  col2 = st.columns(2)

    with col1:
        name = st.text_input("Enter Your Name", max_chars=50)
    with col2:
        customer_id = st.number_input("Enter Your Customer Id", min_value=1, max_value=999, value=None)

    if st.button("Submit", type="primary", use_container_width=True):
        if image_input is not None: 
            image_input = Image.open(image_input).convert("RGB")
            img = process_img(image_input)
            img_array = np.array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)
            prediction = model.predict(img_array)
            st.write(prediction)        
            predicted_index = np.argmax(prediction, axis=1)[0]
            st.write(predicted_index)
            st.success(f"the defect type is : {config_items.class_names[predicted_index]}")
            csv_path = Path(config_items.ongoing_maintainance_path)
            if not csv_path.exists():
                csv_path.parent.mkdir(parents=True, exist_ok=True)
                pd.DataFrame(columns=["Customer ID", "Name", "Fault", "Close Status"]).to_csv(csv_path, index=False)

            data_entry = pd.read_csv(csv_path)

            new_record = pd.DataFrame([{
                "Customer ID": customer_id,
                "Name": name,
                "Fault": config_items.class_names[predicted_index],
                "Close Status": False
            }])

            updated_df = pd.concat([data_entry, new_record], ignore_index=True)

            updated_df.to_csv(csv_path, index=False)
        else:
            st.error("Please upload a solar panel image!")

if selected == "Maintainance Status": 
    st.header("Maintainance Status 🛠️", divider="blue")

    data_entry = pd.read_csv(config_items.ongoing_maintainance_path)
    open_entry = data_entry[data_entry["Close Status"] == False].copy()
    
    edited_df = st.data_editor(
        open_entry,
        column_config={
            "Name": st.column_config.TextColumn("Name", disabled=True),
            "Customer ID": st.column_config.TextColumn("Customer ID", disabled=True),
            "Fault": st.column_config.TextColumn("Fault", disabled=True),
            "Close Status": st.column_config.CheckboxColumn(
                "Close Status",
                help="Toggle if status is closed."
            )
        },
        hide_index=True,
        key="update_ongoing_maintainance",
    )

    if st.button("Save Updates",type='primary'):
        for idx, row in edited_df.iterrows():
            data_entry.at[idx, "Close Status"] = row["Close Status"]
        data_entry.to_csv(config_items.ongoing_maintainance_path, index=False)
        st.success("Changes saved successfully!")

if selected == "Monitoring":
    df = pd.read_csv(config_items.ongoing_maintainance_path)
    df['Close Status'] = np.where(df['Close Status'] == False, 'Open', 'Close')
    monitoring_type = option_menu(
        "Monitoring Control Panel",
        options=["Customer Issue Status", "Fault Type Distribution"],
        menu_icon="cast",
        icons=[ 'people', 'exclamation-triangle'],
        default_index=0,
        orientation='horizontal'
    )

    with st.container():
        metrix_columns = st.columns([1,2,2,2,2,1], vertical_alignment='center')
        with metrix_columns[2]:
                st.metric(
                    label="Open Cases",
                    value=int(len(df[df["Close Status"] == "Open"])),
                    delta=int(len(df[df["Close Status"] == "Open"])),
                    delta_color='inverse',
                    border=True
                )
        with metrix_columns[3]:
                st.metric(
                    label="Close Cases",
                    value=int(len(df[df["Close Status"] == "Close"])),
                    delta=int(len(df[df["Close Status"] == "Close"])),
                    border=True
                )

    if monitoring_type == "Fault Type Distribution":
        with st.container(border=True):
            pivot = pd.crosstab(df["Name"], df["Close Status"])
            with st.container():
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.header("Fault Type Distribution", divider="red")
                with col2:
                    st.download_button(
                        data=df["Fault"].value_counts().to_csv(),
                        file_name="fault_type_distribution.csv",
                        type="secondary",
                        label="Download CSV",
                        icon="⬇️"
                    )
            st.bar_chart(df["Fault"].value_counts())

    if monitoring_type == "Customer Issue Status":
        with st.container(border=True):
            pivot = pd.crosstab(df["Name"], df["Close Status"])
            with st.container():
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.header("Customer Issue Status (Open/Closed)", divider='red')
                with col2:
                    st.write("") 
                    st.download_button(
                        data=pivot.to_csv(),
                        file_name="customer_issue_status.csv",
                        type="secondary",
                        label="Download CSV",
                        icon="⬇️"
                    )
            st.bar_chart(pivot)

