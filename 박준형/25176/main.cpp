#include <iostream>

using namespace std;

int main() {	//12341234, 14321432 ó�� ó�� 4�� �迭�ѰŸ� �Ȱ��� �ݺ��ؾ߸� �ּ������� 4�� �迭�ϴ� ����.
	int N;
	cin >> N;
	int sum = 1;
	for (int i = 1; i <= N; i++) {
		sum = sum * i;
	}
	cout << sum;
}