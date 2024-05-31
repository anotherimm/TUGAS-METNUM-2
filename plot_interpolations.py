import numpy as np
import matplotlib.pyplot as plt
from lagrange_interpolation import lagrange_interpolation
from newton_interpolation import newton_interpolation

# Data dari soal
x_data = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_data = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Rentang nilai x untuk plot
x_plot = np.linspace(5, 40, 100)

# Interpolasi menggunakan Lagrange
y_lagrange = lagrange_interpolation(x_data, y_data, x_plot)

# Interpolasi menggunakan Newton
y_newton = [newton_interpolation(x_data, y_data, xi) for xi in x_plot]

# Plot hasil interpolasi
plt.figure(figsize=(12, 6))

# Plot Lagrange
plt.subplot(1, 2, 1)
plt.plot(x_data, y_data, 'o', label='Data points')
plt.plot(x_plot, y_lagrange, label='Lagrange Interpolation')
plt.legend()
plt.xlabel('Tegangan, x (kg/mm^2)')
plt.ylabel('Waktu patah, y (jam)')
plt.title('Interpolasi Polinom Lagrange')

# Plot Newton
plt.subplot(1, 2, 2)
plt.plot(x_data, y_data, 'o', label='Data points')
plt.plot(x_plot, y_newton, label='Newton Interpolation')
plt.legend()
plt.xlabel('Tegangan, x (kg/mm^2)')
plt.ylabel('Waktu patah, y (jam)')
plt.title('Interpolasi Polinom Newton')

plt.tight_layout()
plt.show()
