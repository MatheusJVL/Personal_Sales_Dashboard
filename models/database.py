import sqlite3
from models.sale import Sale
from datetime import datetime
TABLE_NAME = 'sales'


class DataBase:
    def __init__(self, db_path='data\\vendas.db'):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            product TEXT,
            price REAL
        )
    ''')
        self.conn.commit()

    def add_sales_data(self):
        print('===add sale===')
        product = input('Product Name: ')
        price = float(input('product price: '))
        date = input('date of sale: ')
        sale = Sale(product=product, date=date, price=price)

        self.add_sale(sale)

    def add_sale(self, sale: Sale):
        self.cursor.execute(f'INSERT INTO {TABLE_NAME} '
                            '(date, product, price) '
                            'VALUES (?, ?, ?)',
                            (sale.date, sale.product, sale.price)
                            )
        self.conn.commit()

    def list_sales(self):
        self.cursor.execute(f'SELECT * FROM {TABLE_NAME}')
        data = self.cursor.fetchall()
        return data

    def delet_table(self):
        self.cursor.execute(f'DROP TABLE IF EXISTS {TABLE_NAME}')
        self.conn.commit()

    def delete_sale_by_id(self, id: int):
        self.cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id = ?', (id,))
        self.conn.commit()

    def extract_month_year(self, date_str: str):
        dt = datetime.strptime(date_str, '%d/%m/%Y')
        return dt.strftime('%m/%Y')

    def revenue_by_month(self):
        revenue_by_month = {}  # type: ignore
        sales = self.list_sales()
        for sale in sales:
            date = sale[1]
            price = sale[3]
            month = self.extract_month_year(date)

            if month in revenue_by_month:
                revenue_by_month[month] += price
            else:
                revenue_by_month[month] = price
        sorted_months = sorted(revenue_by_month.keys(),
                               key=lambda m: datetime.strptime(m, '%m/%Y'))
        values = [revenue_by_month[m] for m in sorted_months]
        return (sorted_months, values)

    def revenue_by_day(self):
        revenue_by_day = {}
        sales = self.list_sales()
        for data in sales:
            date = data[1]
            price = data[3]
            if date in revenue_by_day:
                revenue_by_day[date] += price
            else:
                revenue_by_day[date] = price
        dates = sorted(revenue_by_day.keys(),
                       key=lambda d: datetime.strptime(d, "%d/%m/%Y"))
        values = [revenue_by_day[d] for d in dates]
        return (dates, values)

    def top_product_by_month(self):
        products_by_month = {}
        repetiton_by_product = {}
        sales = self.list_sales()

        for sale in sales:
            date = sale[1]
            product = sale[2]
            month = self.extract_month_year(date)
            if month in products_by_month:
                products_by_month[month].append(product)
            else:
                products_by_month[month] = [product]

        sorted_products_by_month = dict(
            sorted(products_by_month.items(),
                   key=lambda m: datetime.strptime(m[0], '%m/%Y')))

        top_products_by_month = {}

        for month, list in sorted_products_by_month.items():
            most_repeated_product = None
            most_repetitions = 0
            for p in list:
                repetitions = list.count(p)
                if repetitions > most_repetitions:
                    most_repeated_product = p
                    most_repetitions = repetitions

            top_products_by_month[month] = most_repeated_product
            repetiton_by_product[month] = most_repetitions

        return top_products_by_month, repetiton_by_product
