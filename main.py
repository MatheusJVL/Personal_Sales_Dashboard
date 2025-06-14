from models.database import DataBase
from models.sale import Sale
from charts import charts
from prediction.prediction import predict_future_month


def main():
    while True:
        print("\n--- MENU ---")
        print("[1] Adicionar nova venda")
        print("[2] Ver gráfico diário")
        print("[3] Ver gráfico mensal")
        print("[4] Prever faturamento")
        print("[5] Produto mais vendido por mês")
        print("[0] Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            # solicitar dados e chamar db.add_sale()
            ...
        elif choice == "2":
            charts.daily_revenue_chart()
        elif choice == "3":
            charts.month_revenue_chart()
        elif choice == "4":
            charts.predict_month_revenue_chart()
        elif choice == "5":
            charts.top_product_by_month_chart()
            ...
        elif choice == "0":
            break
        else:
            print("Opção inválida.")


if __name__ == '__main__':
    main()
