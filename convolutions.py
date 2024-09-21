import numpy as np
import math
#from scipy.fft import fft, ifft

# Обычная свёртка (с наивной сложностью O(N^2))
def convolution_naive(a, b):
    N = len(a) + len(b) - 1
    result = np.zeros(N, dtype=complex)
    
    for i in range(N):
        for j in range(len(a)):
            for t in range(len(b)):
                if j + t == i:
                    result[i] += a[j] * b[t]
    return result

# Свёртка через дискретное преобразование Фурье (DFT) O(N^2)
def dft(x):
    N = len(x)
    A = np.zeros(N, dtype=complex)
    
    for k in range(N):
        for j in range(N):
            angle = 2 * math.pi * k * j / N
            A[k] += x[j] * np.exp(-1j * angle)
    return A / N

def idft(X):
    N = len(X)
    A = np.zeros(N, dtype=complex)
    
    for k in range(N):
        for j in range(N):
            angle = 2 * math.pi * k * j / N
            A[k] += X[j] * np.exp(1j * angle)
    return A

def convolution_dft(a, b):
    N = len(a) + len(b) - 1
    a_padded = np.pad(a, (0, N - len(a)))
    b_padded = np.pad(b, (0, N - len(b)))
    
    A = dft(a_padded)
    B = dft(b_padded)
    
    C = A * B
    return idft(C)

# Полубыстрое преобразование Фурье (SFT) O(N^1.5)
def sft(x, p1, p2):
    N = len(x)
    A1 = np.zeros(N, dtype=complex)
    
    # Первая стадия SFT (по p1)
    for k1 in range(p1):
        for j2 in range(p2):
            for j1 in range(p1):
                angle = 2 * math.pi * j1 * k1 / p1
                A1[k1 + j2 * p1] += x[j2 + p2 * j1] * np.exp(-1j * angle)
            A1[k1 + j2 * p1] /= p1
    
    A2 = np.zeros(N, dtype=complex)
    
    # Вторая стадия SFT (по p2)
    for k1 in range(p1):
        for k2 in range(p2):
            for j2 in range(p2):
                angle = 2 * math.pi * j2 / (p1 * p2) * (k1 + p1 * k2)
                A2[k1 + k2 * p1] += A1[k1 + j2 * p1] * np.exp(-1j * angle)
            A2[k1 + k2 * p1] /= p2
    
    return A2

def rsft(x, p1, p2):
    N = len(x)
    A1 = np.zeros(N, dtype=complex)
    
    # Первая стадия обратного SFT (по p1)
    for k1 in range(p1):
        for j2 in range(p2):
            for j1 in range(p1):
                angle = 2 * math.pi * j1 * k1 / p1
                A1[k1 + j2 * p1] += x[j2 + p2 * j1] * np.exp(1j * angle)
    
    A2 = np.zeros(N, dtype=complex)
    
    # Вторая стадия обратного SFT (по p2)
    for k1 in range(p1):
        for k2 in range(p2):
            for j2 in range(p2):
                angle = 2 * math.pi * j2 / (p1 * p2) * (k1 + p1 * k2)
                A2[k1 + k2 * p1] += A1[k1 + j2 * p1] * np.exp(1j * angle)
    
    return A2

def convolution_sft(a, b):
    N = len(a) + len(b) - 1
    p1 = int(math.sqrt(len(a)))
    p2 = int(math.sqrt(len(a)))
    
    a_sft = sft(a, p1, p2)
    b_sft = sft(b, p1, p2)
    
    C = a_sft * b_sft
    return rsft(C, p1, p2)

# Тестовые данные
a = np.array([i for i in range(10)], dtype=complex)
b = np.array([i for i in range(10)], dtype=complex)

# 1. Обычная свёртка
conv_naive = convolution_naive(a, b)
print("Обычная свёртка:")
print(np.round(conv_naive, 4))

# 2. Свёртка через дискретное преобразование Фурье
conv_dft = convolution_dft(a, b)
print("\nСвертка через DFT:")
print(np.round(conv_dft, 4))

# 3. Свёртка через полубыстрое преобразование Фурье
conv_sft = convolution_sft(a, b)
print("\nCвёртка через SFT:")
print(np.round(conv_sft, 4))
