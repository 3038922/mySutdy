//person发布者实现
#include "learning_topic/Person.h"
#include <ros/ros.h>
int main(int argc, char **argv)
{
    ros::init(argc, argv, "person_publisher"); //初始化节点名字
    ros::NodeHandle n;                         //创建一个节点 管理API节点资源
    //创建一个publisher
    ros::Publisher person_info_pub = n.advertise<learning_topic::Person>("/person_info", 10);
    ros::Rate loop_rate(1);
    int count = 0;
    while (ros::ok())
    {
        //初始化类型消息
        learning_topic::Person person_msg;
        person_msg.name = "Ares";
        person_msg.age = 36;
        person_msg.sex = learning_topic::Person::male;
        //发布消息
        person_info_pub.publish(person_msg);
        //cmd 输出
        ROS_INFO("Publish Person Info: name%s age%d sex:%d", person_msg.name.c_str(), person_msg.age, person_msg.sex);
        loop_rate.sleep();
    }
    return 0;
}