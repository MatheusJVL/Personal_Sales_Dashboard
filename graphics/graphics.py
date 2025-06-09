import matplotlib.pyplot as plt
from datetime import datetime
from models.database import DataBase

revenue_by_day = {}  # type: ignore

db = DataBase()

sales = db.list_sales()
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

plt.figure(figsize=(10, 5))
plt.title('revenue by day')
plt.xlabel('date')
plt.ylabel('revenue (R$)')
plt.plot(dates, values, linestyle='--', marker='o')
plt.tight_layout()
plt.grid(True)
plt.show()
