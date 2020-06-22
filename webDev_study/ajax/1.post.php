<?php
header('content-type:text/html;charset="utf-8"');
$username=$_POST['username'];
$age=$_POST['age'];
$pw=$_POST['pw'];
echo "你的名字:{$username},年龄:{$age},密码:{$pw}";
