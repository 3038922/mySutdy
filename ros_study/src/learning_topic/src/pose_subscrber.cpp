//订阅者实现
#include "turtlesim/Pose.h"
#include <ros/ros.h>
//接受到订阅消息后，会进入消息回调函数
void poseCallback(const turtlesim::Pose::ConstPtr &msg)
{
    //将接受到的消息打印出来
    ROS_INFO("Turtle pose: x:%0.6f, y:%0.6f", msg->x, msg->y);
}
int main(int argc, char **argv)
{
    //初始化ROS节点
    ros::init(argc, argv, "pose_subscriber");
    //创建节点句柄
    ros::NodeHandle n;
    //创建一个subscriber ,订阅名为/turtle1/pose的topic ,注册回调函数poseCallback
    ros::Subscriber pose_sub = n.subscribe("/turtle1/pose", 10, poseCallback);
    //循环等下回调函数
    ros::spin();
    return 0;
}