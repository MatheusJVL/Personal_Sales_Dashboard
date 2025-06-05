from models.database import DataBase
from models.sale import Sale


def main():
    db = DataBase()
    db.creat_table()

    sale = Sale('Matheus', 20.4, 'liquidificador', '14/12/2005')
    db.add_sale(sale)

    sales = db.list_sales()

    for s in sales:
        print(s)


if __name__ == '__main__':
    main()
