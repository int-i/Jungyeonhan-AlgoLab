//1   2   3   4   5
//3   3   4   4
//1   1   1   1   0
//2
//
//1   2   1   1   0
#include <iostream>
#include <vector>
using namespace std;

int main() {
	int M, N;
	cin >> N;  cin >> M;
	vector<int> vec(N);
	int i, j, k;
	for (int a = 0; a < M;a++) {
		cin >> i >> j >> k;
		for (int b = i - 1;b < j;b++)
		{
			vec[b] = k;
		}
	}
	for (int c = 0; c < N;c++) {
		cout << vec[c] << " ";
	}
}
