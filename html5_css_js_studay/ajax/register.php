<?php
    header('content-type:text/html;charset="utf-8"');
    //定义下状态码
    $responseData=array("code"=>0,"message"=>"");
    //取数据
    $username=$_POST['username'];
    $password=$_POST['password'];
    $addTime=$_POST['addTime'];


    /**
     * 1 连接数据库 7.x版本
     * 第一个参数 IP 
     * 第二个参数 用户名
     * 第三个参数  密码
     */
    $study=mysqli_connect("localhost","study","protoss"); 
    //2 判断数据库是否连接成功
    if (mysqli_connect_errno($study)) 
    { 
        $responseData['code']=1;
        $responseData['message']="数据库链接失败";
        echo json_encode($responseData); 
        exit;
    } 
    //3 修改数据库连接字符集为 utf8
    mysqli_set_charset($study,"utf8");
    //4 选择数据库
    mysqli_select_db($study,"study");
    //5  准备SQL语句
    //注意 name 是字符串
    $sql= "insert into users(username,password,create_time) values('{$username}','{$password}',{$addTime})";
    //6 发送sql语句
    $result=mysqli_query($study,$sql);
    //7 处理结果 全部显示
    if(!$result){
        $responseData['code']=2;
        $responseData['message']="注册失败";
        echo json_encode($responseData); 
        exit;
    }
    else{
        $responseData['message']="注册成功";
        echo json_encode($responseData); 
    }
    //8 释放结果集
    mysqli_free_result($result);
    mysqli_close($study);
?>