#include <iostream>
int main() {
  system("chcp 65001");
  system("cls");
  std::string A;
  int level;

  std::cout << "请输入您的账号";
  std::cin >> A;
  std::cout << "请输入您的等级 :";
  std::cin >> level;
  std::cout << "您的账号是:" << A << "\n";

  std::cout << "***姓名***:不羁之风-夏侯惇 \n" << std::endl;
  std::cout << "***种族:人  \n" << std::endl;
  std::cout << "***等级***:" << level << "\n";
  std::cout << "***生命***:" << 3307 * level * 1 << "\n";
  std::cout << "*攻击力**: " << 159 * level * 1 << "\n" << std::endl;
  std::cout << "***护甲***:" << 89 * level * 1 << "\n" << std::endl;
  std::cout << "***蓝条***:" << 430 * level * 1 << "\n" << std::endl;
  std::cout << "***被动***:噬目冷却值：60 消耗：0 "
               "***介绍***:"
               "夏侯惇生命值低于50％时，每一次技能或普通攻击命中目标都会回复3％"
               "的最大生命值，持续8秒；每30秒最多触发一次\n"
            << std::endl;
  std::cout
      << "**1技能***:豪气斩,冷却值：7 消耗：50 "
         "介绍:夏侯惇挥动大刀，向指定方向斩一道刃风，对路径上的敌人造成240/290/"
         "340/390/440/"
         "490（+"
         "100％物理加成）点物理伤害并减少其50％移动速度，持续2秒；刃风命中英雄"
         "后可再次挥动大刀向指定范围方向释放豪气斩，豪气斩会造成240/290/340/"
         "390/440/490（+100％物理加成）点物理伤害并将范围内敌人击飞1秒\n"
      << std::endl;
  std::cout << "**2技能***:龙卷闪,冷却值：12/11/10/9/8/7消耗：60 "
               "***介绍***:夏侯惇对周围敌人造成200/225/250/275/300/"
               "325（+"
               "70％物理加成）点法术伤害；同时获得一个可抵免等同于自身额外最大"
               "生命值15％的护盾，持续5秒；并且夏侯惇的下三次普通攻击将附加100"
               "点真实伤害，持续8秒；每次攻击会减少1秒不羁之刃的冷却时间\n"
            << std::endl;
  std::cout << "**3技能***:不羁之刃,冷却值：15消耗：80 "
               "***介绍***:"
               "夏侯惇向指定目标方向扔出链刃，链刃飞向指定位置或击中敌人后会对"
               "范围内敌人造成300/425/"
               "550(+"
               "118％物理加成）点物理伤害并将自己拉向链刃位置，并且击中的首个敌"
               "人会眩晕1秒；夏侯惇飞抵目标区域后还将追加300/425/"
               "550（+118％物理加成）点物理伤害\n"
            << std::endl;
  std::cout << "***简介***:"
               "夏侯惇属于坦克/"
               "战士类英雄，拥有出色的生存能力，可以依靠被动的回血能力加上二技"
               "能的高额护盾，能让他与其他英雄硬拼的时候占据有利形式，技能的整"
               "体CD都很短，打持久战的能力很强，对线时几乎牢牢吃住其他坦克、战"
               "士英雄，比如刘邦、苏烈、白起、亚瑟，也能与程咬金、老夫子长时间"
               "僵持，缺点是惧怕吕布、典韦这样拥有高额真伤的英雄，后期的肉度比"
               "不上项羽、廉颇，面对后排缺少直接有效的控制\n"
            << std::endl;
  return 0;
}