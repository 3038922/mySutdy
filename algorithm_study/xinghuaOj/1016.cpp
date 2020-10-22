#include <iostream>
using namespace std;
class Stu{
public:

Stu(int iNum,int iChinese,int iMath,int iEnglish):_num(iNum),_chiese(iChinese),_math(iMath),_english(iEnglish){
    _total=iChinese+iMath+iEnglish;
 }
~Stu(){ }
int _num=0;
int _chiese=0;
int _math=0;
int _english=0;
int _total;
};