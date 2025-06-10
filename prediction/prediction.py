from datetime import datetime
from dateutil.relativedelta import relativedelta  # type: ignore
from sklearn.linear_model import LinearRegression  # type: ignore
import numpy as np
from models.database import DataBase


def predict_future_month(months_to_predict: int = 4):
    db = DataBase()
    sorted_months, values = db.revenue_by_month()  # type: ignore

    x = np.arange(len(sorted_months)).reshape(-1, 1)
    y = np.array(values)

    model = LinearRegression()
    model.fit(x, y)

    future_x = np.arange(len(sorted_months),
                         len(sorted_months) + months_to_predict).reshape(-1, 1)
    future_y = model.predict(future_x)

    last_date = datetime.strptime(sorted_months[-1], '%m/%Y')
    future_months = [(last_date + relativedelta(month=1 * i)).strftime('%m/%Y')
                     for i in range(1, months_to_predict + 1)]

    all_months = sorted_months + future_months
    all_revenue = list(y) + list(future_y)

    return (all_months, all_revenue)
