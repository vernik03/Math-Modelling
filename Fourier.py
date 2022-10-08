from ast import main
import numpy as np
import matplotlib.pyplot as plt

# дискретное преобразование Фурье
def DFT(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

# считать точки из файла из одной линии с разделителем пробел 
def readPointsFromFile(filename):
    with open(filename, 'r') as f:
        points = f.read().split(' ')
        points = [float(i) for i in points]
        return points

if __name__ == '__main__':   
    y1 = readPointsFromFile('f1.txt')
    y2 = DFT(y1)
    x = np.arange(len(y1))
    plt.plot(x, y1, 'r', 'points')
    plt.show()
    plt.plot(x, y2, 'b', 'DFT(points)')
    plt.show()

