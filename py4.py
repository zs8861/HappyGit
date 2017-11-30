import json

'''
data1 = {'b':789,'c':456,'a':123}
data2 = {'a':123,'b':789,'c':456}
d1 = json.dumps(data1,sort_keys=True)
d2 = json.dumps(data2)
d3 = json.dumps(data2,sort_keys=True)
print(d1)
print(d2)
print(d3)
print(d1==d2)
'''

data3 = {
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
        "temperature":28.0,  #温度
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

#print(data3)
print(data3["server_time"])