import matplotlib.pyplot as plt
from models.database import DataBase
from prediction.prediction import predict_future_month

db = DataBase()

months = []
products = []
top_products_by_month, repetiton_by_product = db.top_product_by_month()
for month, value in top_products_by_month.items():  # type: ignore
    months.append(month)
    products.append(value)
quantities = list(repetiton_by_product.values())
days_dates, values_days = db.revenue_by_day()  # type: ignore
months_dates, values_months = db.revenue_by_month()  # type: ignore
predict_months, predict_values = predict_future_month()


def daily_revenue_chart():
    plt.figure(figsize=(10, 5))
    plt.title('revenue by day')
    plt.xlabel('date')
    plt.ylabel('revenue (R$)')
    plt.plot(days_dates, values_days,
             linestyle='--', marker='o', color='green')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()


def month_revenue_chart():
    plt.figure(figsize=(10, 5))
    plt.title('revenue by day')
    plt.xlabel('month')
    plt.ylabel('revenue (R$)')
    plt.plot(months_dates, values_months, linestyle='-', marker='o')
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()


def predict_month_revenue_chart():
    plt.figure(figsize=(10, 5))
    plt.title("Revenue Forecast for Next Months")
    plt.xlabel("Month")
    plt.ylabel("Revenue (R$)")
    plt.plot(months_dates, values_months, color='blue', linestyle='-',
             marker='o', label='Real Revenue')

    plt.plot(predict_months, predict_values, color='red', linestyle='-',
             marker='*', label='Predicted Revenue')

    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def top_product_by_month_chart():
    fig, ax = plt.subplots()

    bars = ax.bar(months, quantities, width=0.5)

    for bar, prod in zip(bars, products):
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, h,
                prod, ha='center', va='bottom', rotation=0, fontsize=8)
    ax.set_ylabel('Quantidade vendida')
    ax.set_title('Produto mais vendido por mês')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


top_product_by_month_chart()
