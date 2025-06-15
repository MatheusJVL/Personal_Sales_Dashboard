# Personal Sales Dashboard

A terminal-based Python application to manage and analyze personal sales data.

## 📌 Features

- ✅ Register new sales with product name, price, and date.
- ✅ Store data in an SQLite database.
- 📊 Generate graphical reports with `matplotlib`:
  - Daily revenue
  - Monthly revenue
  - Best-selling product by month
- 📈 Forecast future revenue using linear regression (`scikit-learn`)
- 🧱 Modular structure, ready to be extended with GUI frameworks like **PySide6**

## 💻 Technologies Used

- Python 3.10+
- SQLite (via `sqlite3`)
- `matplotlib`
- `scikit-learn`
- `datetime`

## 🛠️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/MatheusJVL/Personal_Sales_Dashboard.git


2. (Optional but recommended) Create and activate a virtual environment:

    python -m venv venv
    source venv/bin/activate      # For Linux/macOS
    venv\Scripts\activate         # For Windows


3. Install the required dependencies:

    pip install -r requirements.txt


4. Run the application:

    python main.py


📂 Project Structure (simplified)
bash
Copiar
Editar
Personal_Sales_Dashboard/
│
├── data/
│   └── vendas.db               # SQLite database (created at runtime)
│
├── models/
│   └── sale.py                 # Sale class
│
├── charts/
│   └── charts.py               # Functions to generate charts
│
├── prediction/
│   └── prediction.py           # Forecasting logic using scikit-learn
│
├── utils/
│   └── colors.py               # Colored terminal print functions
│
├── main.py                     # Main application loop
├── requirements.txt
└── README.md
📌 Notes
All data is stored locally in the data/vendas.db file.

Make sure the data/ folder exists (it will be created automatically if it doesn't).

Ideal for learning Python, data visualization, and simple ML models in real-world use.

🧑‍💻 Author
Matheus João Vaz Lima