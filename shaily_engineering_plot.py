import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Historical closing prices and dates
dates = [
    "2025-06-02", "2025-06-03", "2025-06-04", "2025-06-05", "2025-06-06", "2025-06-09", "2025-06-10", "2025-06-11",
    "2025-06-12", "2025-06-13", "2025-06-16", "2025-06-17", "2025-06-18", "2025-06-19", "2025-06-20", "2025-06-23",
    "2025-06-24", "2025-06-25", "2025-06-26", "2025-06-27", "2025-06-30", "2025-07-01", "2025-07-02", "2025-07-03",
    "2025-07-04", "2025-07-07", "2025-07-08", "2025-07-09", "2025-07-10", "2025-07-11", "2025-07-14", "2025-07-15",
    "2025-07-16", "2025-07-17", "2025-07-18", "2025-07-21", "2025-07-22", "2025-07-23"
]
closes = [
    1997.9, 1911.2, 1882.1, 1803, 1754, 1759.8, 1790.1, 1783.8, 1764.6, 1738.1, 1749.9, 1755.6, 1776.3, 1719.7, 1719.9,
    1732.2, 1745.8, 1680, 1657.6, 1699.3, 1663.5, 1632.8, 1639, 1643.7, 1628.4, 1613, 1597.6, 1615.7, 1611.4, 1611.8,
    1606.5, 1632.4, 1632, 1633.6, 1645.1, 1670.1, 1632.4, 1635
]

# Convert dates to ordinal for regression
x = np.array([datetime.strptime(d, "%Y-%m-%d").toordinal() for d in dates])
y = np.array(closes)

# Fit linear trendline
coeffs = np.polyfit(x, y, 1)
trendline = np.poly1d(coeffs)

# Plot
plt.figure(figsize=(12,6))
plt.plot(dates, closes, label='Closing Price', marker='o')
plt.plot(dates, trendline(x), label='Trendline', linestyle='--')
plt.xticks(rotation=45)
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.title('Shaily Engineering Plastics Ltd (SHAILY) - Price Trendline')
plt.legend()
plt.tight_layout()
plt.show()