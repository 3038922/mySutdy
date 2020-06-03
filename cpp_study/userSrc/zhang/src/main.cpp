#include <iostream>
int main()
{
    system("chcp 65001");
    system("cls");
    std::string account;
    int level;
    std::cout << "请输入您的账号：";
    std::cin >> account;
    std::cout << "您的账号是：" << account << "\n";
    std::cout << "请输入您的等级：";
    std::cin >> level;
    std::cout << "您的账号是:" << account << "\n"
              << "姓名：后羿\n"
              << "职业：射手\n"
              << "等级：" << level
              << "\n性别：男\n"
              << "技能：灼日之矢\n"
              << "血量：" << 10000 * level * 0.5
              << "\n攻击力：" << 500 * level * 1.5
              << "\n防御力：" << 1000 * level * 1.2;
    return 0;
}