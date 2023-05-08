#include <iostream>
#include <vector>
using namespace std;

int main() {
	int M,N;
	cin >> M;
	cin >> N;
	vector<int> vec;
	int sum = 0;
	int s = 0;

	for (int i = M; i <= N; i++) {
		if (i == 1) {
			continue;
		}
		for (int j = 2; j < i ; j++) {
			if (i % j == 0)		//소수가 아닌 조건.
			{
				s++;		//나눠떨어지는 숫자가 하나라도 있으면 s!=0
			}
		}
			if (s == 0) {
				vec.push_back(i);
			}
			s = 0;				//다시초기화
	}
	//cout << "소수개수는 " << vec.size() << endl;
	for (int i = 0; i < vec.size(); i++) {
		//cout << vec[i] << "   ";
		sum += vec[i];
	}
	if (vec.empty()) {
		cout << "-1" << endl;
		
	}
	else {
		cout << sum << endl;
		cout << vec[0] << endl;
	}
	return 0;
}