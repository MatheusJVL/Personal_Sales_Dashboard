import matplotlib.pyplot as plt
from models.database import DataBase
from prediction.prediction import predict_future_month


def load_chart_data(n_predict=4):
    
    db = DataBase()
    try:
        months = []
        products = []
        top_products_by_month, repetition_by_product = db.top_product_by_month()
        for month, value in top_products_by_month.items():
            months.append(month)
            products.append(value)
        quantities = list(repetition_by_product.values())

        days_dates, values_days = db.revenue_by_day()
        months_dates, values_months = db.revenue_by_month()

        # Chama a predição para n_predict meses
        if months_dates and len(months_dates) > 1:
            predict_months, predict_values, _ = predict_future_month(n_predict)
        else:
            predict_months, predict_values = [], []

        return {
            "months": months,
            "products": products,
            "quantities": quantities,
            "days_dates": days_dates,
            "values_days": values_days,
            "months_dates": months_dates,
            "values_months": values_months,
            "predict_months": predict_months,
            "predict_values": predict_values,
        }
    except Exception as e:
        print(f"\033[31mError loading chart data: {e}\033[0m")
        return None


def daily_revenue_chart():
    plt.figure(figsize=(10, 5))
    plt.title('revenue by day')
    plt.xlabel('date')
    plt.ylabel('revenue (R$)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    data = load_chart_data()
    if data:
        plt.plot(data['days_dates'], data['values_days'],
                 linestyle='--', marker='o', color='green')
        plt.show()


def month_revenue_chart():
    plt.figure(figsize=(10, 5))
    plt.title('revenue by day')
    plt.xlabel('month')
    plt.ylabel('revenue (R$)')
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.grid(True)
    data = load_chart_data   
    if data:
        plt.plot(data['months_dates'],  # type: ignore
                 data['values_months'], linestyle='-', marker='o')
        plt.show()


def predict_month_revenue_chart(n):

    plt.figure(figsize=(10, 5))
    plt.title("Revenue Forecast for Next Months")
    plt.xlabel("Month")
    plt.ylabel("Revenue (R$)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    data = load_chart_data(n_predict=n)
    if data:

        plt.plot(data['months_dates'], data['values_months'],
                 color='blue', linestyle='-', marker='o', label='Real Revenue')

        plt.plot(data['predict_months'], data['predict_values'],
                 color='red', linestyle='-', marker='*', label='Predicted Revenue')

        plt.legend()
        plt.show()


def top_product_by_month_chart():
    data = load_chart_data()
    if data:
        fig, ax = plt.subplots()

        bars = ax.bar(data['months'], data['quantities'], width=0.5)

        for bar, prod in zip(bars, data['products']):
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, h,
                    prod, ha='center', va='bottom', rotation=0, fontsize=8)
        ax.set_ylabel('Quantidade vendida')
        ax.set_title('Produto mais vendido por mês')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
