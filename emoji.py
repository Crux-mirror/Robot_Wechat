#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
#====#====#====#====  
# __author__ = "crux"  
#HomePage:http://blog.csdn.net/jacson_bai  
#FileName: *.py  
#Version:1.0.0  
#====#====#====#====


import requests
import os
import json

class a():
	x = 0


def getManyPages(keyword, pages):
    params = []
    for i in range(30, 30 * pages + 30, 30):
        params.append({
            'tn': 'resultjson_com',
            'ipn': 'rj',
            'ct': 201326592,
            'is': '',
            'fp': 'result',
            'queryWord': keyword,
            'cl': 2,
            'lm': -1,
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid': '',
            'st': -1,
            'z': '',
            'ic': 0,
            'word': keyword,
            's': '',
            'se': '',
            'tab': '',
            'width': '',
            'height': '',
            'face': 0,
            'istype': 2,
            'qc': '',
            'nc': 1,
            'fr': '',
            'pn': i,
            'rn': 30,
            'gsm': '1e',
            '1488942260214': ''
        })
    url = 'https://image.baidu.com/search/acjson'
    urls = []
    for i in params:
        try:
            urls.append(requests.get(url, params=i).json().get('data'))
        except json.decoder.JSONDecodeError:
            print("解析出错")

    return urls





def getImg(dataList, localPath):
    if not os.path.exists(localPath):  # 新建文件夹
        os.mkdir(localPath)
    for list in dataList:
        for i in list:
            if i.get('thumbURL') != None:
                print('正在下载：%s' % i.get('thumbURL'))
                ir = requests.get(i.get('thumbURL'))
                open(localPath + '%d.jpg' % a.x, 'wb').write(ir.content)
                a.x += 1
            else:
                print('图片链接不存在')




if __name__ == '__main__':
	list = ['表情包']
	for str in list:
		dataList = getManyPages(str, 20)  # 参数1:关键字，参数2:要下载的页数
		getImg(dataList, 'C://Users//CISDI//Desktop//icon//')
    #getImg(dataList, '/usr/local/emoji/')