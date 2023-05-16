#include<iostream>
#include<vector>
using namespace std;

int main() {
    int a,b;
    cin >> a;
    cin >> b;
    vector<int> A(16);
    
 

    for (int i = 14; i >=0; i=i-2) {
        A[i] = a % 10; 
        a /= 10; 
    }
    for (int i = 15; i >= 0; i=i-2) {
        A[i] = b % 10; 
        b /= 10; 
    }
    
    for (int a = 15; a >1;a--) {
        for (int i = 0; i < 16; i++) {
            if (i == 15)A[i] = 0;
            else {
                A[i] = (A[i] + A[i + 1]) % 10;
            }
        }A[a] = 0;
        
    }

    for (int i = 0; i < 2; i++) {
        cout << A[i];
    }
}