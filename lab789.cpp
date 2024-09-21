#include <iostream>
#include <cmath>
#include <complex>
#include <vector>

using namespace std;

const double PI = 3.14159265;

typedef complex<double> Complex;
typedef vector<Complex> Vector;

Vector dft(Vector x) {
    size_t N = x.size();
    Vector A(N);

    for (size_t k = 0; k < N; k++) {
        A[k] = 0;
        for (size_t j = 0; j < N; j++) {
            double angle = 2 * PI * k * j / N;
            Complex e(cos(angle), -sin(angle));
            A[k] += x[j] * e;
        }
        A[k] /= N;
    }

    return A;
}

Vector idft(Vector x) {
    size_t N = x.size();
    Vector A(N);

    for (size_t k = 0; k < N; k++) {
        A[k] = 0;
        for (size_t j = 0; j < N; j++) {
            double angle = 2 * PI * k * j / N;
            Complex e(cos(angle), sin(angle));
            A[k] += x[j] * e;
        }
    }

    return A;
}

Vector sft(Vector x, size_t p1, size_t p2) {
    size_t N = x.size();
    Vector A1(N);

    for (size_t k1 = 0; k1 < p1; k1++)
        for (size_t j2 = 0; j2 < p2; j2++) {
            A1[k1 + j2 * p1] = 0;
            for (size_t j1 = 0; j1 < p1; j1++) {
                double angle = 2 * PI * j1 * k1 / p1;
                Complex e(cos(angle), -sin(angle));
                A1[k1 + j2 * p1] += x[j2 + p2 * j1] * e;
            }
            A1[k1 + j2 * p1] /= p1;
        }

    Vector A2(N);

    for (size_t k1 = 0; k1 < p1; k1++)
        for (size_t k2 = 0; k2 < p2; k2++) {
            A2[k1 + k2 * p1] = 0;
            for (size_t j2 = 0; j2 < p2; j2++) {
                double angle = 2 * PI * j2 / p1 / p2 * (k1 + p1 * k2);
                Complex e(cos(angle), -sin(angle));
                A2[k1 + k2 * p1] += A1[k1 + j2 * p1] * e;
            }
            A2[k1 + k2 * p1] /= p2;
        }

    return A2;
}

Vector rsft(Vector x, size_t p1, size_t p2) {
    size_t N = x.size();
    Vector A1(N);

    for (size_t k1 = 0; k1 < p1; k1++)
        for (size_t j2 = 0; j2 < p2; j2++) {
            A1[k1 + j2 * p1] = 0;
            for (size_t j1 = 0; j1 < p1; j1++) {
                double angle = 2 * PI * j1 * k1 / p1;
                Complex e(cos(angle), sin(angle));
                A1[k1 + j2 * p1] += x[j2 + p2 * j1] * e;
            }
        }

    Vector A2(N);

    for (size_t k1 = 0; k1 < p1; k1++)
        for (size_t k2 = 0; k2 < p2; k2++) {
            A2[k1 + k2 * p1] = 0;
            for (size_t j2 = 0; j2 < p2; j2++) {
                double angle = 2 * PI * j2 / p1 / p2 * (k1 + p1 * k2);
                complex<double> e(cos(angle), sin(angle));
                A2[k1 + k2 * p1] += A1[k1 + j2 * p1] * e;
            }
        }

    return A2;
}


int main() {
	Vector a(100), b(100);
    for (int i = 0; i < 100; i++) {
        a[i] = i;
        b[i] = i;
    }
	size_t N = a.size() + b.size() - 1, p1, p2;
	
    cout << fixed;
    cout.precision(4);

    cout << endl << "Transformation:" << endl;
    /*a = dft(a);
    b = dft(b);*/
    p1 = sqrt(a.size());
    p2 = sqrt(a.size());
    a = sft(a, p1, p2);
    p1 = sqrt(b.size());
    p2 = sqrt(b.size());
    b = sft(b, p1, p2);
    for (size_t i = 0; i < a.size(); i++)
        cout << a[i] << " ";
    cout << endl;
    for (size_t i = 0; i < b.size(); i++)
        cout << b[i] << " ";
    cout << endl;

    Vector c(N);
    for (size_t i = 0; i < N; i++) {
        for (size_t j = 0; j < a.size(); j++)
            for (size_t t = 0; t < b.size(); t++)
                if (j + t == i)
                    c[i] += a[j] * b[t];
        cout << c[i] << endl;
    }

    cout << endl << "Reverse:" << endl;
  /*  a = idft(a);
    b = idft(b);*/
    p1 = sqrt(a.size());
    p2 = sqrt(a.size());
    a = rsft(a, p1, p2);
    p1 = sqrt(b.size());
    p2 = sqrt(b.size());
    b = rsft(b, p1, p2);
    for (size_t i = 0; i < a.size(); i++)
        cout << a[i] << " ";
    cout << endl;
    for (size_t i = 0; i < b.size(); i++)
        cout << b[i] << " ";
    cout << endl;

	for (size_t i = 0; i < N; i++) {
        c[i] = 0;
		for (size_t j = 0; j < a.size(); j++)
			for (size_t t = 0; t < b.size(); t++)
				if (j + t == i)
					c[i] += a[j] * b[t];
		cout << c[i] << endl;
	}

	return 0;
}