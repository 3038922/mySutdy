
#include "circular_buffer.hpp"
#include "userConfig.hpp"
#include <string>

//递归打印
void recursionPrintTest(const json &pragma, std::string_view ignore)
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
                    recursionPrintTest(val, ignore);
                }
            }
            break;
        }
        case json::value_t::array: {
            for (auto i = pragma.cbegin(); i != pragma.cend() - 1; ++i)
            {
                std::cout << i.value() << " ";
                recursionPrintTest(*i, ignore);
            }
            std::cout << std::endl;
            break;
        }
        default:
            break;
    }
}
void circular_bufferTest()
{
    // constructors accept iterators, initializer lists or count + element
    ncrapi::circular_buffer<int, 4> cb{100, 999, 888};
    cb.push_back(4444); // 1234
    cb.push_back(555);  // 1235
    cb.push_back(777);  // 1235
    // iterators are supported and constexpr ( except reverse ones because std::reverse_iterator )
    // for (auto &value : cb)
    //     std::cout << value << " ";
    // std::cout << "\n";
    std::cout << "cb back():" << cb.back() << " cb back()-1:" << cb.data()[0] << std::endl;
    cb.size();     // 3
    cb.max_size(); // 4
    cb.clear();
    for (auto &value : cb)
        std::cout << "cb clear:" << value << " "; //没输出任何东西
    std::cout << "cb clear:" << cb.size() << " back():" << cb.back() << std::endl;
    cb.push_back(111);
    std::cout << "cb clear:" << cb.size() << " back():" << cb.back() << std::endl;
    ncrapi::circular_buffer<int, 4> cb1;
    std::cout << "cb1: size():" << cb1.size() << " back():" << cb1.back() << std::endl;
    //
    // this can also be done constexpr.
    // using c++14 the only non constexpr api is emplace_back and emplace_front
}
int main(int argc, char *argv[])
{
    system("chcp 65001");
    // recursionPrintTest(userData, "马达");
    circular_bufferTest();
    return 0;
}