import numpy as np
import matplotlib.pyplot as plt

# Dane wejściowe
np.random.seed(42)
surface = np.linspace(50, 300, 100)  # Powierzchnia w m²
true_slope = 1000  # Rzeczywisty nachylenie (bez regularyzacji)
intercept = 50000  # Stała cena bazowa
noise = np.random.normal(0, 5000, size=surface.shape)  # Szum losowy

# Generowanie danych wyjściowych
true_prices = true_slope * surface + intercept + noise

# Symulacja regularyzacji
low_reg_slope = true_slope  # Minimalna regularyzacja
medium_reg_slope = true_slope * 0.5  # Średnia regularyzacja
high_reg_slope = true_slope * 0.1  # Wysoka regularyzacja

low_reg_prices = low_reg_slope * surface + intercept
medium_reg_prices = medium_reg_slope * surface + intercept
high_reg_prices = high_reg_slope * surface + intercept

# Wykres danych
plt.figure(figsize=(10, 6))
plt.scatter(surface, true_prices, color="gray", label="Dane rzeczywiste (z szumem)", alpha=0.6)
plt.plot(surface, low_reg_prices, label="Minimalna regularyzacja (Brak hamulca)", linewidth=2)
plt.plot(surface, medium_reg_prices, label="Średnia regularyzacja (Umiarkowany hamulec)", linestyle='--', linewidth=2)
plt.plot(surface, high_reg_prices, label="Wysoka regularyzacja (Silny hamulec)", linestyle='-.', linewidth=2)

# Opis wykresu
plt.title("Wpływ regularyzacji na nachylenie modelu liniowego", fontsize=14)
plt.xlabel("Powierzchnia domu (m²)", fontsize=12)
plt.ylabel("Cena domu (PLN)", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)
plt.tight_layout()

# Wyświetlenie wykresu
plt.show()