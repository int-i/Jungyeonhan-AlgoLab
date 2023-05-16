#include<iostream>
#include<vector>
#include <algorithm>
using namespace std;

int main() {
	int n,tmp,k;
	cin >> n;
	vector <int> a;
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		a.push_back(tmp);
	}
	cin >> k;

	int num = n / 2;
	while (num >= 1) {
		int gap = n / num; 
		for (int i = 0; i < n - 1; i = i + gap) {
			sort(a.begin() + i, a.begin() + i + gap);
		}
		if (num == k) {
			for (int i = 0; i < n; i++) {
				cout << a[i]<<" ";
				
			}break;
		}
		num /= 2;
	}

}
