#include "main.hpp"
#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;
class Solution
{
  public:
    int distributeCandies(vector<int> &candyType)
    {
        sort(candyType.begin(), candyType.end());
        vector<pair<int, int>> vecList;
        //需要考虑元素种类不对称问题
        int last = -1;
        int i = 0;
        int countNums = 0;
        for (auto &it : candyType)
        {
            if (it != last)
            {           
            vecList.push_back(make_pair(it, count(candyType.begin() + i, candyType.end(), it)));
            countNums++;
            }
            last = it;
            i++;
        }
        sort(vecList.begin(), vecList.end(), [](auto &left, auto &right) { return left.second < right.second; });
        int i=0;
        int ans=0;
        for (auto it : vecList)
            if(i <countNums/2)
                it.second--;
                ans++;
            i++;
        return 0;
    }
};
int main()
{
    vector<int> data = {1, 1, 3, 3, 3, 22, 3, 100};
    Solution a;
    cout << a.distributeCandies(data) << endl;
    return 0;
}