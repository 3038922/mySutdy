#include <array>
#include <iostream>
#include <string>

using namespace std;
int main() {
  std::array<string, 10> cityNum = {"A", "B", "C", "D", "E",
                                    "F", "G", "R", "S", "T"};
  int n = 0;
  string carNum;
  cin >> n;
  int count = n;
  for (int i = 0; i < n; i++) {
    cin >> carNum;
    carNum.erase(1, 5);
    for (auto it : cityNum) {
      if (it == carNum) {
        count--;
        break;
      }
    }
  }
  cout << count;
}