#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
class target {
public:
  int begin;
  int end;
  int hope;
  bool operator<(target &t) { return end < t.end; };
};
bool cmp(target a, target b) { return a.end < b.end; }
int main() {
  // input
  int treeCount = 0;
  int treeNums = 0;
  int hopeNUms = 0;
  vector<target> targetList;
  vector<bool> roadList(treeNums + 1, false);
  cin >> treeNums;
  cin >> hopeNUms;
  for (int i = 0; i < hopeNUms; i++) {
    int b = 0, e = 0, h = 0;
    cin >> b >> e >> h;
    targetList.push_back({b, e, h});
  }
  // sort
  sort(targetList.begin(), targetList.end(), cmp);
  for (auto &it : targetList) {
    if (it.hope > 0) {
      for (auto j = it.end; j >= it.begin; j--) {
        if (roadList[j])
          it.hope--;
      }
      for (auto j = it.end; j >= it.begin; j--) {
        if (!roadList[j]) {
          if (it.hope == 0)
            break;
          roadList[j] = true;
          it.hope--;
          treeCount++;
        }
      }
    }
  }
  cout << treeCount;
}