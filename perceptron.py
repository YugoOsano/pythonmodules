# Python machine learning programming p-25
# Perceptron example
import numpy as np
class Perceptron(object):
    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta       # learning rate
        self.n_iter = n_iter # training iteration
        self.random_state = random_state # seed

    def fit(self, X, y):
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                # update of weight w1, ... , wm
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                # update of weight w0
                self.w_[0] += update
                # counting incorrect classification when update is not zero
                errors += int(update != 0.0)
            # store the error for every iteration
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)
