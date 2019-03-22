import numpy as np


class Perceptron(object):
    """
    w_          weight afrer fitting
    errors_     era wrong classification
    """
    def __init__(self, eta=0.01, n_iter=10):
        """
        :param eta:     learning factor 0.0 - 1.0
        :param n_iter:  learn iterations
        """
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        """
        :param X: [n_samples, n_feature] learning vectors
        :param y: [n_namples] target values
        :return: self
        """
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target, in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        """Oblicza całkowite pobudzanie"""
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        """Zwraca etykietę klas po obliczeniu fnkcji skoku jednostkowego"""
        return np.where(self.net_input(X) >= 0.0, 1, -1)

