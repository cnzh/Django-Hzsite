# Django博客系统

一直想用Python实现一个博客系统来替换掉现在臃肿的WordPress。之前尝试过使用Flask框架来实现，但是由于功力不足，Flask这种小型框架做起来还是困难比较大的，所以决定还是从Django入手吧。在这之后应该会有一系列的文章来完成一个这个博客系统的实现，虽然离WordPress应该差距不小，但是至少应该能够实现一个博客系统需要的基本功能。

## 目录

* [Django博客系统开发01 – 环境搭建、创建项目](https://www.zivers.com/post/1308.html)
* [Django博客系统开发02 – 模型Model](https://www.zivers.com/post/1318.html)
* [Django博客系统开发03 – 路由Django URL](https://www.zivers.com/post/1331.html)
* [Django博客系统开发04 – 前端改造](https://www.zivers.com/post/1337.html)
* [Django博客系统开发05 – 文章的增删改发布](https://www.zivers.com/post/1346.html)
* [Django博客系统开发06 – 用户登录](https://www.zivers.com/post/1356.html)
* ...

## 目标

实现一个基于Django框架的简单博客，第一阶段应该至少实现以下功能：

1. 增加、修改、删除文章
2. 用户登录、登出
3. 草稿系统，草稿发布逻辑
4. 基本的前端界面

之后会对这些功能迭代，Todo：

1. 页面导航
2. 文章搜索
3. Redis缓存
4. MarkDown集成
5. 富文本编辑
6. …

## 环境

* Ubuntu 16.04 LTS
* Django 1.10
* MySQL 5.7
* Python 3.5

## 参考

代码结构很大程度上参考了[Django Girls](https://github.com/DjangoGirls)的[tutorial](https://github.com/DjangoGirls/tutorial)以及[tutorial-extensions](https://github.com/DjangoGirls/tutorial-extensions)系列教程，这里进行说明。
