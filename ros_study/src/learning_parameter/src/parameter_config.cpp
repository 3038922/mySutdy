//设置读取海龟范例中的参数
#include <ros/ros.h>
#include <std_srvs/Empty.h>
#include <string>
int main(int argc, char **argv)
{
    int red, green, blue;
    ros::init(argc, argv, "parameter_config");
    ros::NodeHandle node;
    //读取背景颜色
    ros::param::get("/background_r", red);
    ros::param::get("/background_g", green);
    ros::param::get("/background_b", blue);
    ROS_INFO("Get Background color[%d, %d, %d]", red, green, blue);
    //设置背景颜色参数
    ros::param::set("/background_r", 255);
    ros::param::set("/background_g", 255);
    ros::param::set("/background_b", 255);
    ros::param::get("/background_r", red);
    ros::param::get("/background_g", green);
    ros::param::get("/background_b", blue);
    ROS_INFO("Set Background color[%d, %d, %d]", red, green, blue);

    //调用服务，刷新背影色
    ros::service::waitForService("/clear");
    ros::ServiceClient clear_background = node.serviceClient<std_srvs::Empty>("/clear");
    std_srvs::Empty srv;
    clear_background.call(srv);
    sleep(1);
    return 0;
}