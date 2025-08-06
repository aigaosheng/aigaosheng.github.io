---
layout:     post
title:      How to setup javascript dvelopment environment in Ubuntu 
date:       2019-09-30
author:     BY GS
published: true 
header-img: image/rawa-sun-falling.jpg
catalog: true
categories: [javascript, node.js] 
tags: [computer program, javascript, nvm, node.js]
---

<h3> Setup javascript development environment </h3>
<ol>
<li> <a href= "https://github.com/nvm-sh/nvm">install node.js version manager (NVM) </a>. Followig the instruction and run command 
{% highlight console %}
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash 
{% endhighlight %}
Then run shell
{% highlight console %}
source ~/.bashrc 
{% endhighlight %}
</li>
<li> run 
{% highlight console %} 
nvm install 10.16.3 
{% endhighlight %} 
to install node.js you need. Here I install latest version.</li>
<li> Restart visual studio code. It it OK to use node.js for debug.</li>
</ol>
