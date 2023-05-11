#include <iostream>

using namespace std;

int main() {	//12341234, 14321432 처럼 처음 4개 배열한거를 똑같이 반복해야만 최소점수라서 4개 배열하는 경우수.
	int N;
	cin >> N;
	int sum = 1;
	for (int i = 1; i <= N; i++) {
		sum = sum * i;
	}
	cout << sum;
}