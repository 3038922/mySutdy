
#include "userConfig.hpp"
#include <string>

//递归打印
void recursionPrint(const json &pragma, std::string_view ignore)
{
    switch (pragma.type())
    {
        case json::value_t::object: {
            for (auto &[key, val] : pragma.items())
            {
                if (key != ignore)
                {
                    if (!val.is_object() && !val.is_array())
                        std::cout << key << ": " << val << std::endl; //这里可以右移
                    else
                        std::cout << key << ": " << std::endl;
                    recursionPrint(val, ignore);
                }
            }
            break;
        }
        case json::value_t::array: {
            for (auto i = pragma.cbegin(); i != pragma.cend() - 1; ++i)
            {
                std::cout << i.value() << " ";
                recursionPrint(*i, ignore);
            }
            std::cout << std::endl;
            break;
        }
        default:
            break;
    }
}

int main(int argc, char *argv[])
{
    system("chcp 65001");
    recursionPrint(userData, "马达");
    return 0;
}