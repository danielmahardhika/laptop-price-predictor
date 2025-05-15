import streamlit as st
import numpy as np
import pickle

# Load the models and data
pipe_X = pickle.load(open('pipe_X.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))
linear_model = pickle.load(open('linear_model.pkl', 'rb'))

st.title("Laptop Price Predictor")

# Sidebar inputs
company = st.sidebar.selectbox('Brand', df['Company'].unique())
type = st.sidebar.selectbox('Type', df['TypeName'].unique())
ram = st.sidebar.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
weight = st.sidebar.number_input('Weight of Laptop')
touchscreen = st.sidebar.selectbox('Touchscreen', ['No', 'Yes'])
ips = st.sidebar.selectbox('IPS', ['No', 'Yes'])
screen_size = st.sidebar.number_input('Screen Size')
resolution = st.sidebar.selectbox('Screen Resolution', [
    '1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800',
    '2880x1800', '2560x1600', '2560x1440', '2304x1440'
])
cpu = st.sidebar.selectbox('CPU', df['Cpu brand'].unique())
hdd = st.sidebar.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])
ssd = st.sidebar.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])
gpu = st.sidebar.selectbox('GPU', df['Gpu Brand'].unique())
os = st.sidebar.selectbox('OS', df['os'].unique())

if st.button('Predict Price'):
    # Convert categorical inputs to numerical
    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0

    # Calculate PPI
    X_res, Y_res = map(int, resolution.split('x'))
    ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size

    # Create the feature array
    query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os]).reshape(1, -1)

    # Transform the query using the pipeline
    query_transformed = pipe_X.transform(query)

    # Predict the price using the linear regression model
    prediction = int(np.exp(linear_model.predict(query_transformed)[0]))

    # Determine Price Category (CLUSTERING)
    if prediction < 700:
        category = "Harga Murah"
    elif prediction < 1300:
        category = "Harga Menengah"
    else:
        category = "Harga Mahal"

    st.title(f"Harga Prediksi Konfigurasi Terpilih: ${prediction}, Termasuk Kategori: {category}")