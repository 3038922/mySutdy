#include <iostream>
using namespace std;
int main() {
    int n = 0;
    cin >> n;
     int count = 1;
     for (int i = 1; i <=n; i++)
     {
         for (int j = 0; j < i; j++)
         {  
             cout << count;
             count++;
             if (count > 9)
                 count = 0;
         }
         cout << "\n";
     }
    return 0;
}