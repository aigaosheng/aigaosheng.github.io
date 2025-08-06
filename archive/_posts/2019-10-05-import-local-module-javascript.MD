---
layout:     post
title:      How to export and import local modules in Javascript 
date:       2019-10-05
author:     BY GS
published: true 
header-img: image/rawa-sun-falling.jpg
catalog: true
categories: [javascript, import, export, module] 
tags: [computer program, javascript, nvm, node.js]
---

<h3> Export and import local modules in Javascript </h3>
A lot of examples teach you how to import modules in html. But how do you import own-coded modules in JS file? Here is a simple example showing you how to do. More info refer to
<a href= "https://www.tutorialsteacher.com/nodejs/nodejs-local-modules">JS local modules</a>. 
Main module <em>test.js</em> imports functions from demo_module.js, which is in the same folder as test.js
{% highlight javascript %}
var mymodule = require('./demo_module.js');
console.log(mymodule.square(11));
console.log(mymodule.diag(4, 3));
{% endhighlight %}
<p>In <em>demo_module.js</em>, export your modules </p>
{% highlight javascript %}
var sqrt = Math.sqrt;
function square(x) {
    return x*x;
}
function diag(x, y) {
    let v = Math.sqrt(square(x) + square(y));
    return v;
};
module.exports.diag = diag;
module.exports.square = square;
{% endhighlight %}

