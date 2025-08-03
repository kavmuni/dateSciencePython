# numpy and Pandas

import pandas as pd
import numpy as np

#Raw file link - https://raw.githubusercontent.com/Laxminarayen/Inceptez-batch-25-Classwork/refs/heads/main/Python-Class10-Pandas-Intermediate/orders.csv
orders_csv=pd.read_csv("https://raw.githubusercontent.com/Laxminarayen/Inceptez-batch-25-Classwork/refs/heads/main/Python-Class10-Pandas-Intermediate/orders.csv")
#print(type(orders_csv)) # <class 'pandas.core.frame.DataFrame'>
print(orders_csv.head())
print(orders_csv.dtypes)
"""
[5 rows x 9 columns]
Order Id              object
Date                  object
Meal Id               object
Company Id            object
Date of Meal          object
Participants          object
Meal Price           float64
Type of Meal          object
Heroes Adjustment     object
"""
orders_csv['Date'] = pd.to_datetime(orders_csv['Date'])
print(orders_csv.dtypes)
"""
dtype: object
Order Id                     object
Date                 datetime64[ns]
Meal Id                      object
Company Id                   object
Date of Meal                 object
Participants                 object
Meal Price                  float64
Type of Meal                 object
Heroes Adjustment            object
"""

print(orders_csv['Date'].dt.year.head(5)) # date accessor

print(orders_csv['Participants'].head(2))

print(orders_csv['Type of Meal'].head(10).str.zfill(width = 10))
"""
0    0Breakfast
1    0000Dinner
2    00000Lunch
3    0000Dinner
4    00000Lunch
5    0000Dinner
6    0000Dinner
7    0Breakfast
8    00000Lunch
9    0000Dinner
Name: Type of Meal, dtype: object
"""
orders_csv['Type of Meal'] = orders_csv['Type of Meal'].astype('category')
print(orders_csv.dtypes)
"""
Name: Type of Meal, dtype: object
Order Id                     object
Date                 datetime64[ns]
Meal Id                      object
Company Id                   object
Date of Meal                 object
Participants                 object
Meal Price                  float64
Type of Meal               category
Heroes Adjustment            object
dtype: object
"""
print(orders_csv['Type of Meal'].value_counts())
"""
Dinner       4848
Breakfast    4766
Lunch        4747
Name: count, dtype: int64 
"""