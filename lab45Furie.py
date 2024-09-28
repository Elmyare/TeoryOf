import math
import cmath

PI = 3.14159265

# Определяем типы данных
Complex = complex
Vector = list

def dft(x, m):
    N = len(x)
    A = [0] * N

    for k in range(N):
        A[k] = 0
        for j in range(N):
            angle = 2 * PI * k * j / N
            e = Complex(math.cos(angle), -math.sin(angle))
            A[k] += x[j] * e
            m[0] += 1
        A[k] /= N

    return A

def idft(x, m):
    N = len(x)
    A = [0] * N

    for k in range(N):
        A[k] = 0
        for j in range(N):
            angle = 2 * PI * k * j / N
            e = Complex(math.cos(angle), math.sin(angle))
            A[k] += x[j] * e
            m[0] += 1

    return A

def sft(x, p1, p2, m):
    N = len(x)
    A1 = [0] * N

    for k1 in range(p1):
        for j2 in range(p2):
            A1[k1 + j2 * p1] = 0
            for j1 in range(p1):
                angle = 2 * PI * j1 * k1 / p1
                e = Complex(math.cos(angle), -math.sin(angle))
                A1[k1 + j2 * p1] += x[j2 + p2 * j1] * e
                m[0] += 1
            A1[k1 + j2 * p1] /= p1

    A2 = [0] * N

    for k1 in range(p1):
        for k2 in range(p2):
            A2[k1 + k2 * p1] = 0
            for j2 in range(p2):
                angle = 2 * PI * j2 / p1 / p2 * (k1 + p1 * k2)
                e = Complex(math.cos(angle), -math.sin(angle))
                A2[k1 + k2 * p1] += A1[k1 + j2 * p1] * e
                m[0] += 1
            A2[k1 + k2 * p1] /= p2

    return A2

def rsft(x, p1, p2, m):
    N = len(x)
    A1 = [0] * N

    for k1 in range(p1):
        for j2 in range(p2):
            A1[k1 + j2 * p1] = 0
            for j1 in range(p1):
                angle = 2 * PI * j1 * k1 / p1
                e = Complex(math.cos(angle), math.sin(angle))
                A1[k1 + j2 * p1] += x[j2 + p2 * j1] * e
                m[0] += 1

    A2 = [0] * N

    for k1 in range(p1):
        for k2 in range(p2):
            A2[k1 + k2 * p1] = 0
            for j2 in range(p2):
                angle = 2 * PI * j2 / p1 / p2 * (k1 + p1 * k2)
                e = Complex(math.cos(angle), math.sin(angle))
                A2[k1 + k2 * p1] += A1[k1 + j2 * p1] * e
                m[0] += 1

    return A2

def main():
    N = 100
    x = [Complex(i, 0) for i in range(N)]
    p1 = 10
    p2 = 10
    m = [0]

    print("Input sequence:")
    for val in x:
        print(val)

    # print("\nTransformation:")
    # X = dft(x, m)
    # for val in X:
    #     print(val)

    # print("\nReverse:")
    # X = idft(X, m)
    # for val in X:
    #     print(val)

    # print(f"\nOperation counts for N=100, 400, 1600:")
    # print(m[0], end="\t")
    
    # # For N=400
    # m[0] = 0
    # N = 400
    # p1 = 20
    # p2 = 20
    # x2 = [Complex(i, 0) for i in range(N)]
    # X = dft(x2, m)
    # X = idft(X, m)
    # print(m[0], end="\t")

    # # For N=1600
    # m[0] = 0
    # N = 1600
    # p1 = 40
    # p2 = 40
    # x3 = [Complex(i, 0) for i in range(N)]
    # X = dft(x3, m)
    # X = idft(X, m)
    # print(m[0])

    print("\nTransformation:")
    X = sft(x, p1, p2, m)
    for val in X:
        print(val)

    print("\nReverse:")
    X = rsft(X, p1, p2, m)
    for val in X:
        print(val)

    print(f"\nOperation counts for N=100, 400, 1600:")
    print(m[0], end="\t")
    
    # For N=400
    m[0] = 0
    N = 400
    p1 = 20
    p2 = 20
    x2 = [Complex(i, 0) for i in range(N)]
    X = sft(x2, p1, p2, m)
    X = rsft(X, p1, p2, m)
    print(m[0], end="\t")

    # For N=1600
    m[0] = 0
    N = 1600
    p1 = 40
    p2 = 40
    x3 = [Complex(i, 0) for i in range(N)]
    X = sft(x3, p1, p2, m)
    X = rsft(X, p1, p2, m)
    print(m[0])

if __name__ == "__main__":
    main()
