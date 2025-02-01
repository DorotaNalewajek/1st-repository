from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
import pandas as pd


wine = pd.read_csv("/Users/dorotanalewajek/Documents/ml/Drzewa decyzyjne /wine/'winequality-white.csv'/'winequality-red.csv'")

#print (wine)

# Wczytaj dane z pliku CSV (dostosuj separator, jeśli potrzeba)
df_white = pd.read_csv('winequality-white.csv', delimiter=';')
df_red = pd.read_csv('winequality-red.csv', delimiter=';')
df_combined = pd.concat([df_white, df_red], ignore_index=True)

df_white['wine_type'] = 'white'
df_red['wine_type'] = 'red'

# Podgląd wynikowego zbioru danych
print(df_combined.head())
print(f'Łączna liczba próbek: {df_combined.shape[0]}')

# # Konwersja DataFrame na tablicę numpy
# data_array = df_combined.to_numpy()

# # Wyświetlenie pierwszych 5 wierszy tablicy
# print("Tablica danych (pierwsze 5 wierszy):")
# print(data_array[:5])

# # Rozmiar danych (wiersze, kolumny)
# print("\nKształt tablicy:", data_array.shape)

# # Sprawdzenie typów danych
# print("\nTypy danych w tablicy:", data_array.dtype)
# x , y = wine.data, wine.target

# np.set_printoptions(suppress=True)
# print(np.unique(wine.data))

# print( 'wine features', np.unique(x))
# print ('class labels' , np.unique (y))

pipe = make_pipeline(StandardScaler(), DecisionTreeClassifier())

x_train , x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, shuffle= True ,stratify=y)

# print(f"Liczba cech w danych: {x_train.shape[1]}")
# print(f"Liczba nazw cech: {len(x)}")
# print(f"Number of training points: {len(x_train)}")
# print(f"Number of test points {len(x_test)}")

# print ('Labels counts in y:' , np.bincount(y))
# print('Label counts in y_train:', np.bincount(y_train))
# print('Label counts in y_test:', np.bincount(y_test))

# dtc = DecisionTreeClassifier(random_state=42)

# params = {'max_depth': range(1, 21)}  

# grid = GridSearchCV(dtc, param_grid=params ,cv = 5)
# grid.fit(x_train,y_train)
# #print (grid.cv_results_)
# print ('Best params:', grid.best_params_)
# print('Best score: {:.2f}%'.format(grid.best_score_ * 100))
# print('Best estimator', grid.best_estimator_)

# clf = DecisionTreeClassifier(criterion='entropy', max_depth= 3, random_state=42)
# clf.fit(x_train,y_train)
# print('Test accuracy: %.2f%%' % (clf.score(x_test, y_test) * 100))


# plt.figure(figsize=(15,10))
# plot_tree(clf, 
#           filled=True, 
#           rounded=True, 
#           class_names=['Class 0', 'Class 1', 'Class 2'], 
#           feature_names = wine.feature_names)
# plt.title('Wine quality - Decision Tree / classification')
# plt.show()



