# -*-conding: UTF-8-*-
from urllib import request  # 导入urllib库中的request模块
import re

def news():
    url = 'http://www.hnu.edu.cn/'  # 要闻的链接
    # print("url = {0}".format(url))

    with request.urlopen(url) as f:
        # print('Status:', f.status, f.reason)
        # for k, v in f.getheaders():
        #     print('%s:%s' % (k, v))
        dataAll = f.read()  # 使用read()方法读取数据，否则返回的是一个请求对象的描述

        # print(dataAll)  # 打印结果

        data_ul = re.findall(
            '<li><a href="(.*?)" title="(.*?)" target="_blank"><div class="div">.*?</div></a><span>(.*?)</span></li>',
            dataAll.decode('utf-8'),
            re.M | re.S)

    return data_ul



