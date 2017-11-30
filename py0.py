# -*- coding: utf-8 -*-
import requests
import json
import threading
import datetime

#token = hEeNABksrcQXVf8l
#义乌坐标：120.130467,29.316559
'''
我需要的数据：
温度 yiwuWeather["result"]["temperature"]
天气 yiwuWeather["result"]["skycon"]
PM2.5 yiwuWeather["result"]["pm25"]
风速 yiwuWeather["result"]["wind"]["speed"]
'''


'''res = requests.get("https://api.caiyunapp.com/v2/hEeNABksrcQXVf8l/120.130467,29.316559/realtime.json")
yiwuWeather = json.loads(str(res.content, encoding = "utf-8"))
print(yiwuWeather)
print("\n")'''


yiwuWeather = {
    "status":"ok",
    "lang":"zh_CN",  #目前只支持简体中文（zh_CN、zh_SG）、繁体中文（zh_TW、zh_HK），英语（en_US、en_GB）在测试中
    "server_time":1443418222,
    "tzshift":28800, #时区的偏移秒数，如东八区就是 28800 秒，使用秒是为了支持像尼泊尔这样的差 5 小时 45 分钟的地区，它们有非整齐的偏移量
    "location":[
        25.1552, #纬度
        121.6544 #经度
    ],
    "unit":"metric", #目前只支持米制（metric）和科学计量法（SI），英制还有待开发
    "result":{
        "status":"ok",
        "temperature":33.0,  #温度
        "skycon":"RAIN",  #天气概况
        "pm25": 11,       #pm25值   在新的api中增加的字段
        "cloudrate":0.51,  # 云量
        "humidity":0.92,  #相对湿度
        "precipitation":{  #降水
            "nearest":{ #最近的降水带 //用户补充：nearest这段有时候没有
                "status":"ok",
                "distance":0.77, #距离
                "intensity":0.3125 #角度
            },
            "local":{ #本地的降水
                "status":"ok",
                "intensity":0.2812, #降水强度
                "datasource":"radar" #数据源
            }
        },
        "wind":{ #风
            "direction":25.33, #风向。单位是度。正北方向为0度，顺时针增加到360度。
            "speed":83.3 #风速，米制下是公里每小时
        }
    }
}

temperature = yiwuWeather["result"]["temperature"]
skycon = yiwuWeather["result"]["skycon"]
pm25 = yiwuWeather["result"]["pm25"]
wind_speed = yiwuWeather["result"]["wind"]["speed"]

print("json请求状态 ---> ", yiwuWeather["status"])
print("------东洲花园秋萍苑12幢 - 实时天气提示------")
print("温度 ---> ", temperature)
print("天气 ---> ", skycon)
print("PM2.5 ---> ", pm25)
print("风速 ---> ", wind_speed)
print("------东洲花园秋萍苑12幢 - 实时天气提示------\n")

weather = str("我家门口当前温度：" + str(temperature) + 
              "度, 天气：" + str(skycon) +
              ", PM2.5指数：" + str(pm25) +
              ", 风速：" + str(wind_speed) + ",,,")
print(weather)    

now = datetime.datetime.now() 
time_now = now.strftime('%Y-%m-%d %H:%M:%S')   

url1 = "https://sc.ftqq.com/SCU17060Tcb6d837157a6f37b5789bbaa23979b715a1fd9926649c.send?text=" + "家庭温度提示" + "&desp=" + weather + time_now

res1 = requests.get(url1)
d = json.loads(str(res1.content, encoding = "utf-8"))
print(d)
print("\n")