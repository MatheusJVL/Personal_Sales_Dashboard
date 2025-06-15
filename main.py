from models.database import DataBase
from charts import charts
from prediction.prediction import predict_future_month
from utils import colors as co
from time import sleep
db = DataBase()


def run_forecast():
    try:
        _, _, n = predict_future_month()
        return len(n)
    except ValueError:
        return 0


def main():
    while True:
        print()
        print(co.print_bold("--- MENU ---"))
        print(co.print_blue("[1] Add new sale"))
        print(co.print_blue("[2] View daily revenue chart"))
        print(co.print_blue("[3] View monthly revenue chart"))
        print(co.print_blue("[4] View chart of best-selling product by month"))
        print(co.print_blue("[5] Forecast revenue for future months"))
        print(co.print_red("[6] Delete sale"))
        print(co.print_red("[7] Delete all data"))
        print(co.print_green("[0] Exit"))

        choice = input(co.print_magenta("Choose an option: "))

        if choice == "1":
            print(co.print_yellow('Enter the date in the format: dd/mm/yyyy'))
            try:
                print(co.print_bold('===add sale==='))
                db.add_sales_data()
                print(co.print_green('Sale added successfully.'))
                sleep(1.5)
            except ValueError as e:
                print(
                    co.print_red(f'\nInvalid data, please try again: {e.__class__.__name__}'
                    ))
                sleep(1.5)
        elif choice == "2":
            charts.daily_revenue_chart()

        elif choice == "3":
            charts.month_revenue_chart()

        elif choice == "4":
            charts.top_product_by_month_chart()

        elif choice == "5":
            if run_forecast() <= 1:
                print(co.print_red('\nInsufficient data for the forecast, please add new sales.'))
                sleep(1.5)
                continue
            try:
                n = int(input(co.print_yellow('How many future months do you want to forecast? ')))
                if n <= 0:
                    raise ValueError()
            except ValueError:
                print(co.print_red('Please enter a valid positive number.'))
                sleep(1.5)
                continue

            charts.predict_month_revenue_chart(n)

        elif choice == '6':
            sales = len(db.list_sales())
            if sales == 0:
                print(co.print_red('\nNo sales to delete, please add a sale first'))
                sleep(1.5)
                continue
            print(co.print_bold('\n=== Sales ==='))
            for sale in db.list_sales():
                print(
                    co.print_white(f'\nSale number: [{co.print_cyan(str(sale[0]))}], Date: {sale[1]}, '
                    f'Product: {sale[2]}, Price: R$ {sale[3]}'
                    ))
            sale_id = input(co.print_yellow('Select the sale number you wish to delete: '))
            if sale_id.isdigit():
                sale_id = int(sale_id)
                sales_ids = [sale[0] for sale in db.list_sales()]
                if sale_id not in sales_ids:
                    print(co.print_red('\nPlease choose a valid purchase number.'))
                    sleep(1.5)
                    continue
                db.delete_sale_by_id(sale_id)
                print(co.print_green('Sale deleted successfully.'))
                sleep(1.5)
            else:
                print(co.print_red('\nPlease enter numbers only'))
                sleep(1.5)

        elif choice == '7':
            y_n = input(co.print_yellow(
                "Are you sure you want to delete all data? This will "
                f"permanently remove the database table. [{co.print_green('Y')}{co.print_yellow('/')}{co.print_red('N')}{co.print_yellow(']')}: "
                )).strip().upper()
            if not y_n or y_n[0] not in 'YN':
                print(co.print_red('Please enter yes or no.'))
                sleep(1.5)
                continue
            if y_n[0] == 'Y':
                db.delete_table()
                print(co.print_green('All data deleted successfully.'))
                sleep(1.5)

        elif choice == "0":
            break

        else:
            print(co.print_red('Choose one of the options'))


if __name__ == '__main__':
    main()
