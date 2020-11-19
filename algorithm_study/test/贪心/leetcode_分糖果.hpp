#pragma once
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
pair<int, int> cmp(pair<int, int> a,pair<int,int>b)
{
  if(a.second<b.second)
    return a;
}
class Solution {
public:

    int distributeCandies(vector<int>& candyType) {
        sort(candyType.begin(),candyType.end());
        vector<pair<int,int>> vecList;
        //需要考虑元素种类不对称问题
        int last=-1;
        int i=0;
        for(auto &it:candyType)
        { 
        if(it!=last)
           vecList.push_back(make_pair(it, count(candyType.begin()+i, candyType.end(), it)));
        last=it;
        i++;
        }
        sort(vecList.begin(),vecList.end());
        for (auto it : vecList)
           cout<<it.first<<" "<<it.second<<endl;
        return  0;
     }
};