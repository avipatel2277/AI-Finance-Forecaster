# 💰 AI-Powered Personal Finance Assistant

A Full-Stack Data Science application that aggregates personal financial data, visualizes spending habits, and utilizes **Machine Learning** to forecast future monthly expenses. 

---

## 🚀 Overview
Managing personal finances can be difficult when data is spread across multiple bank statements. This tool allows users to upload multiple CSV transaction files, merges them into a unified dataset, and applies a **Linear Regression** model to predict spending trends for the upcoming month.

## ✨ Key Features
* **Multi-File Aggregation:** Upload several CSV files at once; the system automatically merges and sorts them by date.
* **ML Expense Forecasting:** Uses a Scikit-learn Linear Regression model to identify spending trends.
* **Dynamic Visualizations:** Interactive bar charts showing monthly spending and category-wise breakdowns.
* **Auto-Cleaning:** Automatically handles date parsing and currency formats, resolving common "hashtag" display errors found in spreadsheet software.



## 🛠️ Tech Stack
* **Frontend:** [Streamlit](https://streamlit.io/) (Web Framework)
* **Data Analysis:** [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
* **Machine Learning:** [Scikit-learn](https://scikit-learn.org/)
* **Visuals:** [Altair](https://altair-viz.github.io/)

---

## ⚙️ Installation & How to Run

### 1. Prerequisites
Ensure you have **Python 3.9 or higher** installed on your machine.

### 2. Setup the Project
Clone this repository to your local machine:

git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME

### 3. Install Dependencies
Install all required Python libraries with a single command:

pip install -r requirements.txt

### 3. Run the Application
Launch the dashboard locally:

streamlit run app.py

The app will open automatically in your browser at http://localhost:8501.

📊 Data Format RequirementsTo use the predictor, ensure your CSV files contain the following columns:Date: Transaction date (e.g., 2026-01-01)Category: The type of expense (e.g., Food, Transport, Rent)Amount: The numerical cost of the transaction.

🧠 How the AI Model WorksThe application groups transactions by month and calculates total spending. It treats the sequence of months as the independent variable ($X$) and the total amount as the dependent variable ($y$).By training a Linear Regression model on this historical data, the app predicts the next value in the sequence, helping users understand if their spending is trending upward or downward.
