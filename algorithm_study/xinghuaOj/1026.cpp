#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
int main() {
  int n = 0, k = 0, num = 0;
  cin >> n >> k;
  vector<int> vec;
  for (int i = 0; i < n; i++) {
    cin >> num;
    vec.push_back(num);
  }
  sort(vec.begin(), vec.end());
  vec.erase(unique(vec.begin(), vec.end()), vec.end());
  if (k <= vec.size()) {
    cout << vec[k - 1];
  } else {
    cout << "No result";
  }
}
