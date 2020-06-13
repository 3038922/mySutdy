//客户端
#include <ros/ros.h>
#include <turtlesim/Spawn.h>
int main(int argc, char **argv)
{
    ros::init(argc, argv, "turtle_spawn"); //初始化
    ros::NodeHandle node;                  //创建节点句柄
        //发现/spwan服务后，创建一个服务客户端，连接名为 /spawn 的service
    ros::service::waitForService("/spwan"); //如果没找到/spwan服务 就一直等待
    ros::ServiceClient add_turtle = node.serviceClient<turtlesim::Spawn>("/spawn");

    //初始化turtlesim::Spwan的请求数据
    turtlesim::Spawn srv;
    srv.request.x = 2.0;
    srv.request.y = 2.0;
    srv.request.name = "turtle2";
    //请求服务调用
    ROS_INFO("Call service to spwan turtle[x:%0.6f, y:%0.6f, name:%s]", srv.request.x, srv.request.y, srv.request.name.c_str());
    add_turtle.call(srv); //访问成功后才会执行下一句
    //显示服务调用结果
    ROS_INFO("Spwan turtle successfully[name:%s]", srv.response.name.c_str());
    return 0;
}