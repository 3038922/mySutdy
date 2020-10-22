#include <iostream>
#include <string>
using namespace std;

bool prime(int pre) {
  pre = sqrt(pre);
  if (pre < 2)
    return false;
  if (pre == 2)
    return true;
  for (int i = 2; i < pre; i++)
    if (pre % i == 0)
      return false;
  return true;
}
int main() {
  int arr[150] = {0};
  string str;
  int max = 0, min = 65536;
  cin >> str;
  for (int i = 0; i < str.length(); i++)
    arr[static_cast<int>(str[i])]++; //按askii编号累加
  for (int i = static_cast<int>('a'); i <= static_cast<int>('z'); i++) {
    if (arr[i] > max)
      max = arr[i];
    if (arr[i] < min && arr[i] > 0)
      min = arr[i];
  }
  bool now = prime(max - min);
  cout << (now ? "Lucky Word" : "No Answer") << '\n';
  cout << (now ? max - min : 0) << endl;
  return 0;
}