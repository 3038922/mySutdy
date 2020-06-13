<?php
header('content-type:text/html;charset="utf-8"');
$username=$_GET['username'];
$age=$_GET['age'];
$pw=$_GET['pw'];
echo "你的名字:{$username},年龄:{$age},密码:{$pw}";
?>