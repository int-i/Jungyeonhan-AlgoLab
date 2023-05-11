#include<iostream>
using namespace std;


int main() {
	int t, a, b, c;
	a = 0; b = 0; c = 0;
	cin >> t;

	if (t % 10 != 0) {
		cout << "-1";
		return 0;
	}
	while (t/300 > 0) {
			t = t - 300;
			a++;
	}
	
	while (t / 60 > 0) {
		t = t - 60;
		b++;
	}

	while (t / 10 > 0) {
		t = t - 10;
		c++;
	}

	cout << a <<" " << b <<" " << c;
	return 0;
}