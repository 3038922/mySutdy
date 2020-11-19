#pragma once
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        sort(candyType.begin(),candyType.end());
        //需要考虑元素种类不对称问题
        map<int,size_t> mapList;
        int last=candyType[0];
        int count=1;//统计元素个数
        for(auto it:candyType)
        { 
           if(it!=last)
           {  
            auto numes=count(candyType.begin(),candyType.end(),it);
             mapList.insert(it,);
             count=1;
           }
          else
            count++ ;
          last=it;
        }
        for (auto it : nums)
            cout<<it.first<<" "<<it.second<<endl;
    //     for (int i=0; i<candyType.size();i++)
    //                  ;
    //     if(len%2==0)
    //       return len;
    //     else
    //       return len/2+2;
        return  0;
     }
};