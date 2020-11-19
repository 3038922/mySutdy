#include <iostream>
#include <set>
#include <string>

using namespace std;
int main() {
  string robot1, robot2;
  cin >> robot1;
  cin >> robot2;
  set<char> recoderlist;
  for (auto r1 : robot1)
    for (auto r2 : robot2)
      if (r1 == r2)
        recoderlist.insert(r1);
  auto nums = recoderlist.size();
  if (nums == 0)
    cout << "WuXiao";
  else if (nums == 1)
    cout << "ZhiHui" << '\n' << *recoderlist.begin();
  else {
    cout << "XLuo" << '\n';
    cout << nums << '\n';
    int count = 0;
    for (auto it : recoderlist) {
      if (count < nums - 1)
        cout << it << "-";
      else
        cout << it;
      count++;
    }
  }
}