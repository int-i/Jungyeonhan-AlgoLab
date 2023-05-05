#include <iostream>
#include <vector>
using namespace std;

int main() {
	string word;
	cin >> word;
	vector<char> letters;
	vector<int> alp(26);
	for (int i = 0; i < alp.size(); i++) {		//초기값 -1설정.
		alp[i] = -1;
	}

	int a=0;
	for (int i = 0; i < word.length(); i++) {
		letters.push_back(word[i]);
	}
	
	for (char c = 'a'; c <= 'z'; c++) {
		for (int i = word.length()-1; i >=0; i--) {
			if (c == letters[i]) {
				alp[a] = i;
			}
		}
		a++;
	}
	for (int i = 0; i < 26;i++) {
		cout << alp[i]<<" ";
	}

}

//#include <iostream>
//#include <string>
//using namespace std;
//int main() {
//    string s;
//    string alphabet = "abcdefghijklmnopqrstuvwxyz";
//    cin >> s;
//    for (int i = 0; i < alphabet.length(); i++)
//        cout << (int)s.find(alphabet[i]) << " ";        //s.find('a') 하면 s에서 a를 찾는다.
//    return 0;
//}