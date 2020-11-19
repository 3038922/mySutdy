#include <algorithm>
#include <array>
#include <iostream>
using namespace std;
array<int, 31> arr = {
    0,
    1,
    2,
    4,
};
int main() {
  int m;
  cin >> m;
  for (int i = 4; i <= m; i++) {
    arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3];
  }
  cout << arr[m];
  return 0;
}