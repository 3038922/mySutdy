<?php
    header('content-type:text/html;charset="utf-8"');
    //定义下状态码
    $responseData=array("code"=>0,"message"=>"");
    //取数据
    $username=$_POST['username'];
    $password=$_POST['password'];
    $addTime=$_POST['addTime'];

    if(!$username){
        $responseData['code']=3;
        $responseData['message']="用户名不能为空";
        echo json_encode($responseData); 
        exit;
    }
    if(!$password){
        $responseData['code']=4;
        $responseData['message']="密码不能为空";
        echo json_encode($responseData); 
        exit;
    }
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
    //验证用户是否重名
    $sql1= "select * from users where username='{$username}'";
    $result1=mysqli_query($study,$sql1);
    $row=mysqli_fetch_assoc($result1);
    if($row){
        $responseData['code']=5;
        $responseData['message']="用户名已存在";
        echo json_encode($responseData); 
        mysqli_free_result($result);
        mysqli_close($study);
        exit;
    }
    //ADD 注意密码进行MD5加密
    $pwMd5=md5(md5(md5($password)."xxx")."yyy");
    $sql= "insert into users(username,password,create_time) values('{$username}','{$pwMd5}',{$addTime})";
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