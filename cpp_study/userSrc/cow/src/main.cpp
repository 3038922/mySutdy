#include <iostream>
using namespace std;
int main() {
  system("chcp 65001");
  std::string asd;
  int aj;
  cout << "请输入您的账号:";
  cin >> asd;
  cout << "您的等级是: ";
  cin >> aj;
  std::cout << "姓名：凯皇\n性别：男♂\n";
  cout << "种族：凯皇——战士\n";
  cout << "技能1攻击力: " << 1000000 * aj << "\n";
  cout << "技能2攻击力: " << 1000000 * aj << "\n";
  cout << "技能3攻击力: " << 1000008 * aj << "\n";
  cout << "生命力：" << 10000 * aj << "\n" << endl;

  return 0;
}