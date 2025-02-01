from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Zdanie do zakodowania
zdanie = ["Tomek", "idzie", "do", "szkoły"]

# Transformacja na tablicę 2D (jeden wyraz = jedna kategoria)
dane = np.array(zdanie).reshape(-1, 1)

# Inicjalizacja One-Hot Encodera
encoder = OneHotEncoder(sparse_output=False)  # Zwraca macierz gęstą

# Dopasowanie i transformacja danych
encoded_data = encoder.fit_transform(dane)

# Debugowanie typu przed zmianą
print("Typ danych przed zmianą:", encoded_data.dtype)

# Konwersja na typ object
encoded_data_object = np.array(encoded_data, dtype=object)

# Debugowanie typu po zmianie
print("Typ danych po zmianie:", encoded_data_object.dtype)

# Wyświetlenie zakodowanych danych
print("Zakodowane zdanie (One-Hot Encoding):\n", encoded_data_object)

# Wyświetlenie słownika kategorii
print("Słownik kategorii:", encoder.categories_)