# -*- coding: utf-8 -*-

import threading
import datetime

#Python实现定时器功能
def fun_timer():
    now = datetime.datetime.now()    
    print('Hello Timer!' + now.strftime('%Y-%m-%d %H:%M:%S'))
    global timer
    timer = threading.Timer(2, fun_timer)
    timer.start()

timer = threading.Timer(0, fun_timer)
timer.start()

#timer.sleep(15) # 15秒后停止定时器
#timer.cancel()