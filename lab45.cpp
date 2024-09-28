#include <iostream>
#include <cmath>
#include <complex>
#include <vector>

using namespace std;

const double PI = 3.14159265;

typedef complex<double> Complex;
typedef vector<Complex> Vector;

Vector dft(Vector x, int &m) {
    size_t N = x.size();
    Vector A(N);

    for (size_t k = 0; k < N; k++) {
        A[k] = 0;
        for (size_t j = 0; j < N; j++) {
            double angle = 2 * PI * k * j / N;
            Complex e(cos(angle), -sin(angle));
            A[k] += x[j] * e;
            m++;
        }
        A[k] /= N;
    }

    return A;
}

Vector idft(Vector x, int& m) {
    size_t N = x.size();
    Vector A(N);

    for (size_t k = 0; k < N; k++) {
        A[k] = 0;
        for (size_t j = 0; j < N; j++) {
            double angle = 2 * PI * k * j / N;
            Complex e(cos(angle), sin(angle));
            A[k] += x[j] * e;
            m++;
        }
    }

    return A;
}

Vector sft(Vector x, size_t p1, size_t p2, int& m) {
    size_t N = x.size();
    Vector A1(N);

    for (size_t k1 = 0; k1 < p1; k1++)
        for (size_t j2 = 0; j2 < p2; j2++) {
            A1[k1 + j2 * p1] = 0;
            for (size_t j1 = 0; j1 < p1; j1++) {
                double angle = 2 * PI * j1 * k1 / p1;
                Complex e(cos(angle), -sin(angle));
                A1[k1 + j2 * p1] += x[j2 + p2 * j1] * e;
                m++;
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
                m++;
            }
            A2[k1 + k2 * p1] /= p2;
        }

    return A2;
}

Vector rsft(Vector x, size_t p1, size_t p2, int& m) {
    size_t N = x.size();
    Vector A1(N);

    for (size_t k1 = 0; k1 < p1; k1++)
        for (size_t j2 = 0; j2 < p2; j2++) {
            A1[k1 + j2 * p1] = 0;
            for (size_t j1 = 0; j1 < p1; j1++) {
                double angle = 2 * PI * j1 * k1 / p1;
                Complex e(cos(angle), sin(angle));
                A1[k1 + j2 * p1] += x[j2 + p2 * j1] * e;
                m++;
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
                m++;
            }
        }

    return A2;
}

int main() {
    cout << fixed;
    cout.precision(4);

    size_t N = 100;
    Vector x(N);
    size_t p1 = 10;
    size_t p2 = 10;
    int m = 0;

    for (size_t i = 0; i < N; i++) {
        x[i] = i;
        cout << x[i] << " ";
    }

    cout << endl << "transformation:" << endl;
    Vector X = dft(x, m);
    for (size_t i = 0; i < N; i++)
       cout << x[i] << endl;

    cout << endl << "reverse:" << endl;
    X = idft(X, m);
    for (size_t i = 0; i < N; i++)
       cout << x[i] << endl;

    cout << "100\t400\t1600" << endl;
    cout << m << "\t";
    m = 0;
    N = 400;
    Vector x2(N);
    for (size_t i = 0; i < N; i++) {
       x2[i] = i;
    }
    X = dft(x2, m);
    X = idft(X, m);
    cout << m << "\t";
    m = 0;
    N = 1600;
    Vector x3(N);
    for (size_t i = 0; i < N; i++) {
       x3[i] = i;
    }
    X = dft(x3, m);
    X = idft(X, m);
    cout << m << endl;

    // cout << endl << "Transformation:" << endl;
    // Vector X = sft(x, p1, p2, m);
    // for (size_t i = 0; i < N; i++)
    //     cout << X[i] << endl;

    // cout << endl << "Reverse:" << endl;
    // X = rsft(X, p1, p2, m);
    // for (size_t i = 0; i < N; i++)
    //     cout << X[i] << endl;

    // cout << "100\t400\t1600" << endl;
    // cout << m << "\t";
    // m = 0; N = 400; p1 = 20; p2 = 20;
    // Vector x2(N);
    // for (size_t i = 0; i < N; i++) {
    //     x2[i] = i;
    // }
    // X = sft(x2, p1, p2, m);
    // X = rsft(X, p1, p2, m);
    // cout << m << "\t";
    // m = 0; N = 1600; p1 = 40; p2 = 40;
    // Vector x3(N);
    // for (size_t i = 0; i < N; i++) {
    //     x3[i] = i;
    // }
    // X = sft(x3, p1, p2, m);
    // X = rsft(X, p1, p2, m);
    // cout << m << endl;

    return 0;
}