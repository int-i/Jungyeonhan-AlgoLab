#include<stdio.h>
#include <iostream>
using namespace std;
int main() {
	int A, B, V;
	cin >> A >> B >> V;
	int left = V;
	int day = 0;
	while (left > 0) {
		left = left - A;
		day++;
		if (left <= 0) {
			break;
		}
		left = left + B;
	}
	cout << day;

}