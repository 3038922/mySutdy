#include <iostream>
int main() {
  system("chcp 65001");
  system("cls");
  std::string zhanghao;
  int level;
  std::cout << "账号：" << zhanghao << std::endl;
  std::cin >> zhanghao;
  std::cout << "等 级:";
  std::cin >> level;
  std::cout << "姓 名：关公\n" << std::endl;
  std::cout << "性 别：男\n" << std::endl;
  std::cout << "职 业： 战士\n" << std::endl;
  std::cout << "技 能：一刀两断\n " << std::endl;
  std::cout << "生 命：" << 100 * level * 1.5 << std::endl;
  std::cout << "攻 击 力：" << 199 * level * 4.0 << std::endl;
  std::cout << "防 御 力" << 50 * level * 0.5 << std::endl;
  return 0;
}