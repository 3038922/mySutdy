#include <iostream>

using namespace std;
int main() {
  int a = 0, b = 0;
  for (int i = 0; i < 7; i++) {
    cin >> a >> b;
    if (a + b > 8) {
      cout << i + 1;
      return 0;
    }
  }
  cout << 0;
}