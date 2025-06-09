import sqlite3
from models.sale import Sale

TABLE_NAME = 'sales'


class DataBase:
    def __init__(self, db_path='data\\vendas.db'):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def creat_table(self):
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
        self.cursor.execute('DELETE FROM {TABLE_NAME} WHERE id = ?', (id,))
        self.conn.commit()
