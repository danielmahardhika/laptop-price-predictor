# Laptop Price Predictor

## Description
This application predicts laptop prices based on various features such as brand, type, RAM, and other specifications. It is built using Streamlit.

## Prerequisites
Make sure you have Python and the required libraries installed. You can install all the libraries using the following command:

```bash
pip install -r requirements.txt
```

## Project Structure
- `laptop_price_predictor.py`: The main code for the laptop price prediction application.
- `pipe_X.pkl`: The model pipeline for data preprocessing.
- `df.pkl`: The DataFrame containing laptop data.
- `linear_model.pkl`: The linear regression model for price prediction.

## How to Run the Application
1. Clone this repository
2. Open a terminal and navigate to the directory where the files are stored.
3. Run the application using the following command:

```bash
streamlit run laptop_price_predictor.py
```

4. The application will open in your browser, and you can start entering data to predict laptop prices.

## How to Use
- Select the brand, type, and specifications of the laptop using the sidebar.
- Click the "Predict Price" button to see the predicted price and price category of the laptop.
