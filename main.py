from models.database import DataBase
from models.sale import Sale


def main():
    db = DataBase()
    db.creat_table()

    sale = Sale(20.4, 'liquidificador', '14/12/2005')
    db.add_sale(sale)

    db.list_sales()



if __name__ == '__main__':
    main()
