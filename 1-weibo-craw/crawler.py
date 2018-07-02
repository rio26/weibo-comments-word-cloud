# -*- coding: utf-8 -*-
"""
Created on FRI Jun 19 2018

@author: Rio Kunn
"""

import requests
import json
import time
import csv
import os
import codecs
import sys
import random
import re
reload(sys)
sys.setdefaultencoding('utf8')

page_f = 1;
page_l = 200;

headers = {
    # "Cookies":'在这里输入你的个人cookie',
    "Cookies":'PUT YOUR OWN COOKIE HERE',
    "User-Agent":'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
}
# id可以换成任意新浪微博的微博id号，具体可以打开相应微博查看，这个评论通过微博开放的api获取，不是微博地址
# https://m.weibo.cn/api/comments/show?id=xxxxxxxxxxxxxxxxxxx&page={}.

url_comment = ['https://m.weibo.cn/api/comments/show?id=xxxxxxxxxxxxxxxxxxxxxxxx&page={}'.format(str(i)) for i in range(page_f,page_l)]
#print(url_comment)
path = os.getcwd()+"/weibo.csv"
csvfile = open(path, 'w')
csvfile.write(codecs.BOM_UTF8)
writer = csv.writer(csvfile)
writer.writerow(('username','created_at','source','comment','like_counts'))


def get_comment(url):
    try:
        wb_data = requests.get(url,headers=headers) # Get Weibo page
        jsondata = wb_data.json()                   # Load Json format data
        datas = jsondata.get('data').get('data')
        for data in datas:
            created_at = data.get("created_at")
            like_counts = data.get("like_counts")
            source = data.get("source")
            username = data.get("user").get("screen_name")
            comment = data.get("text")
            # comment = re.sub(r'(?:回复)?(?://)?@[\w\u2E80-\u9FFF]+:?|\[\w+\]', ',',ori_comment)   This line doesn't really work and I don't know. PLease let me know if you can fix it.
            print json.dumps(comment, encoding="UTF-8", ensure_ascii=False)
            writer.writerow((username,created_at,source,json.dumps(comment, encoding="UTF-8", ensure_ascii=False),like_counts))

    except KeyError:
        print('KeyError')
        pass

for url in url_comment:
    get_comment(url)
    time.sleep(2)          # Or some random time to escape from their supervision. This is jut a simple crawler's demo. I didn't bother that much.

