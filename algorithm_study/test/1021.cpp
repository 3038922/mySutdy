#include <iostream>
#include <string>
using namespace std;

bool isPrime(const int n) {
  if (n < 2)
    return false;
  if (n == 2)
    return true;
  if (n % 2 == 0)
    return false;
  int stop = sqrt(n);
  for (int i = 2; i <= stop + 1; i++)
    if (n % i == 0)
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
  bool now = isPrime(max - min);
  cout << (now ? "Lucky Word" : "No Answer") << '\n';
  cout << (now ? max - min : 0) << endl;
  return 0;
}