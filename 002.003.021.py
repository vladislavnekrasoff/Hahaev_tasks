# -*- coding: utf-8 -*-

x = [0,1,2,3,4,0,0,5,7,8,0,4,5,7,9]
i = 0
count = 0
chet = 0
chet_count = 0
while i < len(x):
    if x[i] != 0:
        if x[i] % 3 == 0:
            count += 1
        if x[i] % 2 == 0:
            chet += x[i]
            chet_count += 1
    i += 1
x.append(count)
x.append(float(chet)/float(chet_count))
print x