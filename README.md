# 🌞 SolarGuard -- Intelligent Solar Panel Defect Detection

## 📌 Project Overview

SolarGuard is a Deep Learning-powered web application designed to detect
and classify defects in solar panels using image data. The system
automates inspection processes by identifying panel conditions such as
dust, snow, bird droppings, electrical damage, and physical damage.

This project integrates: - Image preprocessing - CNN-based
classification model - Streamlit web application - Maintenance tracking
system - Monitoring dashboard

------------------------------------------------------------------------

## 🚀 Features

### 🔍 1. Fault Detection

-   Upload solar panel images
-   Preprocess images (resize, padding, normalization)
-   Predict defect type using trained CNN model
-   Display classification result

### 🛠️ 2. Maintenance Management

-   Track ongoing maintenance cases
-   Update case status (Open / Closed)
-   Persist changes in CSV database

### 📊 3. Monitoring Dashboard

-   View open vs closed cases
-   Analyze fault type distribution
-   Download analytical reports as CSV

------------------------------------------------------------------------

## 🧠 Model Details

-   Custom CNN Model (`solar_panel_custom_model.keras`)
-   Multi-class classification (6 classes):
    -   Clean
    -   Dusty
    -   Bird-Drop
    -   Electrical-Damage
    -   Physical-Damage
    -   Snow-Covered

### 📈 Evaluation Metrics

-   Accuracy
-   Precision
-   Recall
-   F1 Score

------------------------------------------------------------------------

## 🏗️ Project Architecture

    Dataset → Preprocessing → CNN Model → Saved Model (.keras)
                                    ↓
                             Streamlit Application
                                    ↓
            Fault Detection | Maintenance | Monitoring

Architecture Type: 3-Tier Architecture - Presentation Layer: Streamlit
UI - Business Logic Layer: Image Processing + Model Inference - Data
Layer: Image Dataset + Maintenance CSV

------------------------------------------------------------------------

## 📂 Project Structure

    SOLAR PANEL/
    │
    ├── Code/
    │   ├── config.py
    │   ├── dashboard.py
    │   ├── main.py
    │   ├── methords.py
    │   ├── custom_cnn.ipynb
    │   ├── solar_analysis_resNet50.ipynb
    │   ├── solar_panel_custom_model.keras
    │
    ├── Faulty_solar_panel_raw_data/
    │   ├── Bird-drop/
    │   ├── Clean/
    │   ├── Dusty/
    │   ├── Electrical-damage/
    │   ├── Physical-Damage/
    │   └── Snow-Covered/
    │
    ├── requirements.txt
    ├── README.md
    └── SolarPanel_Defect_Detection_using_DeepLearning.pdf

------------------------------------------------------------------------

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

``` bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2️⃣ Create Virtual Environment (Recommended)

``` bash
python -m venv env
```

Activate:

Windows:

``` bash
env\Scripts\activate
```

Mac/Linux:

``` bash
source env/bin/activate
```

### 3️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ▶️ Run the Application

Navigate to Code directory:

``` bash
cd Code
```

Run Streamlit:

``` bash
streamlit run dashboard.py
```

The app will open in your browser.

------------------------------------------------------------------------

## 🗂️ Dataset

Dataset contains categorized solar panel images across six defect
types.\
Ensure the dataset path is correctly configured inside `config.py`.

------------------------------------------------------------------------

## 🔮 Future Improvements

-   Deploy model using FastAPI + Docker
-   Integrate PostgreSQL instead of CSV
-   Add object detection (YOLOv8)
-   Deploy on AWS SageMaker
-   Add logging & monitoring

------------------------------------------------------------------------

## 💼 Business Impact

-   Reduces manual inspection costs
-   Enables predictive maintenance
-   Improves solar farm efficiency
-   Automates defect detection

------------------------------------------------------------------------

## 📌 Tech Stack

-   Python
-   TensorFlow / Keras
-   NumPy
-   Pandas
-   PIL
-   Streamlit

------------------------------------------------------------------------

## 👨‍💻 Author

Naman Joshi

------------------------------------------------------------------------

## 📄 License

This project is for educational and research purposes.
