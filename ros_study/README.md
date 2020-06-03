# ROS_STUDAY
## 初始化
1. ` cd src`
2. 初始化  `catkin_init_workspace`
3. 空编译 `cd ..` `catkin_make`
4. (可选) 产生install 文件夹  `catkin_make install`

## 创建功能包
1.  `cd src`
2. `catkin_create_pkg learning_topic std_msgs rospy roscpp geometry_msgs turtlesim`

## 编译功能包
1. `cd ~/catkin_ws`
2. `catkin_make`  
3. 加载环境变量  bash:`source  ~/catkin_ws/devel/setup.bash` zsh: `source  ~/catkin_ws/devel/setup.zsh` 
4. 为了避免每次都要设置环境变量可以 `source /home/ares/catkin_ws/devel/setup.zsh`
5. (可选) 测试工作空间环境变量 `echo $ROS_PACKAGE_PATH`