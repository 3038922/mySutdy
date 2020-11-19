#pragma once
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
using namespace std;
class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        sort(candyType.begin(),candyType.end());
        //需要考虑元素种类不对称问题
        set<int> myset;
        for(auto it : candyType)
        {
            myset.insert(it);
        }
        auto len=myset.size();
        if(len%2==0)
          return len;
        else
          return len/2+2;
    }
};