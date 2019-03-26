import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from perceptron import Perceptron

# plote Parcell length and Flake length
plote_values_1 = False

print("get CSV data of flowers\n")
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
df.tail()

y = df.iloc[0:100, 4].values
print("First %s values (column 5):\n" % (y.size,))
print(y)
y = np.where(y == 'Iris-setosa', -1, 1)
print("Iris-setosa values map true/false:\n")
print(y)
X = df.iloc[0:100, [0, 2]].values
print("First %s values (Parcell length,Flake length)\n"% (X.size / 2,))
print(X)
if plote_values_1:
    # plote first 50 values - iris-setosa
    plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='Setosa')
    # plote 50 to 100 values - iris-versicolor
    plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='Versicolor')
    plt.xlabel('Parcell length [cm]')
    plt.ylabel('Flake length [cm]')
    plt.legend(loc='upper left')
    plt.show()

ppn = Perceptron(eta=0.1, n_iter=10)
ppn.fit(X, y)
plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
plt.xlabel('Epoki')
plt.ylabel('Liczba aktualizacji')
plt.show()

from matplotlib.colors import ListedColormap


def plot_decision_regions(X, y, classifier, resolution=0.02):
    # konfiguruje generator znaczników i mapę kolorów
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # rysuje wykres powierzchni decyzyjnej
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    # rysuje wykres próbek
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1], alpha=0.8, c=cmap(idx), marker=markers[idx], label=cl)


plot_decision_regions(X, y, classifier=ppn)
plt.xlabel('Długość działki [cm]')
plt.ylabel('Długość płatka [cm]')
plt.legend(loc='upper left')
plt.show()

