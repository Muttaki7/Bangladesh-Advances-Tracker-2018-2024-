# Bangladesh-Advances-Tracker-2018-2024-
📊 Bangladesh Advances Tracker (2018–2024)

This project analyzes and visualizes **Bangladesh Bank’s data on advances distributed by Divisions, Districts, and Areas (Urban/Rural)** between 2018 and 2024.  
It provides interactive insights into how advances were distributed over time and across regions.

---

## 🚀 Features
- **Dataset Summary**  
  - Total records, missing values, unique divisions/districts  
  - Urban vs. Rural breakdown  
  - Time period coverage

- **Trend Analysis**  
  - Advances growth across years/quarters  
  - Seasonal patterns and quarterly fluctuations

- **Regional Insights**  
  - Top divisions by advances (bar charts)  
  - Division/District-level comparisons  
  - Urban vs. Rural distribution plots

- **Forecasting (Optional)**  
  - Time-series forecasting with Holt-Winters Exponential Smoothing  
  - Supports future outlook on advances growth

---

## 📂 Project Structure
Bangladesh Advances Tracker (2018–2024)/
│── main.py # Main analysis & visualization script
│── data/ # Raw CSV dataset(s)
│── outputs/ # Generated plots & results
│── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/bangladesh-advances-tracker.git
   cd bangladesh-advances-tracker
Create and activate a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
📊 Usage
Place the dataset in the data/ folder.
Example:

kotlin
Copy code
data-resource_2024_06_25_Table-22_Advances_Distributed_by_DivisionsDistricts.csv
Run the analysis script:

bash
Copy code
python main.py
Results:

Summary statistics print in the console

Visualizations (line plots, bar charts) open in new windows

Forecast plots generated if enabled

📦 Dependencies
Main libraries used:

pandas – data manipulation

numpy – numerical computing

matplotlib / seaborn – visualization

statsmodels – time-series forecasting (Holt-Winters)

scikit-learn – clustering and scaling (optional)

Install via:

bash
Copy code
pip install pandas numpy matplotlib seaborn statsmodels scikit-learn
📈 Example Visualizations
Advances over time (2018–2024)

Urban vs. Rural breakdown for Barishal Division

Top 5 divisions by total advances

Forecast of advances using Holt-Winters

📌 Notes
Make sure the dataset headers are cleaned (first row may need to be skipped using skiprows=2).

The script auto-detects the Division/District/Area column and standardizes it as "District".

NaN handling is included for robustness.

🏛️ Data Source
The dataset is collected from the Bangladesh Bank's official publications.

📜 License
MIT License © 2025
Feel free to use, modify, and share.
