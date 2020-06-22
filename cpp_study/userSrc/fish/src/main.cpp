#include <iostream>
int main()
{
    system("chcp 65001");
    std::string a;
    int b;
    int c;
    std::cout << "请输入召唤师名字:";
    std::cin >> a;
    std::cout << "您的召唤师的姓名是:" << a << std::endl;
    std::cout << "请输入你的召唤师等级:";
    std::cin >> b;
    std::cout << "您的召唤师等级是:" << b << std::endl;
    std::cout << "请选择你的英雄:(1.亚瑟...暂代开发)";
    std::cin >> c;
    std::cout << "技能1:圣剑冲锋(攻击力:1000)" << std::endl;
    std::cout << "技能2:圣剑守护(攻击力:500)" << std::endl;
    std::cout << "大招:圣剑审判(攻击力:3000)" << std::endl;
    std::cout << "职业:战士" << std::endl;
    std::cout << "生命:" << 5000 * b * 1.3 << std::endl;
    std::cout << "蓝量:无" << std::endl;
    std::cout << "攻击力:" << 300 * b * 0.7 << std::endl;
    std::cout << "防御:" << 200 * b * 1 << std::endl;
}
