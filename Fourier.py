from ast import main
import numpy as np

# дискретное преобразование Фурье
def DFT(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

if __name__ == '__main__':
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    print(DFT(x))
