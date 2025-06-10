import matplotlib.pyplot as plt
from models.database import DataBase
from prediction.prediction import predict_future_month

db = DataBase()
days_dates, values_days = db.revenue_by_day()  # type: ignore

months_dates, values_months = db.revenue_by_month()  # type: ignore


def daily_revenue_chart():
    plt.figure(figsize=(10, 5))
    plt.title('revenue by day')
    plt.xlabel('date')
    plt.ylabel('revenue (R$)')
    plt.plot(days_dates, values_days, linestyle='--', marker='o')
    plt.tight_layout()
    plt.grid(True)
    plt.show()


def month_revenue_chart():
    plt.figure(figsize=(10, 5))
    plt.title('revenue by day')
    plt.xlabel('date')
    plt.ylabel('revenue (R$)')
    plt.plot(months_dates, values_months, linestyle='--', marker='o')
    plt.tight_layout()
    plt.grid(True)
    plt.show()
