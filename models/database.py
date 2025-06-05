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
            custumer TEXT,
            product TEXT,
            price REAL
        )
    ''')
        self.conn.commit()

    def add_sale(self, sale: Sale):
        self.cursor.execute(f'INSERT INTO {TABLE_NAME} '
                            '(date, custumer, product, price) '
                            'VALUES (?, ?, ?, ?)',
                            (sale.date, sale.custumer,
                             sale.product, sale.price)
                            )

    def list_sales(self):
        self.cursor.execute(f'SELECT * FROM {TABLE_NAME}')
        return self.cursor.fetchall()
