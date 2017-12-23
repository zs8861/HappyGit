# -*- coding: utf-8 -*-
import requests
import json
import datetime
import time

#token = hEeNABksrcQXVf8l
#我家坐标: 120.130467,29.316559

res = requests.get("https://api.caiyunapp.com/v2/hEeNABksrcQXVf8l/120.130467,29.316559/realtime.json")
myHome = json.loads(str(res.content, encoding = "utf-8"))

server_time = myHome["server_time"] #服务器时间
status = myHome["status"] #json返回状态
temperature = myHome["result"]["temperature"] #温度
pm25 = myHome["result"]["pm25"] #pm2.5
wind_speed = myHome["result"]["wind"]["speed"] #风速
skycon = myHome["result"]["skycon"] #天气
skycon_zh = "null" #天气对应中文名

if status == "ok":
    if skycon == "CLEAR_DAY":
        skycon_zh = "晴天"
    elif skycon == "CLEAR_NIGHT":
        skycon_zh = "晴夜"
    elif skycon == "PARTLY_CLOUDY_DAY":
        skycon_zh = "白天多云"
    elif skycon == "PARTLY_CLOUDY_NIGHT":
        skycon_zh = "夜晚多云"
    elif skycon == "CLOUDY":
        skycon_zh = "阴天"
    elif skycon == "RAIN":
        skycon_zh = "有雨"
    elif skycon == "SNOW":
        skycon_zh = "下雪了"
    elif skycon == "WIND":
        skycon_zh = "有风"
    elif skycon == "FOG":
        skycon_zh = "有雾"
    else:
        skycon_zh = "null"
else:
    print("获取天气失败！")

timeOnPC = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
timeOnServer = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(server_time))

weather = str("东洲花园秋萍苑12幢上空, 当前气温: " + str(temperature) + 
              "度, 天气: " + str(skycon_zh) +
              ", PM2.5指数: " + str(pm25) +
              ", 风速: " + str(wind_speed) + 
              ", 天气服务器时间: " + str(timeOnServer) +
              ", PC端时间: " + timeOnPC)
print(weather)

url = str("https://sc.ftqq.com/SCU17060Tcb6d837157a6f37b5789bbaa23979b715a1fd9926649c.send?text=" + "无邪的天气小秘书" + "&desp=" + weather)
requests.get(url)