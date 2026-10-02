import numpy as np

def linear_regression_normal_equation(X, y):
    X = np.array(X)
    y = np.array(y)

    theta = np.linalg.solve(X.T @ X, X.T @ y)

    return np.round(theta, 4).tolist()