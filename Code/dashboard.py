import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from PIL import Image
from tensorflow.keras.models import load_model
from config import Config_elements

config_items = Config_elements()


st.set_page_config(layout="wide")

# Load trained AI model 
# model = load_model(r"C:\Users\naman\OneDrive\Desktop\Guvi_Projects\Solar Panel\solar_panel_analyzer.h5")

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        options=["Fault Detection", "Maintainance Status", "Monitoring"],
        menu_icon="cast",
        icons=['search', 'tools', 'bar-chart'],
        default_index=2
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
    monitoring_type = option_menu(
        "Main Menu",
        options=["Fault Type Distribution", "Open/Close Cases", "Customer Issue Status"],
        menu_icon="cast",
        icons=['exclamation-triangle', 'check-circle', 'people'],
        default_index=2,
        orientation='horizontal'
    )

    df = pd.read_csv(config_items.ongoing_maintainance_path)
    
    if monitoring_type == "Fault Type Distribution":
        st.header("Fault Type Distribution", divider="red")
        st.bar_chart(df["Fault"].value_counts())

    if monitoring_type == "Open/Close Cases":
        st.header("Open vs Closed Cases", divider='red')
        st.bar_chart(df["Close Status"].value_counts())

    if monitoring_type == "Customer Issue Status":
        st.header("Customer Issue Status (Open/Closed)", divider='red')
        pivot = pd.crosstab(df["Name"], df["Close Status"])
        st.bar_chart(pivot)

        pivot_df = pd.crosstab([df["Name"], df["Fault"]], df["Close Status"])

        st.header("Customer Issue Status and Fault Type (Open/Closed)", divider='red')
        st.dataframe(pivot_df)

    
    






