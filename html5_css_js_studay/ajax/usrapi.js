function show(arr) {
    for (const it1 of arr) {
        if (it1 instanceof Array) {
            for (const it2 of it1) //这里其实用递归更好 懒得烦了.
                document.write(it2 + " ");
            document.write("<br/>");
        }
        else
            document.write(it1 + " ");
    }
}
function bubbleSort(arr) {
    for (var i = 0; i < arr.length - 1; i++)
        for (var j = 0; j < arr.length - (i + 1); j++)
            if (arr[j] < arr[j + 1]) {
                var temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
}

function verificationCode(n) {
    var arr = [];

    for (var i = 0; i < n; i++) {
        var num = parseInt(Math.random() * 123);
        if (num >= 0 && num <= 9)
            arr.push(num);
        else if (num >= 97 && num <= 122 || num >= 65 && num <= 90)
            arr.push(String.fromCharCode(num));
        else
            i--;
    }
    return arr.join("");//拼接
}
function countDate(var1, var2) {
    d1 = new Date(var1);
    d2 = new Date(var2);
    return parseInt(Math.abs(d1.getTime() - d2.getTime()) / 1000 / 3600 / 24);
}
function doubleNum(n) {
    if (n < 10)
        return "0" + n;
    else {
        return n;
    }

}
function $(id) { return document.getElementById(id); }

function randomColor() {
    var str = "rgba(" + parseInt(Math.random() * 256) + "," + parseInt(Math.random() * 256) + "," + parseInt(Math.random() * 256) + "," + "1)"
    return str;
}
function querystring(obj) {
    var str = "";
    for (var i in obj)
        str += i + "=" + obj[i] + "&";
    return str.substring(0, str.length - 1);
}
function $ajax({ method = "get", url, data }) {
    var xhr = null;
    try {
        xhr = new XMLHttpRequest();
    }
    catch (error) {
        xhr = new ActiveXObject("Microsoft.XMLHTTP");
    }
    if (data)
        data = querystring(data);
    if (method == "get" && data)
        url += "?" + data;
    xhr.open(method, url, true);
    if (method == "get")
        xhr.send();
    else {
        xhr.setRequestHeader("content-type", "application/x-www-form-urlencoded")
        xhr.send(data);
    }
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4)
            if (xhr.status == 200)
                alert(xhr.responseText);
            else
                alert(xhr.status);
    }

}