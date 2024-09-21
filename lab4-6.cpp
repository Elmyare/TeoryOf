#include <iostream>
#include <cmath>

const double PI = 3.14159265358979323846;

// Функция для вычисления дискретного преобразования Фурье (DFT)
void DFT(double* input, double* real_output, double* imag_output, int N) {
    for (int k = 0; k < N; ++k) {
        real_output[k] = 0.0;
        imag_output[k] = 0.0;
        for (int n = 0; n < N; ++n) {
            double angle = 2.0 * PI * k * n / N;
            real_output[k] += input[n] * cos(angle);
            imag_output[k] -= input[n] * sin(angle);
        }
    }
}
/* 
Эта функция вычисляет дискретное преобразование Фурье (DFT) для заданной временной последовательности input размером N точек и сохраняет реальные (real_output) и мнимые (imag_output) части результата DFT для каждой компоненты частоты k.

Процесс работы функции DFT:

Внешний цикл выполняется для каждой компоненты частоты k от 0 до N-1.
Внутренний цикл выполняется для каждой временной точки n от 0 до N-1.
Для каждой пары (k, n) вычисляется угол angle с использованием формулы для преобразования Фурье.
Для каждой компоненты k, реальная часть (real_output[k]) вычисляется как сумма произведений input[n] на cos(angle), а мнимая часть (imag_output[k]) вычисляется как сумма произведений input[n] на -sin(angle).
В результате выполнения функции DFT, массивы real_output и imag_output будут содержать реальные и мнимые части соответствующих компонент DFT для входной временной последовательности.
*/


// Функция для вычисления обратного дискретного преобразования Фурье (IDFT)
void IDFT(double* real_input, double* imag_input, double* output, int N) {
    for (int n = 0; n < N; ++n) {
        output[n] = 0.0;
        for (int k = 0; k < N; ++k) {
            double angle = 2.0 * PI * k * n / N;
            output[n] += (real_input[k] * cos(angle) - imag_input[k] * sin(angle)) / N;
        }
    }
}
/* 
Эта функция вычисляет обратное дискретное преобразование Фурье (IDFT) для заданных реальных (real_input) и мнимых (imag_input) частей DFT и сохраняет результат в массив output.

Процесс работы функции IDFT:

Внешний цикл выполняется для каждой временной точки n от 0 до N-1.
Внутренний цикл выполняется для каждой компоненты частоты k от 0 до N-1.
Для каждой пары (n, k) вычисляется угол angle с использованием формулы для преобразования Фурье.
Для каждой временной точки n, суммируются значения выражения (real_input[k] * cos(angle) - imag_input[k] * sin(angle)) / N для всех компонент частоты k. Это значение затем записывается в соответствующий элемент массива output.
В результате выполнения функции IDFT, массив output будет содержать временную последовательность, которая была исходным входом для DFT.
*/
int main() {
    const int N = 8; // Размер временной последовательности
    double input[N];
    double dft_real[N];
    double dft_imag[N];
    double idft_result[N];
    
    std::cout << "Массив чисел до DFT по функции n^2:" << std::endl;
    // Заполнение входных данных (n^2)
    for (int n = 0; n < N; ++n) {
        input[n] = static_cast<double>(n * n);
        std::cout << "input[" << n << "] = " << input[n] << std::endl;
    }

    // Вычисление DFT
    DFT(input, dft_real, dft_imag, N);

    // Вывод результатов DFT
    std::cout << "Результаты DFT:" << std::endl;
    for (int k = 0; k < N; ++k) {
        std::cout << "DFT[" << k << "] = " << dft_real[k] << " + " << dft_imag[k] << "i" << std::endl;
    }

    // Вычисление IDFT
    IDFT(dft_real, dft_imag, idft_result, N);

    // Вывод результатов IDFT
    std::cout << "Результаты IDFT:" << std::endl;
    for (int n = 0; n < N; ++n) {
        std::cout << "IDFT[" << n << "] = " << idft_result[n] << std::endl;
    }

    return 0;
}
/*
Значение IDFT[0] равное 2.79776e-13 вместо нуля является результатом численных вычислений и, скорее всего, связано с погрешностью при использовании чисел с плавающей точкой в вычислениях. В идеальных условиях, когда преобразования Фурье и обратные преобразования Фурье выполняются точно, IDFT[0] должно быть близко к нулю.

Однако в реальных численных вычислениях с плавающей точкой могут возникать ошибки округления и накопления, которые могут привести к небольшим ненулевым значениям. Эти ошибки могут быть вызваны ограниченной точностью представления чисел с плавающей точкой и округлением в процессе выполнения множества арифметических операций.

Чтобы уменьшить такие ошибки, можно использовать методы улучшения точности численных вычислений, такие как увеличение разрядности чисел с плавающей точкой или другие техники численного анализа.
*/
