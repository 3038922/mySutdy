#include <iostream>
using namespace std;
int main()
{
    system("chcp 65001");
    string account;
    int level;
    cout << "请输入您的游戏账号:" << account << endl;
    cin >> account;
    cout << "*****************您的游戏账号名字是:" << account << endl;
    cout << "*******************请输入您的等级:";
    cin >> level;
    cout << "*********************姓名:百里守约\n性别:男*************************" << endl;
    cout << "种族:人*************************" << endl;
    cout << "*************************职业:射手 " << endl;
    cout << "技能:1.狂风之息2.静谧之眼3.逃脱" << endl;
    cout << "*************************攻击力:" << 600 * level << endl;
    cout << "防御力:" << 50 * level;
    cout << "攻击范围:" << 10 * level * 0.5;

    cout << "血量:" << 5000 * level * 0.5;
    return 0;
}