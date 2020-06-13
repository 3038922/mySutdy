#include "../include/userAPI.hpp"
sheep::sheepAPI::sheepAPI()
{
}
sheep::sheepAPI::~sheepAPI()
{
}
void sheep::sheepAPI::API_Init()
{
    int cin;
    short count = 0;
    do
    {
        this->debug = false;
        if (count > 0)
            this->printf("输入错误,重新输入\n", 30);
        if (count >= 3)
        {
            this->printf("输入错误次数太多,程序退出\n", 30);
            reset = true;
        }
        this->printf("是否启用调试模式(1代表是,0代表否,只有3次机会)\n:", 30);
        std::cin >> cin;
        if (cin)
            this->debug = true;
        else if (!cin)
            this->debug = false;
        count++;
        system("cls");
    } while (cin != 1 && cin != 0);
}
void sheep::sheepAPI::printf(const char *cin, const int delay_time)
{
    SYSTEMTIME a;
    GetLocalTime(&a);
    for (int i = 0; cin[i] != 0; i++)
    {
        std::cout << cin[i];
        Sleep(delay_time);
    }
    SYSTEMTIME b;
    GetLocalTime(&b);
    if (this->debug)
        std::cout << "打印时间:"
                  << (b.wHour - a.wHour) * 60 * 60 * 1000 + (b.wMinute - a.wMinute) * 60 * 1000 + (b.wSecond - a.wSecond) * 1000 + b.wMilliseconds - a.wMilliseconds
                  << "毫秒" << std::endl;
}
void sheep::sheepAPI::SetTitle(const char *title)
{
    SetConsoleTitle(title);
}
void sheep::sheepAPI::SetColor(int ForeColor, int BackColor)
{
    HANDLE WinHandle = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(WinHandle, ForeColor + BackColor * 0x10);
}
void sheep::sheepAPI::SetCoord(const short x, const short y)
{
    COORD pos = {x, y};
    HANDLE WinHandle = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleCursorPosition(WinHandle, pos);
}