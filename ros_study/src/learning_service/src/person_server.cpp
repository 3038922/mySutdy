//服务端
#include "learning_service/Person.h"
#include <ros/ros.h>

//service 回调函数 输入参数req,输出参数res
bool personCallback(learning_service::Person::Request &req, learning_service::Person::Response &res)
{
    //显示数据请求
    ROS_INFO("Person [name:%s, age:%d, sex:%d]", req.name.c_str(), req.age, req.sex);
    //设置反馈数据
    res.result = "OK";
    return true;
}
int main(int argc, char **argv)
{
    ros::init(argc, argv, "person_server");
    ros::NodeHandle n;
    //创建一个server 注册回调函数
    ros::ServiceServer command_service = n.advertiseService("/show_person", personCallback);
    //循环等下回调函数
    ROS_INFO("Ready to show person informtion.");
    ros::spin();
    return 0;
}