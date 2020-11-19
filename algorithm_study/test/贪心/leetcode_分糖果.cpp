#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
using namespace std;
int main()
{
    vector<int> candyType={1,1,2111,2,3,3};
    sort(candyType.begin(),candyType.end());
    set<int> myset;
    for(auto it : candyType)
    {
        myset.insert(it);
    }
    auto len=myset.size();
    cout<<len<<endl;
    if(len%2==0)
      cout<<len/2; 
    else
      cout<<len/2+2; 
}