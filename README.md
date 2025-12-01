# 🏡 House Price Prediction App

A web application built with **Streamlit** to predict house prices based on key features like square footage, number of bedrooms, bathrooms, lot size, garage size, and neighborhood quality. The model is trained using a **Random Forest Regressor** and saved as a pipeline.

---

## 📂 Project Structure

house-price-predictor/
│
├─ house_price_model.pkl # Trained Random Forest model
├─ house_price_app.py # Streamlit app
├─ House_Price_EDA_Model.ipynb # Jupyter notebook with EDA and model training
├─ README.md # Project documentation
└─ requirements.txt # Python dependencies

---

## 🧪 Features

- Predict estimated house price instantly by entering:
  - Square Footage 📏
  - Number of Bedrooms 🛏️
  - Number of Bathrooms 🛁
  - Year Built 🏗️
  - Lot Size 🌳
  - Garage Size 🚗
  - Neighborhood Quality 🏘️
- Interactive **bar chart** showing feature comparison.
- Optional **house emoji display** for fun visualization.
- Clean and responsive UI with **Streamlit columns and styled containers**.

---

## 💻 How to Run
```bash
1. Clone this repository:

git clone <your-repo-url>
cd house-price-predictor

2. Install dependencies:
pip install -r requirements.txt

3. Run the Streamlit app:
streamlit run house_price_app.py

4. The app will open in your browser at http://localhost:8501.

📝 Model Training
The model is trained in the included Jupyter notebook: House_Price_EDA_Model.ipynb.
-->Steps in the notebook:
--> Load and inspect the dataset.
-->Perform EDA (Exploratory Data Analysis).
-->Preprocess features and handle missing values.
-->Train a Random Forest Regressor.
-->Save the trained model using joblib as house_price_model.pkl.

🛠️ Technologies Used
-->Python 🐍
-->Streamlit ⚡
-->Pandas & NumPy 🧮
-->Scikit-learn 🌲
-->Matplotlib / Seaborn (for EDA) 📊
-->Joblib 💾

📌 Notes
-->Make sure house_price_model.pkl is in the same directory as the Streamlit app.
-->The app is lightweight and can run locally without internet.
-->The UI uses emojis instead of images for simplicity.
👩‍💻 Author
[Abhishek R. Kayasth]
Email: kayasthabhishek2000@gmail.com
GitHub: github.com/Abhixtech4
