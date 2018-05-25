# coding=gbk
import json
import re
import urllib
from http.cookiejar import CookieJar
from urllib import request
import requests
from bs4 import BeautifulSoup


# 测试
# get md5-pwd

def ykt_message():
    username = '201508010720'
    password = 'zhong123'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept - Encoding': 'gzip, deflate, br',
        'Accept - Language': 'zh-CN,zh;q=0.9',
        'Cache - Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Content - Length': '206',
        'Content - Type': 'application/x-www-form-urlencoded',
        'Host': 'pt.hnu.edu.cn',
        'Origin': 'https://pt.hnu.edu.cn',
        'Referer': 'https://pt.hnu.edu.cn/zfca/login',
        'Upgrade - Insecure - Requests': '1',
        'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }

    # get view_state
    s = requests.session()
    s.cookies = CookieJar()
    url = "https://pt.hnu.edu.cn/zfca/login"
    response = s.get(url, headers=headers, verify=False)
    # print(response)
    html = response.content.decode('GBK')
    # print(html)
    lt = re.findall(r'<input type="hidden" name="lt" value="(.*?)" />', html, re.M | re.S)
    print('lt = ', lt)

    # 表单
    data = {
        'useValidateCode': '0',
        'isremenberme': '0',
        'ip': '',
        'username': '201508010720',
        'password': 'zhong123',
        'losetime': '30',
        'lt': lt,
        '_eventId': 'submit',
        'submit1': '登 录'
    }

    response = s.post(url, data=data, headers=headers)
    # print("response = ", response)
    print("返回页面： ", response.url)
    html = response.content
    title = re.findall(r"<.itle>(.*?)</.itle>", html.decode('GBK'), re.M | re.S)[0]
    print("title = ", title)

    # 进入一卡通查询页面，处理dwr页面，需要添加头部和表单
    # 表单这里直接使用抓取到的HTTPSessionId和scriptSessionId，如果使用其他的学号密码，需要动态抓取这两个数据。
    ykt_url = "http://pt.hnu.edu.cn/dwr/call/plaincall/yktAjax.getHisConsumeLog.dwr"  # 消费信息，存储在dwr中。
    ykt_headers = {
        'Accept': '*/*',
        'Content-Length': '340',
        'Content-Type': 'text/plain',
        # 'Cookie': 'UM_distinctid=162fdce89342e4-04f7b501d329d2-3b60450b-100200-162fdce893510b; JSESSIONID=93552B635AF1B30BF1865F5149BA4674',
        'Host': 'pt.hnu.edu.cn',
        'Origin': 'http://pt.hnu.edu.cn',
        'Referer': 'http://pt.hnu.edu.cn/portal.do?ticket=ST-193682-ndipiXrkDS1xor31q969-zfca',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    }

    ykt_data = {
        'callCount': '1',
        'page': '/portal.do?ticket=ST-193682-ndipiXrkDS1xor31q969-zfca',
        'httpSessionId': '93552B635AF1B30BF1865F5149BA4674',
        'scriptSessionId': 'B9E65D04D6E4D0B72C43EF914FD12934441',
        'c0-scriptName': 'yktAjax',
        'c0-methodName': 'getHisConsumeLog',
        'c0-id': '0',
        'c0-param0': 'string:2018-05-17',
        'c0-param1': 'string:2018-05-24',
        'c0-param2': 'string:15',
        'c0-param3': 'number:10000',
        'batchId': '6'
    }

    ykt_html = s.post(ykt_url, data=ykt_data, headers=ykt_headers)
    ykt_html = ykt_html.content.decode('unicode_escape').encode('utf-8').decode('utf-8')

    pattern = re.compile(r'FCardBalance="(.*?)".*?FTranAmt="(.*?)".*?effectdate="(.*?)".*?sysname1="(.*?)"',
                         re.M | re.S)
    ykt_msg = re.findall(pattern, ykt_html)  # 最后返回的数据

    # 进入流量查询页面
    print("\n进入流量查询界面")
    netflow_url = "http://pt.hnu.edu.cn/dwr/call/plaincall/netFlowAjax.getMonitor.dwr"
    netflow_data = {
        'callCount': '1',
        'page': '/portal.do?ticket=ST-193682-ndipiXrkDS1xor31q969-zfca',
        'httpSessionId': '93552B635AF1B30BF1865F5149BA4674',
        'scriptSessionId': 'B9E65D04D6E4D0B72C43EF914FD12934441',
        'c0-scriptName': 'netFlowAjax',
        'c0-methodName': 'getMonitor',
        'c0-id': '0',
        'batchId': '5'
    }
    netflow_headers = {
        'Host': 'pt.hnu.edu.cn',
        'Origin': 'http://pt.hnu.edu.cn',
        'Referer': 'http://pt.hnu.edu.cn/portal.do?ticket=ST-193682-ndipiXrkDS1xor31q969-zfca',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    }
    netflow_html = s.post(url=netflow_url, data=netflow_data, headers=netflow_headers)
    netflow_html = netflow_html.content.decode('gbk')
    # print("流量使用信息：", netflow_html)
    netflow_msg = re.findall(r'{currentnetflow:(.*?),prenetflow:(.*?),', netflow_html)

    return ykt_msg
    # 进入教务系统

    # hdjw_url = "https://pt.hnu.edu.cn/zfca?yhlx=student&login=0122579031373493685&url=login.aspx"
    #
    # hdjw_html = s.get(url=hdjw_url, headers=headers )
    #
    # print("response: ",hdjw_html.url )
    #
    # title = re.findall(r'<.itle>.*?<.itle>', hdjw_html.content.decode('GBK'), re.M|re.S)
    # print("title:", title)

    # f = open('打印网页.html', 'w')
    # f.write(hdjw_html.content.decode('GBK'))
    # f.close()


if __name__ == '__main__':
    ykt_msg, netflow_msg = ykt_message()

    print("处理后的数据")
    for i in ykt_msg:
        print("消费信息：", i)

    ykt_yue = ykt_msg[0][0]
    print("一卡通余额为：", ykt_yue)

    print("处理后的流量数据：", netflow_msg)
    print("当月已使用流量：", netflow_msg[0][0], "上月使用の流量：", netflow_msg[0][1])
