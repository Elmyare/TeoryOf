import math
import cmath

PI = 3.14159265

# Функция DFT (дискретное преобразование Фурье)
def dft(x):
    N = len(x)
    A = [0] * N
    for k in range(N):
        A[k] = 0
        for j in range(N):
            angle = 2 * PI * k * j / N
            e = cmath.exp(-1j * angle)
            A[k] += x[j] * e
        A[k] /= N
    return A

# Обратное DFT (IDFT)
def idft(x):
    N = len(x)
    A = [0] * N
    for k in range(N):
        A[k] = 0
        for j in range(N):
            angle = 2 * PI * k * j / N
            e = cmath.exp(1j * angle)
            A[k] += x[j] * e
    return A

# Функция SFT (преобразование в двух измерениях)
def sft(x, p1, p2):
    N = len(x)
    A1 = [0] * N

    for k1 in range(p1):
        for j2 in range(p2):
            idx1 = k1 + j2 * p1
            A1[idx1] = 0
            for j1 in range(p1):
                angle = 2 * PI * j1 * k1 / p1
                e = cmath.exp(-1j * angle)
                A1[idx1] += x[j2 + p2 * j1] * e
            A1[idx1] /= p1

    A2 = [0] * N
    for k1 in range(p1):
        for k2 in range(p2):
            idx1 = k1 + k2 * p1
            A2[idx1] = 0
            for j2 in range(p2):
                angle = 2 * PI * j2 / p1 / p2 * (k1 + p1 * k2)
                e = cmath.exp(-1j * angle)
                A2[idx1] += A1[k1 + j2 * p1]
            A2[idx1] /= p2
    return A2

# Обратное SFT (RSFT)
def rsft(x, p1, p2):
    N = len(x)
    A1 = [0] * N

    for k1 in range(p1):
        for j2 in range(p2):
            idx1 = k1 + j2 * p1
            A1[idx1] = 0
            for j1 in range(p1):
                angle = 2 * PI * j1 * k1 / p1
                e = cmath.exp(1j * angle)
                A1[idx1] += x[j2 + p2 * j1]

    A2 = [0] * N
    for k1 in range(p1):
        for k2 in range(p2):
            idx1 = k1 + k2 * p1
            A2[idx1] = 0
            for j2 in range(p2):
                angle = 2 * PI * j2 / p1 / p2 * (k1 + p1 * k2)
                e = cmath.exp(1j * angle)
                A2[idx1] += A1[k1 + j2 * p1]
    return A2

# Основная программа
def main():
    a = [complex(i, 0) for i in range(100)]
    b = [complex(i, 0) for i in range(100)]
    
    N = len(a) + len(b) - 1
    
    print("Transformation:")
    # Преобразование SFT
    p1 = int(math.sqrt(len(a)))
    p2 = p1
    a = sft(a, p1, p2)

    p1 = int(math.sqrt(len(b)))
    p2 = p1
    b = sft(b, p1, p2)

    print(a)
    print(b)

    # Вычисление свертки векторов
    c = [0] * N
    for i in range(N):
        for j in range(len(a)):
            for t in range(len(b)):
                if j + t == i:
                    c[i] += a[j] * b[t]
        print(c[i])

    print("\nReverse:")

    # Обратное преобразование RSFT
    p1 = int(math.sqrt(len(a)))
    p2 = p1
    a = rsft(a, p1, p2)

    p1 = int(math.sqrt(len(b)))
    p2 = p1
    b = rsft(b, p1, p2)

    print(a)
    print(b)

    # Повторное вычисление свертки
    for i in range(N):
        c[i] = 0
        for j in range(len(a)):
            for t in range(len(b)):
                if j + t == i:
                    c[i] += a[j] * b[t]
        print(c[i])

if __name__ == "__main__":
    main()
