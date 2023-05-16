#include<iostream>
#include <vector>
using namespace std;



int main() {

	int n;
	vector <long long> fibo(100);
	cin >> n;
	fibo[0] = 0;
	fibo[1] = 1;
	for (int i = 2; i < 100; i++) {
		fibo[i] = fibo[i-1] + fibo[i-2];
	}

	cout<< fibo[n];
	return 0;

}


//int fibo(int n) {
//	if (n == 0) {
//		return 0;
//	}
//	else if (n == 1) 
//	{ return 1; }
//	else {
//		return fibo(n - 1) + fibo(n - 2);
//	}
//
//}