#pragma once
#include "userAPI.hpp"

namespace sheep {
class sheep_main : public sheep::sheepAPI
{
  public:
    sheep_main()
    {
    }
    ~sheep_main()
    {
    }
    void Init()
    {
        sheep::sheepAPI::API_Init();
    }
    void Function()
    {
        while (true)
        {
            ;
        }
    }
    void End()
    {
    }

  private:
};
} // namespace sheep