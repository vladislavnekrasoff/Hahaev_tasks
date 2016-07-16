# -*- coding: utf-8 -*-

x = [0,1,2,3,4,0,0,5,7,8,0,4,5,7]
i = 0
flag = 0
while i < len(x)-1:
    if x[i] == 0 and x[i+1] == 0:
        flag = 1
        break
    i += 1
if flag == 1:
    print '2 подряд идущих нуля имеются'
else:
    print '2 подряд идущих нулей в массиве нет'