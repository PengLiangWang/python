#! /usr/bin/python
#! coding = utf-8

import calendar


cal = calendar.month(2016, 1)
print ("2016-01")
print (cal)

#判断是否为闰年
print (calendar.isleap(2016))


#返回给定日期是周几
print ("WeekDay: ",calendar.weekday(2016, 5, 25))



