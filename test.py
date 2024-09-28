import cmath
import math

PI = 3.14159265

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

def sft(x, p1, p2):
    N = len(x)
    A1 = [0] * N

    for k1 in range(p1):
        for j2 in range(p2):
            A1[k1 + j2 * p1] = 0
            for j1 in range(p1):
                angle = 2 * PI * j1 * k1 / p1
                e = cmath.exp(-1j * angle)
                A1[k1 + j2 * p1] += x[j2 + p2 * j1] * e
            A1[k1 + j2 * p1] /= p1

    A2 = [0] * N
    for k1 in range(p1):
        for k2 in range(p2):
            A2[k1 + k2 * p1] = 0
            for j2 in range(p2):
                angle = 2 * PI * j2 / (p1 * p2) * (k1 + p1 * k2)
                e = cmath.exp(-1j * angle)
                A2[k1 + k2 * p1] += A1[k1 + j2 * p1] * e
            A2[k1 + k2 * p1] /= p2

    return A2

def rsft(x, p1, p2):
    N = len(x)
    A1 = [0] * N

    for k1 in range(p1):
        for j2 in range(p2):
            A1[k1 + j2 * p1] = 0
            for j1 in range(p1):
                angle = 2 * PI * j1 * k1 / p1
                e = cmath.exp(1j * angle)
                A1[k1 + j2 * p1] += x[j2 + p2 * j1] * e

    A2 = [0] * N
    for k1 in range(p1):
        for k2 in range(p2):
            A2[k1 + k2 * p1] = 0
            for j2 in range(p2):
                angle = 2 * PI * j2 / (p1 * p2) * (k1 + p1 * k2)
                e = cmath.exp(1j * angle)
                A2[k1 + k2 * p1] += A1[k1 + j2 * p1] * e

    return A2

def main():
    a = [complex(i, 0) for i in range(9)]
    b = [complex(i, 0) for i in range(9)]
    
    N = len(a) + len(b) - 1
    p1 = int(math.sqrt(len(a)))
    p2 = int(math.sqrt(len(a)))
    
    print("\nTransformation:")
    
    a = sft(a, p1, p2)
    p1 = int(math.sqrt(len(b)))
    p2 = int(math.sqrt(len(b)))
    b = sft(b, p1, p2)
    
    print("a:", [f"{x.real:.4f} + {x.imag:.4f}j" for x in a])
    print("b:", [f"{x.real:.4f} + {x.imag:.4f}j" for x in b])

    c = [0] * N
    for i in range(N):
        for j in range(len(a)):
            for t in range(len(b)):
                if j + t == i:
                    c[i] += a[j] * b[t]
        print(f"{c[i].real:.4f} + {c[i].imag:.4f}j")

    print("\nReverse:")
    
    p1 = int(math.sqrt(len(a)))
    p2 = int(math.sqrt(len(a)))
    a = rsft(a, p1, p2)
    p1 = int(math.sqrt(len(b)))
    p2 = int(math.sqrt(len(b)))
    b = rsft(b, p1, p2)
    
    print("a:", [f"{x.real:.4f} + {x.imag:.4f}j" for x in a])
    print("b:", [f"{x.real:.4f} + {x.imag:.4f}j" for x in b])

    for i in range(N):
        c[i] = 0
        for j in range(len(a)):
            for t in range(len(b)):
                if j + t == i:
                    c[i] += a[j] * b[t]
        print(f"{c[i].real:.4f} + {c[i].imag:.4f}j")


if __name__ == "__main__":
    main()
