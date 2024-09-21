using System.Collections;
using System.Collections.Generic;

namespace _7_10_Сonvolution
{
    public class UsualConvolution
    {
        private int[] _a;
        private int[] _b;
        private int _cLength;
        public int Complexity;

        public UsualConvolution(int[] a, int[] b)
        {
            _cLength = a.Length + b.Length - 1;
            (a, b) = (b, a);
            _a = a;
            _b = b;
        }

        public int[] Execute()
        {
            var c = new int[_cLength];

            for (var i = 0; i < _a.Length; i++)
            {
                for (var j = 0; j < _b.Length; j++)
                {
                    if (i + j >= _cLength)
                        continue;

                    c[i + j] += _a[i] * _b[j];
                    Complexity += 2;
                }
            }

            return c;
        }
    }
}