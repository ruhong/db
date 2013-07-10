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
> 不要对命名空间创建别名

```

### 8. 文件名
> 文件名应该使用小写字符,以避免在有些系统平台上不识别大小写的命名方式.文件名以.js结尾,不要包含除 - 和 _ 外的标点符号(使用 - 优于
_)。

### 9. 代码格式

> 大括号
> 分号会被隐式插入到代码中,  所以你务必在同一行上插入大括号

```{.js}
if (something) {
    // ...
} else {
    /
}
```

### 10. 数组和对象的初始化

> 如果初始值不是很长,  就保持写在单行

```{.js}
var arr = [1, 2, 3];   // No space after [ or before ].
var obj = {a: 1, b: 2, c: 3};   // No space after { or before }.
```
> 初始值占用多行时,  缩进4个空格

```{.js}
// Object initializer.
var inset = { 
    top: 10, 
    right: 20, 
    bottom: 15, 
    left: 12
};

// Array initializer.
this.rows_ = [
    '"Slartibartfast" <fjordmaster@magrathea.com>',
    '"Zaphod Beeblebrox" <theprez@universe.gov>',
    '"Ford Prefect" <ford@theguide.com>',
    '"Arthur Dent" <has.no.tea@gmail.com>',
    '"Marvin the Paranoid Android" <marv@googlemail.com>',
    'the.mice@magrathea.com'
];

// Used in a method call.
goog.dom.createDom(goog.dom.TagName.DIV, {
    id: 'foo',
    className: 'some-css-class', 
    style: 'display:none'
}, 'Hello, world!');

```
> 比较长的标识符或者数值,  不要为了让代码好看些而手工对齐。

```{.js}
CORRECT_Object.prototype = {
    a: 0, 
    b: 1,
    lengthyName: 2
};

//不要这样做:
WRONG_Object.prototype = {
    a          : 0, 
    b          : 1, 
    lengthyName: 2
};

```

### 11. 函数参数

> 尽量让函数参数在同一行上.  如果一行超过  80  字符,每个参数独占一行,  并以4个空格缩进,  或者与括号对齐,  以提高可读性.  尽可能不要让每行超过
80个字符.  比如下面这样:

```{.js}
// Four-space, wrap at 80.   Works with very long function names, survives
// renaming without reindenting, low on space. goog.foo.bar.
doThingThatIsVeryDifficultToExplain = function(
    veryDescriptiveArgumentNumberOne, veryDescriptiveArgumentTwo, 
    tableModelEventHandlerProxy, artichokeDescriptorAdapterIterator) {
    // ...
};

// Four-space, one argument per line.   Works with long function names,
// survives renaming, and emphasizes each argument. goog.foo.bar.
doThingThatIsVeryDifficultToExplain = function(
    veryDescriptiveArgumentNumberOne, 
    veryDescriptiveArgumentTwo, 
    tableModelEventHandlerProxy, 
    artichokeDescriptorAdapterIterator) {
    // ...
};

// Parenthesis-aligned indentation, wrap at 80.   Visually groups arguments,
// low on space.
function foo(veryDescriptiveArgumentNumberOne, veryDescriptiveArgumentTwo, 
tableModelEventHandlerProxy, artichokeDescriptorAdapterIterator) {
    // ...
};

// Parenthesis-aligned, one argument per line.   Visually groups and
// emphasizes each individual argument. 
function bar(
    veryDescriptiveArgumentNumberOne,
    veryDescriptiveArgumentTwo, 
    tableModelEventHandlerProxy, 
    artichokeDescriptorAdapterIterator) {
    //...
}
```

### 12. 传递匿名函数

> 如果参数中有匿名函数,  函数体从调用该函数的左边开始缩进4个空格,  
而不是从  function  这个关键字开始.  这让匿名函数更加易读  (不要增加很多没 
必要的缩进让函数体显示在屏幕的右侧)

```{.js}
//Not recommand
var names = items.map(function(item) {
                        return item.name;
                    });

//Recommand
prefix.something.reallyLongFunctionName('whatever', function(a1, a2) {
    if (a1.equals(a2)) {
        someOtherLongFunctionName(a1);
    } else {
        andNowForSomethingCompletelyDifferent(a2.parrot);
    }
});

```

### 13. 更多的缩进

> 事实上,除了初始化数组和对象 ,和传递匿名函数外,
所有被拆开的多行文本与之前的表达式左对齐,以4个
空格作为一缩进层次

```{.js}
someWonderfulHtml = ' +
    getEvenMoreHtml(
        someReallyInterestingValues, 
        moreValues, 
        evenMoreParams, 
        'a duck', 
        true, 
        72, 
        slightlyMoreMonkeys(0xfff)) +
    ';

thisIsAVeryLongVariableName =
    hereIsAnEvenLongerOtherFunctionNameThatWillNotFitOnPrevLine();

thisIsAVeryLongVariableName = 'expressionPartOne' + someMethodThatIsLong() +
    thisIsAnEvenLongerOtherFunctionNameThatCannotBeIndentedMore();

someValue = this.foo(
    shortArg,
    'Some really long string arg - this is a pretty common case, actually.',
    shorty2,
    this.bar());

if (searchableCollection(allYourStuff).contains(theStuffYouWant) &&
    !ambientNotification.isActive() && 
    (client.isAmbientSupported() || client.alwaysTryAmbientAnyways()) {
    ambientNotification.activate();
}

```

### 14. 空行

> 使用空行来划分一组逻辑上相关联的代码片段

```{.js}
doSomethingTo(x);
doSomethingElseTo(x);
andThen(x);

nowDoSomethingWith(y);

andNowWith(z);
```

### 15. 二元和三元操作符

> 操作符始终跟随着前行,这样就不用顾虑分号的隐式插入问题。
如果一行实在放不下,  还是按照上述的缩进风格来换行。

```{.js}
var x = a ? b : c;   // All on one line if it will fit.

// Indentation +4 is OK.
var y = a ?
    longButSimpleOperandB : longButSimpleOperandC;

```

### 15. 字符串

> 使用单引号 ' 优于双引号 "

```{.js}
var msg = 'This is some HTML';
```