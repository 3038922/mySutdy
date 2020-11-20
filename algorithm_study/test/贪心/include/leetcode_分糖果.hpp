#include <algorithm>
#include <iostream>
#include <map>
#include <vector>
/******
1 1
2 2
3 3
4 4
5 5
6 5
******/
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
        for (auto it:vecList)
        {
            cout<<it.first<<" "<<it.second<<endl;
        }
        int ans = 0;
        for (int j =0;j< vecList.size();j++)
        // if (countNums %2) //如果种类是偶数
        // ;
        // else //种类是奇数
        // ;
            if(vecList[j].second>0)
            {    
                if (j < countNums / 2)
                     {
                         vecList[j].second--;
                         ans++;
                         contione ;
                     }
              
            }
        return ans;
    }
};