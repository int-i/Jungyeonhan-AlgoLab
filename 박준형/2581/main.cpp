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
			if (i % j == 0)		//�Ҽ��� �ƴ� ����.
			{
				s++;		//������������ ���ڰ� �ϳ��� ������ s!=0
			}
		}
			if (s == 0) {
				vec.push_back(i);
			}
			s = 0;				//�ٽ��ʱ�ȭ
	}
	//cout << "�Ҽ������� " << vec.size() << endl;
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