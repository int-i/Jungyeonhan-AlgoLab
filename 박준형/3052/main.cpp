#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int n;
	int a,count=0;
	vector<int> nums;
	for (int i = 0; i < 10; i++)
	{
		cin >> n;
		a = n%42;
		if (find(nums.begin(), nums.end(), a)==nums.end())
		{
			nums.push_back(a);
			count++;
		}
	}
	cout << count;
	return 0;
}