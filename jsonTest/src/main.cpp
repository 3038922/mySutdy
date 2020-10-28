#include "chinese.hpp"
#include "json.hpp"
#include <string>
const json userData = {
    {I18N_JSON_VER, 2.4},
    {
        I18N_SYSTEM_INFO,
        {
            {I18N_ROBOT_TYPE, "赛博朋克2077"},
            {I18N_TEAM_NUM, "8982D"},
            {I18N_USER, "bobo"},
        },
    },
    {
        I18N_AUTO,
        {
            {I18N_AUTO "&" I18N_SKILL_AUTO, false},
            {I18N_RED_ALLIANCE "&" I18N_BLUE_ALLIANCE, true},
            {"左边&右边", false},
            {"启用视觉&不启用视觉", false},

        },
    },
    {
        I18N_ODOM_INFO,
        {
            {I18N_ROBOT_LENGTH, 456},
            {I18N_ROBOT_WIDTH, 456},
            {I18N_ROBOT_WEIGHT, 8.132},
            {I18N_WHEEL_DIAMETER, 104},
            {I18N_WHEEL_SPACING, 315.0},
            {I18N_SITE_SIZE, 3445},
            {I18N_GYRO I18N_PROPORTION, 0.936}, //陀螺仪比例
            {I18N_GYRO I18N_BALANCE, 0.01},     //陀螺仪平衡 如果左边360 右边350
                                                //正数 如果左边360 右边370 负数
            {I18N_ADI,
             {
                 {I18N_GYRO, 1},
             }},
        },
    },
    {
        I18N_VISION_INFO,
        {
            {I18N_VISION_FRONT,
             {
                 {I18N_PORT, 17},
                 {I18N_EXPOSURE, 20},
                 {I18N_MAX_HIGH, 75},
                 {I18N_MAX_WIDTH, 65},
                 {I18N_DATA, 0},
                 {I18N_COLOR_RANGE,
                  {
                      {I18N_RED, {8.8, 10.0, 11.0, 10.0, 10.0, 6.9}},
                      {I18N_BLUE, {9.5, 11.0, 11.0, 7.0, 7.1, 11.0}},
                      {I18N_GREEN, {11.0, 9.0, 8.0, 8.3, 10.0, 5.0}},
                  }},
             }},
        },
    },
    {
        "底盘",
        {
            {"马达",
             {
                 {"左前", {{"端口", 1}, {"正反", true}, {"齿轮", 1}}},
                 {"左后", {{"端口", 2}, {"正反", false}, {"齿轮", 1}}},
                 {"右前", {{"端口", 3}, {"正反", false}, {"齿轮", 1}}},
                 {"右后", {{"端口", 4}, {"正反", true}, {"齿轮", 1}}},
             }},
            {"参数",
             {
                 {"左右矫正比例", 1.052},
                 {"遥控器矫正", 10},
                 {"最大旋转速度", 127},
                 {"模式", 0},
             }},
            {"PID参数",
             {
                 {"模式0",
                  {
                      {"速度pid",
                       {{"KP", 0.5},
                        {"KI", 0.001},
                        {"KD", 2.0},
                        {"KBIAS", 0},
                        {"LIMIT", 200},
                        {"Q", 0.01},
                        {"R", 0.02}}},
                      {"前后pid",
                       {{"KP", 0.5},
                        {"KI", 0.001},
                        {"KD", 2.0},
                        {"KBIAS", 0},
                        {"LIMIT", 200},
                        {"Q", 0.01},
                        {"R", 0.02}}},
                      {"左右pid",
                       {{"KP", 2.0},
                        {"KI", 0.01},
                        {"KD", 8.5},
                        {"KBIAS", 0},
                        {"LIMIT", 10},
                        {"Q", 0.01},
                        {"R", 0.02}}},
                      {"自瞄pid",
                       {{"KP", 0.55},
                        {"KI", 0.001},
                        {"KD", 0.5},
                        {"KBIAS", 0},
                        {"LIMIT", 40},
                        {"Q", 0.01},
                        {"R", 0.02}}},

                  }},
                 {"模式1",
                  {
                      {"前后pid",
                       {{"KP", 0.3},
                        {"KI", 0.005},
                        {"KD", 0.0},
                        {"KBIAS", 0},
                        {"LIMIT", 500},
                        {"Q", 0.01},
                        {"R", 0.02}}},
                      {"左右pid",
                       {{"KP", 0.79},
                        {"KI", 0.003},
                        {"KD", 0.0},
                        {"KBIAS", 0},
                        {"LIMIT", 10},
                        {"Q", 0.01},
                        {"R", 0.02}}},
                      {"自瞄pid",
                       {{"KP", 0.4},
                        {"KI", 0.001},
                        {"KD", 0.001},
                        {"KBIAS", 0},
                        {"LIMIT", 40},
                        {"Q", 0.01},
                        {"R", 0.02}}},
                  }},
             }},
        },
    },
    {
        "发射器",
        {
            {"马达",
             {
                 {"发射L", {{"端口", 5}, {"正反", true}, {"齿轮", 1}}},
                 {"发射H", {{"端口", 6}, {"正反", true}, {"齿轮", 1}}},

             }},
            {"ADI",
             {
                 {"巡线低", 2},
                 {"巡线高", 4},
             }},
            {"参数",
             {
                 {"悬停值", 0},
                 {"巡线低阈值", 2400},
                 {"巡线高阈值", 2400},
                 {"中层马达转速", 60},
             }},
        },
    },
    {
        "吸吐",
        {
            {"马达",
             {
                 {"吸吐L", {{"端口", 7}, {"正反", false}, {"齿轮", 1}}},
                 {"吸吐R", {{"端口", 8}, {"正反", true}, {"齿轮", 1}}},
             }},
            {"参数",
             {
                 {"悬停值", 0},
             }},
        },
    },

};
//递归打印
void recursionPrint(const json &pragma)
{
    switch (pragma.type())
    {
        case json::value_t::object: {
            if (pragma.empty())
            {
                return;
            }
            //第一遍：遍历此对象的元素
            for (auto &[key, val] : pragma.items())
            {
                std::cout << "\n"
                          << key << ": "; //这里可以右移
                recursionPrint(val);
            }
            break;
        }
        default:
            break;
    }
}

int main(int argc, char *argv[])
{
    recursionPrint(userData);
    return 0;
}