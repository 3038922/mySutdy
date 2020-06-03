#include <geometry_msgs/Twist.h>
#include <ros/ros.h>
#include <std_srvs/Trigger.h>
ros::Publisher turtle_vel_pub;
bool pubCommand = false;
//service 回调函数 输入参数req,输出参数res
bool commandCallback(std_srvs::Trigger::Request &req, std_srvs::Trigger::Response &res)
{
    pubCommand = !pubCommand;
    //显示数据请求
    ROS_INFO("Publish turtle velocity command [%s]", pubCommand == true ? "Yes" : "No");
    //设置反馈数据
    res.success = true;
    res.message = "Change turtle command state!";
    return true;
}
int main(int argc, char **argv)
{
    ros::init(argc, argv, "turtle_command_server");
    ros::NodeHandle n;
    //创建一个server 注册回调函数
    ros::ServiceServer command_service = n.advertiseService("/turtle_command", commandCallback);
    //创建一个publisher 发布topic
    turtle_vel_pub = n.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 10);
    //循环等下回调函数
    ROS_INFO("Ready to receive turtle command.");
    //设置循环频率
    ros::Rate loop_rate(10);
    while (ros::ok())
    {
        //查看一次回调函数队列
        ros::spinOnce();
        //如果标志为true 则发布速度指令
        if (pubCommand)
        {
            geometry_msgs::Twist vel_msg;
            vel_msg.linear.x = 0.5;
            vel_msg.angular.z = 0.2;
            turtle_vel_pub.publish(vel_msg);
        }
        loop_rate.sleep();
    }
    return 0;
}