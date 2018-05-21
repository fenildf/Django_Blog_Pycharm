﻿# 个人博客搭建

## GitHub的使用

1. 下载GitHub桌面版

1.1  创建新的仓库，选择本地路径
创建成功之后，就可以进入本地目录，进行文件的编辑。

1.2  上传到GitHub
 
2. 下载git

2.1 创建ssh key

使用自己注册GitHub时用的邮箱

$ ssh-keygen -t rsa -C "your_email@youremail.com"

## 测试GitHub桌面版

增加几句话，GitHub中出现了修改的记录，把修改提交并上传。查看GitHub网页中的代码是否得到更新。

## 测试Pycharm更新GitHub代码

选择tools -> git 可以看到熟悉Git操作，但我push，虽然现实push成功了，但GitHub中却完全没有更新。
照理来说应该先commit再fetch，但不好意思，是先commit再push就更新成功了。

## 克隆
可不可以不克隆整个项目，只克隆修改过的文件？比如说pull拉怎么用？
据我了解可能需要在服务器上搭建一个git服务器。有点麻烦。


