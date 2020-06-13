//客户端
#include "learning_service/Person.h"
#include <ros/ros.h>
int main(int argc, char **argv)
{
    ros::init(argc, argv, "turtle_spawn"); //初始化
    ros::NodeHandle node;                  //创建节点句柄
        //发现/spwan服务后，创建一个服务客户端，连接名为 /spawn 的service
    ros::service::waitForService("/show_person"); //如果没找到/spwan服务 就一直等待
    ros::ServiceClient add_turtle = node.serviceClient<learning_service::Person>("/show_person");

    //初始化turtlesim::Spwan的请求数据
    learning_service::Person srv;
    srv.request.name = "陈昱安";
    srv.request.age = 35;
    srv.request.sex = learning_service::Person::Request::male;
    //请求服务调用
    ROS_INFO("Call service to person turtle[name:%s, age:%d, sex:%d]", srv.request.name.c_str(), srv.request.age, srv.request.sex);
    add_turtle.call(srv); //访问成功后才会执行下一句
    //显示服务调用结果
    ROS_INFO("Show person result :%s", srv.response.result.c_str());
    return 0;
}