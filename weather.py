#-*-coding:utf-8-*-
import requests
import time
import json
from config import APPID
import csv

URL='http://api.openweathermap.org/data/2.5/weather?units=metric&APPID=%s&lang=zh_cn&q='%APPID


def get_weather(city):
        """
        根据输入的城市名获取天气
        :param city:
        :param length:
        :return:
        """
        r = requests.get(URL+city).json()
        if r['cod'] !=200 :
            return '哦豁，好像没有查到您要的信息,请从新检查输入的格式。'
        else:
            hello = '%s 当前的天气状况为:\n'%city
            coord = '\t经度:%s  纬度:%s\t\n'%(r['coord']['lon'],r['coord']['lat'])
            weather = '\t天气状况:%s  描述:%s\n'%(r['weather'][0]['main'],r['weather'][0]['description'])
            ma = '\t温度:%s  大气压力:%s  湿度:%s  最低温度:%s  最高温度:%s\n'%(r['main']['temp'],
                r['main']['pressure'],r['main']['humidity'],r['main']['temp_min'],r['main']['temp_max'])

            wind = '\t风速:%s\n'%(r['wind']['speed'])
            clouds = '\t云量:%s\n'%r['clouds']
            dt = '\t数据计算时间:%s\n'%time.ctime(r['dt'])
            sys = '\t国家代码:%s  日出时间:%s  日落时间:%s'%(r['sys']['country'],time.ctime(r['sys']['sunrise']),time.ctime(r['sys']['sunset']))



            weather_now = hello+coord+weather+ma+wind+clouds+dt+sys
            return weather_now

def csvtojson():
    with open('china-city-list.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        for i in reader:
            yield {
                'name':i[2],
                'id':i[0].strip('CN')
            }



def get_five_day_weather(city):
    url='http://t.weather.sojson.com/api/weather/city/'
    for item in csvtojson():
        if item['name']==city:
            response = requests.get(url+str(item['id']))
            forecast = response.json()['data']['forecast']
            result=""
            for item in forecast:
                date = item['ymd']+'\t'
                week = item['week']+'\t'
                high = item['high']+'\t'
                low = item['low']+'\t'
                wind = item['fx']+'\t'
                weather = item['type']+'\t'
                notice = item['notice']+'\t'
                result +=date+week+high+low+wind+weather+notice+'\n'
            return result

    else:
        print('对不起，没有您要找的城市！')


if __name__ == '__main__':
    print(get_five_day_weather('瑞金'))
