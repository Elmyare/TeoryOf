#include <iostream>
#include <vector>

using namespace std;

typedef vector<vector<int>> Vector;

int theft(Vector& product, Vector& backpack, int S) {
	if (S < 0)
		return 0;
	int max = 0, index{};
	for (int i = 0; i < product.size(); i++)
		if (S - product[i][0] > -1) {
			int temp = backpack[S - product[i][0]][0] + product[i][1];
			if (max < temp) {
				max = temp;
				index = i;
			}
		}
		else if (i == 0)
			return 0;
	backpack[S][0] += max;
	for (int i = 1; i < product.size() + 1; i++)
		backpack[S][i] = backpack[S - product[index][0]][i];
	backpack[S][index + 1]++;
	return backpack[S][0];
}

int main() {
	int S = 23;
	Vector product = {
		{5,9},
		{7,13},
		{11,21}
	};
	Vector backpack(S + 1, vector<int>(4));

	for (int i = 0; i < S + 1; i++)
		theft(product, backpack, i);

	//for (int i = 0; i < S + 1; i++) {
		//cout << i << ": ";
		for (int j = 0; j < 4; j++)
			cout << backpack[S][j] << " ";
		cout << endl;
	//}
}