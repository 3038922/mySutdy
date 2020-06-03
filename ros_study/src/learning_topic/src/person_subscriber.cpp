//订阅者实现
#include "learning_topic/Person.h"
#include <ros/ros.h>
//接受到订阅消息后，会进入消息回调函数
void poseCallback(const learning_topic::Person::ConstPtr &msg)
{
    //将接受到的消息打印出来
    ROS_INFO("Subcribe Person Info: name%s age%d sex:%d", msg->name.c_str(), msg->age, msg->sex);
}
int main(int argc, char **argv)
{
    //初始化ROS节点
    ros::init(argc, argv, "person_subscriber");
    //创建节点句柄
    ros::NodeHandle n;
    //创建一个subscriber ,订阅名为/turtle1/pose的topic ,注册回调函数poseCallback
    ros::Subscriber person_info_sub = n.subscribe("/person_info", 10, poseCallback);
    //循环等下回调函数
    ros::spin();
    return 0;
}