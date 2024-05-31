import numpy as np

def newton_interpolation(x_values, y_values, x):
    def divided_differences(x_values, y_values):
        n = len(y_values)
        coef = np.zeros([n, n])
        coef[:,0] = y_values
        for j in range(1, n):
            for i in range(n - j):
                coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x_values[i + j] - x_values[i])
        return coef[0, :]

    def newton_polynomial(coef, x_values, x):
        n = len(coef) - 1
        p = coef[n]
        for k in range(1, n + 1):
            p = coef[n - k] + (x - x_values[n - k]) * p
        return p

    coef = divided_differences(x_values, y_values)
    return newton_polynomial(coef, x_values, x)

if __name__ == "__main__":
    # Testing function
    x_data = np.array([5, 10, 15, 20, 25, 30, 35, 40])
    y_data = np.array([40, 30, 25, 40, 18, 20, 22, 15])
    x_test = np.linspace(5, 40, 100)
    y_test = [newton_interpolation(x_data, y_data, xi) for xi in x_test]
    print("Newton interpolation test passed.")
