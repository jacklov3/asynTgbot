import requests
from config import APPID

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
            dt = '\t数据计算时间:%s\n'%r['dt']
            sys = '\t国家代码:%s  日出时间:%s  日落时间:%s'%(r['sys']['country'],r['sys']['sunrise'],r['sys']['sunset'])



            weather_now = hello+coord+weather+ma+wind+clouds+dt+sys
            return weather_now

if __name__ == '__main__':
    print(get_weather('杭州市'))