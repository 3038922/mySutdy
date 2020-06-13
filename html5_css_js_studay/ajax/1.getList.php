<?php
header('content-type:text/html;charset="utf-8"');
error_reporting(0);
//普通数组
$arr1=array('leo','momo','zhangsan');
echo json_encode($arr1);
?>