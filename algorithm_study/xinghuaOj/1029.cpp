#include <algorithm>
#include <iostream>
#include <string>

using namespace std;
int main(int argc, char **) {
  int begin = 0, end = 0, count = 0;
  cin >> begin >> end;
  for (int i = begin; i <= end; i++) {
    string tmp = to_string(i);
    for (auto it : tmp)
      if (it == '2')
        count++;
  }
  cout << count << endl;
  return 0;
}