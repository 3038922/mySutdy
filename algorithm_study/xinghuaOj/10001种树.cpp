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
} targetList[5000];
void f(target t)
{
    cout << "[" << t.begin << "," << t.end << "," << t.hope << "]" << endl;
}
bool cmp(target a, target b) { return a.end < b.end; }
int main()
{
    // input
    int treeCount = 0, hopeNums = 0, treeNums = 0;
    bool roadList[N] = {false};
    cin >> treeNums;
    cin >> hopeNums;
    for (int i = 0; i < hopeNums; i++)
    {
        cin >> targetList[i].begin >> targetList[i].end >> targetList[i].hope;
    }
    // sort
    sort(targetList, targetList + hopeNums, cmp);
    //for_each(targetList, targetList + hopeNums, f);
    for (auto i = 0; i < hopeNums; i++)
    {
        //cout << "[" << targetList[i].begin << "," << targetList[i].end << "," << targetList[i].hope << "]" << endl;
        if (targetList[i].hope > 0)
        {
            for (auto j = targetList[i].begin; j <= targetList[i].end; j++)
            {
                //先扫一次 看看该节点内有没被标记的
                //   cout << j << ",";
                if (roadList[j])
                    targetList[i].hope--;
            }
            // cout << endl;
            for (auto j = targetList[i].end; j >= targetList[i].begin; j--)
            {
                if (!roadList[j])
                {
                    if (targetList[i].hope < 1)
                        break;
                    roadList[j] = true;
                    //cout << "在 roadlist" << j << "位置种树" << endl;
                    targetList[i].hope--;
                    treeCount++;
                }
            }
        }
    }
    cout << treeCount;
    return 0;
}