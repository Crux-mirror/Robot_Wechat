import requests
import json


class Weather:

    url = 'https://www.tianqiapi.com/api/?'
    headers = {'User-Agent':'Mozilla/5.0'}

    city = "合川"
    params = {
        'version': 'v1',
        'city': city,
        }
    def getWeather(self):

        res = requests.get(self.url,params=self.params,headers=self.headers)
        res.encoding = 'utf-8'
        #这个是已编译的字符串
        print(type(res.text))

        #将已编码的JSON字符串解码为Python对象，dumps刚好相反
        data = json.loads(res.text)

        print(data)
        return  data['data'][0]