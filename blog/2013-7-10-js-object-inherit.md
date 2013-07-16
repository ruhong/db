---
title: Recommands three kinds of inheritance way for js
---


### 1. 原型继承

> 原型继承是让父对象作为子对象的原型，从而达到继承的目的：

```{.javascript}
function object(o) {
    function F() {

    }
    F.prototype = o;
    return new F();
}

//要继承的父对象
var Parent = {
    name: 'Papa'
}

//子对象
var child = object(Parent)

//test
console.log(child.name); //Papa

//父构造函数
function Person() {
    this.name = "Adam";
}

Person.prototype.getName = function() {
    return this.name;
}

var papa = new Person();
var kid = object(papa);

console.log(kid.getName()); //"Adam"


//父构造函数
function Person() {
    this.name = "Adam";
}

Person.prototype.getName = function() {
    return this.name;
}

//只继承到原型
var kid = object(Person.prototype);
console.log(typeof kid.getName); // "function",因为是在原型里定义的
console.log(typeof kid.name); // "undefined", 因为只继承了原型
```

### 2. 复制所有属性进行继承

> 这种方式的继承就是将父对象里所有的属性都复制到子对象上，一般子对象可以使用父对象的数据。

```{.javascript}
//浅拷贝
//代码的最后一行，你可以发现dad和kid的reads是一样的，也就是他们使用的是同一个引用，这也就是浅拷贝带来的问题。

function extend(parent, child) {
    var i;
    child = child || {};
    for(i in parent) {
        if(parent.hasOwnProperty(i)) {
            child[i] = parent(i);
        }
    }

    return child;
}

var dad = {
    counts: [1, 2, 3],
    reads: {paper: true}
};

var kid = extend(dad);
kid.counts.push(4);

console.log(dad.counts.toString()); //"1,2,3,4"
console.log(dad.reads === kid.reads); //true

//深拷贝

function extendDeep(parent, child) {
    var i,
        toStr = Object.prototype.toString,
        astr = "[object Array]";

    child = child || {};

    for(i in parent) {
        if(parent.hasOwnProperty(i)) {
            if(typeof parent[i] === 'object') {
                child[i] = (toStr.call(parent[i])===astr) ? [] : {}; 
                extendDeep(parent[i], child[i]);
            }else{
                child[i] = parent[i];
            }
        }
    }

    return child;
}

var dad = {
    counts: [1, 2, 3],
    reads: {paper: true}
}

var kid = extendDeep(dad);
kid.counts.push(4);

console.log(kid.counts.toString()); //"1,2,3,4"
console.log(dad.counts.toString()); //"1,2,3"

console.log(dad.reads === kid.reads); //false
```

### 3. 混合（mix-in）

> 混入就是将一个对象的一个或多个（或全部）属性（或方法）复制到另外一个对象，我们举一个例子：

```{.javascript}
function mix() {
    var arg, 
        prop, 
        child = {};

    for(arg = 0, arg<arguments.length; arg +=1) {
        for(prop in arguments[arg]) {
            if(arguments[arg].hasOwnProperty(prop)) {
                child[prop] = arguments[arg][prop];
            }
        }
    }

    return child;

}
```