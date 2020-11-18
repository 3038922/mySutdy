#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
const int N = 1e6 + 10;
class target
{
  public:
    int begin;
    int end;
    int hope;
};
void f(target t)
{
    cout << "[" << t.begin << "," << t.end << "," << t.hope << "]" << endl;
}
bool cmp(target a, target b) { return a.end < b.end; }
int main()
{
    // input
    int treeCount = 0, hopeNums = 0, treeNums = 0;
    target targetList[50001];
    bool roadList[N] = {false};
    cin >> treeNums;
    cin >> hopeNums;
    for (int i = 0; i < hopeNums; i++)
    {
        cin >> targetList[i].begin >> targetList[i].end >> targetList[i].hope;
    }
    // sort
    sort(targetList, targetList + hopeNums - 1, cmp);
    // for_each(targetList.begin(), targetList.end(), f);
    for (auto it : targetList)
    {
        //cout << "[" << it.begin << "," << it.end << "," << it.hope << "]" << endl;
        if (it.hope > 0)
        {
            for (auto j = it.begin; j <= it.end; j++)
            {
                //先扫一次 看看该节点内有没被标记的
                //   cout << j << ",";
                if (roadList[j])
                    it.hope--;
            }
            // cout << endl;
            for (auto j = it.end; j >= it.begin; j--)
            {
                if (!roadList[j])
                {
                    if (it.hope < 1)
                        break;
                    roadList[j] = true;
                    //cout << "在 roadlist" << j << "位置种树" << endl;
                    it.hope--;
                    treeCount++;
                }
            }
        }
    }
    cout << treeCount;
    return 0;
}