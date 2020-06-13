<?php
    header('content-type:text/html;charset="utf-8"');
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
        echo "连接 MySQL 失败: " . mysqli_connect_error(); 
        exit;
    } 
    //3 修改数据库连接字符集为 utf8
    mysqli_set_charset($study,"utf8");
    //4 选择数据库
    mysqli_select_db($study,"study");
    //5  准备SQL语句
    $sql= "select * from students";
    //6 发送sql语句
    $result=mysqli_query($study,$sql);
    //设置表头
    echo "<table border= '1'>";
    echo "<tr><th>学号</th><th>姓名</th><th>英语</th><th>数学</th><th>语文</th></tr>";
    //7 处理结果 全部显示
    while ($row=mysqli_fetch_assoc($result))
       echo "<tr><th>{$row['id']}</th><th>{$row['name']}</th><th>{$row['english']}</th><th>{$row['math']}</th><th>{$row['chinese']}</th></tr>";
    echo "</table>";
    //8 释放结果集
    mysqli_free_result($result);
    mysqli_close($study);
?>