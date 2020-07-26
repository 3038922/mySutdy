<?php
header('content-type:text/html;charset="utf-8"');
error_reporting(0);
// 关联数组
$arr2=array('username'=>'小屁屁',
            'age'=>12,
            'sex'=>'男');
echo json_encode($arr2);
