#include <iostream>
int main()
{
    system("chcp 65001");
    system("cls");
    std::string zhanghao;
    int dengji;
    std::cout << "请输入您的账号: ";
    std::cin >> zhanghao;
    std::cout << "请输入您的等级: ";
    std::cin >> dengji;
    system("cls");
    std::cout << "账  号: " << zhanghao << "\n"
              << "等  级: " << dengji << "\n"
              << "姓  名: 后羿\n"
              << "性  别: 男♂\n"
              << "职  业: 射手\n"
              << "技能 1: 多重箭矢\n"
              << "技能 2: 落日余晖\n"
              << "大  招: 灼日之矢\n"
              << "血  量: " << 250 * dengji << "\n"
              << "攻击力: " << 50 * dengji << "\n"
              << "防御力: " << 20 * dengji << "\n"
              << std::endl;
    return 0;
}