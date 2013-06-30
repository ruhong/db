---
title: css-rules
---


### 1. 变量

> 声明变量必须加上var

### 2. 常量

> 使用大写字符,并用下划线分隔：NAMES_LIKE_THIS

### 3. 分号

> 总是使用分号

### 4. this

> 仅在对象构造器,  方法,  闭包中使用。

### 5. for in循环

> 只用于object/map/hash 的遍历

> 对Array用for-in循环有时会出错。因为它并不是从0到length-1 进行遍历,
> 而是所有出现在对象及其原型链的键值。下面就是一些失败的使用案例:

```{.js}
function printArray(arr) {
    for (var key in arr) {
        print(arr[key]);
    }
}
printArray([0,1,2,3]);   // This works. var a = new Array(10);
printArray(a);   // This is wrong.

a = document.getElementsByTagName('*');
printArray(a);   // This is wrong.

a = [0,1,2,3];
a.buhu = 'wine';
printArray(a);   // This is wrong again.

a = new Array;
a[3] = 3;
printArray(a);   // This is wrong again.

//而遍历数组通常用最普通的  for  循环.

function printArray(arr) {
    for (var i = 0, len=arr.length; i < len; i++) {
        print(arr[i]);
    }
}
```
### 6. 命名规则

    1) 变量 variableNamesLikeThis
    2) 常量 SYMBOLIC_CONSTANTS_LIKE_THIS
    3) 函数 functionNamesLikeThis
    4) 构造函数 ClassNamesLikeThis
    5) 方法名 methodNamesLikeThis
    6) 私有属性、变量和方法名应该以下划线"_"开头

    7) 可选参数以"opt_"开头
    8) getters和setters并不是必要的。但只要使用它们了,就请将getters命名成getFoo()形式,将setters命名成setFoo(value) 形式.


### 7. 命名空间

> 在全局作用域上,使用一个唯一的,与工程/库相关的名字作为前缀标识。比如,你的工程是"Project  Sloth",那么命名空间前缀可取为sloth.*

```{.js}
var sloth = {};
sloth.sleep = function() {

};
```

### 8. 文件名
> 文件名应该使用小写字符,以避免在有些系统平台上不识别大小写的命名方式.文件名以.js结尾,不要包含除 - 和 _ 外的标点符号(使用 - 优于
_)。

### 9. 


