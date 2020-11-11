"""
题目描述
    小伟报名参加中央电视台的智力大冲浪节目。本次挑战赛吸引了众多参赛者，主持人为了表彰大家的勇气，先奖励每个参赛者m元。先不要太高兴！因为这些钱还不一定都是你的！接下来主持人宣布了比赛规则：
    首先，比赛时间分为n个时段，它又给出了很多小游戏，每个小游戏都必须在规定期限ti 前完成（包括边界时间ti）。如果一个游戏没能在规定期限前完成，则要从奖励费m元中扣去一部分钱wi（wi为自然数），不同的游戏扣去的钱可能不一样的。当然，每个游戏本身都很简单，保证每个参赛者都能在一个时段内完成，而且都必须从整时段开始。主持人只是想考考每个参赛者如何安排组织自己做游戏的顺序。作为参赛者，小伟很想赢得冠军，当然更想赢取最多的钱！
     注意：比赛绝对不会让参赛者赔钱。
输入
第1行为m，表示一开始奖励给每位参赛者的钱；
第2行为n，表示有n个小游戏；
第3行有n个整数，分别表示游戏1到n的规定完成期限ti；
第4行有n个整数，分别表示游戏1到n不能在规定期限前完成（包括边界时间）的扣款数wi。
输出
输出共一行一个整数，表示小伟能赢取最多的钱。
样例输入 Copy
10000
7
4 2 4 3 1 4 6
70 60 50 40 30 20 10

样例输出 Copy
9950

提示
【样例解释】一种可行的方案如下图：其中#1代表第1个游戏，#2代表第2个游戏，依次类推。
      
【数据规模】
对于50%的数据： 1≤n≤500；
对于100%的数据：1≤n≤50,000；1≤m≤231-1；1≤ti≤n；1≤wi≤1,000；
"""