<?php
    header('content-type:text/html;charset="utf-8"');
    //定义下状态码
    $responseData=array("code"=>0,"message"=>"");
    //取数据
    $id=$_POST['id'];
    if(!$id)
    {
        $responseData['code']=4;
        $responseData['message']="id传入后台失败";
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
    $sql= "select * from users where id={$id}";
    //6 发送数据库
    $result=mysqli_query($study,$sql);
    //解析数据 千万别漏了
    $row=mysqli_fetch_assoc($result);
    if(!$row) {
        $responseData['code']=2;
        $responseData['message']="id不存在";
        echo json_encode($responseData); 
        mysqli_free_result($result);
        mysqli_close($study);
        exit;
    }
    else{
        $responseData['code']=3;
        $responseData['message']=json_encode($row);//拼接上去
        echo json_encode($responseData); 
    }

    //8 释放结果集
    mysqli_free_result($result);
    mysqli_close($study);
?>