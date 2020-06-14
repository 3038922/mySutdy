<?php
    header('content-type:text/html;charset="utf-8"');
    //定义下状态码
    $responseData=array("code"=>0,"message"=>"");
    $id =$_POST['id'];

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
    $sql1= "delete from users where id={$id}";
    //6 发送
    $result1=mysqli_query($study,$sql1);
    if(!$result1) {
        $responseData['code']=2;
        $responseData['message']="删除失败";
        echo json_encode($responseData); 
        mysqli_free_result($result);
        mysqli_close($study);
        exit;
    }
    else{
        $responseData['code']=3;
        $responseData['message']="删除成功";
        echo json_encode($responseData); 
    }
    //8 释放结果集
    mysqli_free_result($result);
    mysqli_close($study);
?>