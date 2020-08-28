#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
# ====#====#====#====
# __author__ = "crux"
# FileName: *.py
# Version:1.0.0
# ====#====#====#====


from apscheduler.schedulers.background import BlockingScheduler
import itchat
import requests
import random
import weather


class tuling:
    temp = "雨"


    def jobs(self):
        data = weather.Weather().getWeather()
        result = itchat.search_friends(remarkName="小仙女")
        wea = data['wea']
        temp1 = data['tem1']  # 最高温度
        temp2 = data['tem2']
        win_meter = data['win_meter']
        air_level = data['air_level']
        air_tips = data['air_tips']
        date = data['date']
        msg = '早上好，今天是{}\n天气：{}\n 最低温度：{}，最高温度：{}\n 风速：{}\n空气质量：{}\n 来自亲亲的提示：{}' \
        .format(date, wea, temp2, temp1, win_meter, air_level, air_tips)
        itchat.send_msg(msg, result[0]['UserName'])


    def monitor(self):
        global temp
        data = weather.Weather().getWeather()
        wea = data['wea']

        if (temp != wea):
            result = itchat.search_friends(remarkName="小仙女")
            temp1 = data['tem1']  # 最高温度
            temp2 = data['tem2']
            win_meter = data['win_meter']
            air_level = data['air_level']
            air_tips = data['air_tips']
            msg = '天气：{}\n 最低温度：{}，最高温度：{}\n 风速：{}\n空气质量：{}\n 来自亲亲的提示：{}' \
            .format(wea, temp2, temp1, win_meter, air_level, air_tips)
            itchat.send_msg(msg, result[0]['UserName'])
            print(temp)
            print(wea)
        temp = wea


    def get_response(_info,self):
        print(_info)
        api_url = 'http://www.tuling123.com/openapi/api'
        data = {
            'key': '0df4a8d72d7b45f3afa835975f65f3f0',
            'info': _info,
            'user_id': '123123'
        }
        r = requests.post(api_url, data=data).json()
        print(r.get('text'))
        return r


    @itchat.msg_register(itchat.content.TEXT)
    def text_replys(msg,self):
        print(msg)
        if msg['User']['RemarkName'] == '小仙女':
            return self.get_response(msg['Text'])['text']


    @itchat.msg_register(itchat.content.PICTURE)
    def image_replys(msg):
        print(msg['User']['UserName'])
        if msg['User']['RemarkName'] == '小仙女':
            x = random.randint(0, 900)
            itchat.send_image('/usr/local/emoji/{}.jpg'.format(x),msg['User']['UserName'])
            #itchat.send_image('C:\\Users\\CISDI\\Desktop\\couple\\{}.jpg'.format(x), msg['User']['UserName'])


    def login(self):
        itchat.auto_login(hotReload=True)


if __name__ == '__main__':
    tuling = tuling()
    tuling.login()
    scheduler = BlockingScheduler()
    print(123)
    scheduler.add_job( tuling.jobs, 'cron', day_of_week='0-6', hour='7', minute='0')
    scheduler.add_job( tuling.monitor, 'cron', day_of_week='0-6', hour='7-22', minute='0')
    scheduler.start()
    itchat.run()
