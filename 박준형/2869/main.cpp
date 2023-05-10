#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int A, B, V;
    cin >> A >> B >> V;

    int climbing_per_day = A - B;
    int distance_to_cover = V - A;

    // 마지막 날을 포함한 전체 일수 계산
    int days = (int)floor((double)distance_to_cover / climbing_per_day) + 1;

    if (distance_to_cover % climbing_per_day != 0) {
        days += 1;
    }

    cout << days;
}
