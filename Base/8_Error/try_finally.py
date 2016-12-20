#! /usr/bin/python

try:
    print ('try')
    raise KeyboardInterrupt
    print ('end')   #已结束, 不打印

except KeyboardInterrupt:
    print ('catch KeyboardInterrupt!')

finally:
    print ('GoodBye, world!')
