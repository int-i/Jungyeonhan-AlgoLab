#include <iostream>

using namespace std;
//적어도 3개의 배수


int main() {
	int num[5];
	cin >> num[0] >> num[1] >> num[2] >> num[3] >> num[4];
	int lcm= 1;
	int count=0;
	while (count < 3) {
		count = 0;
		for (int i = 0; i < 5; i++) {
			if (lcm % num[i] == 0) 
				count++;
		}
		lcm++;
	}
	cout << lcm-1;
	return 0;
}