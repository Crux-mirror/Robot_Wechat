#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
#====#====#====#====  
# __author__ = "crux"
#FileName: *.py  
#Version:1.0.0
#description:生成折线图
#====#====#====#====

import matplotlib.pyplot as plt
from weather import Weather
from pylab import mpl

def linePlotsl(x_axis,y_axis,wea):
    mpl.rcParams['font.sans-serif'] = ['FangSong']
    mpl.rcParams['axes.unicode_minus'] = False

    plt.figure()
    plt.plot(x_axis,y_axis,'-o',label='温度')
    plt.plot(wea,'--',color='g',label='天气')
    plt.yticks([y for y in range(1,45,5)])
    ax = plt.gca()
    for x,y in zip(x_axis,y_axis):
            ax.text(x,y,str(y),color='r',fontsize=12)
    plt.show()

def get_xy():
    data = Weather.getWeather(Weather)
    hours = data['hours']
    x_axis = []
    y_axis = []
    wea = []
    for hour in hours:
        x_axis.append(hour['day'][3:])
        y_axis.append(int(hour['tem'][0:-1]))
        wea.append(hour['wea'])
    return x_axis,y_axis,wea
if __name__ == '__main__':
    x,y,wea = get_xy()
    linePlotsl(x,y,wea)