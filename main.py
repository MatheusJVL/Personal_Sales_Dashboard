from models.database import DataBase
from models.sale import Sale


def main():
    db = DataBase()
    db.delet_table()
    db.creat_table()
    sale = Sale(20.4, 'liquidificador', '14/12/2005')
    db.add_sale(sale)
    sale = Sale(4, 'liquidificador', '07/10/2006')
    db.add_sale(sale)
    sale = Sale(11, 'liquidificador', '20/06/2005')
    db.add_sale(sale)
    sale = Sale(20.4, 'liquidificador', '14/04/2005')
    db.add_sale(sale)
    sale = Sale(20.4, 'liquidificador', '14/02/2005')
    db.add_sale(sale)
    sale = Sale(20.4, 'liquidificador', '14/07/2005')
    db.add_sale(sale)
    sale = Sale(20.4, 'liquidificador', '14/10/2005')
    db.add_sale(sale)

    d = db.list_sales()
    for c in d:
        print(c)


if __name__ == '__main__':
    main()
