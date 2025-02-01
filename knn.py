import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor

# Pobiera i przygotowuje dane
data_root = "https://github.com/ageron/data/raw/main/"
lifesat = pd.read_csv(data_root + "lifesat/lifesat.csv")
X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

# Wizualizuje dane
lifesat.plot(kind='scatter', grid=True,
             x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23_500, 62_500, 4, 9])

# Wybiera model KNeighborsRegressor
model = KNeighborsRegressor(n_neighbors=3)

# Trenuje model
model.fit(X, y)

# Generuje przewidywane wartości dla zakresu X
X_range = np.linspace(X.min(), X.max(), 100)
y_pred = model.predict(X_range.reshape(-1, 1))

# Rysuje prostą regresji (w tym przypadku będzie to linia łącząca punkty)
plt.plot(X_range, y_pred, color='red')

plt.show()

# Uzyskuje przewidywania dla Cypru
X_new = [[37_655.2]]  # PKB Cypru per capita w 2020 r.
print(model.predict(X_new))  # Wynik: [[6.30165767]]