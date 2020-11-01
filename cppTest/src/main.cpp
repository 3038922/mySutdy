
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
    ncrapi::circular_buffer<int, 4> cb{1, 2, 3};
    cb.push_back(4); // 1234
    cb.push_back(5); // 1235
    // iterators are supported and constexpr ( except reverse ones because std::reverse_iterator )
    for (auto &value : cb)
        std::cout << value << " ";
    std::cout << "\n"
              << "back():" << cb.back() << std::endl;
    cb.size();     // 3
    cb.max_size(); // 4
    cb.clear();    //
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