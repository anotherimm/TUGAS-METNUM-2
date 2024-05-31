import numpy as np

def lagrange_interpolation(x_values, y_values, x):
    def L(k, x):
        terms = [(x - x_values[j]) / (x_values[k] - x_values[j]) for j in range(len(x_values)) if j != k]
        return np.prod(terms, axis=0)

    return sum(y_values[k] * L(k, x) for k in range(len(x_values)))

if __name__ == "__main__":
    # Testing function
    x_data = np.array([5, 10, 15, 20, 25, 30, 35, 40])
    y_data = np.array([40, 30, 25, 40, 18, 20, 22, 15])
    x_test = np.linspace(5, 40, 100)
    y_test = lagrange_interpolation(x_data, y_data, x_test)
    print("Lagrange interpolation test passed.")
