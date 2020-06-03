//发布者实现
#include <geometry_msgs/Twist.h>
#include <ros/ros.h>
int main(int argc, char **argv)
{
    ros::init(argc, argv, "velocity_publisher"); //初始化节点名字
    ros::NodeHandle n;                           //创建一个节点 管理API节点资源
    //创建一个publisher
    ros::Publisher turtle_vel_pub = n.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 10);
    ros::Rate loop_rate(10);
    int count = 0;
    while (ros::ok())
    {
        geometry_msgs::Twist vel_msg;
        vel_msg.linear.x = 0.5;
        vel_msg.angular.z = 0.2;
        turtle_vel_pub.publish(vel_msg);
        ROS_INFO("publsh turtle velocity command[%0.2f m/s,%0.2f rad/s]", vel_msg.linear.x, vel_msg.angular.z);
        loop_rate.sleep();
    }
    return 0;
}