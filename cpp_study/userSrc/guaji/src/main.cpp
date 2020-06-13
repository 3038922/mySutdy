#include <iostream>
int main()
{
    std::string aasiad = {"ffffffff"};
    std::string apsiad = {"ffffffff"};
    std::string account;
    std::string pass;
    int level;
    system("chcp 65001");
    std::cout << "请输入您的账号:";
    std::cin >> account;
    std::cout << "您的账号是:" << account << std::endl;
    std::cout << "请输入您的密码:";
    std::cin >> pass;
    std::cout << "您的密码是:" << pass << std::endl;
    std::cout << "请输入你的等级:" << std::endl;
    std::cin >> level;
    if (account == aasiad && pass == apsiad)
    {
        std::cout << "密码正确,下面开始打印" << std::endl;
        std::cout << "姓名:吕布" << std::endl;
        std::cout << "职业:战士" << std::endl;
        std::cout << "生命:" << 2000 * level * 0.5 << std::endl;
        std::cout << "攻击:" << 100 * level * 1 << std::endl;
        std::cout << "防御:" << 500 * level * 0.7 << std ::endl;
        std::cout << "法防:" << 300 * level * 0.3 << std::endl;
        std::cout << "法攻:" << 10 * level * 0.1 << std::endl;
    }
    else
    {
        std::cout << "密码错误,请再输入一次" << std::endl;
    }
    return 0;
}