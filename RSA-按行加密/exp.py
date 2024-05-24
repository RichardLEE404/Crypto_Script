#!/usr/bin/python
#coding:utf-8

import gmpy2
from Crypto.Util.number import long_to_bytes

n = 920139713
p = 49891
q = 18443
e = 19
phi = (p-1)*(q-1)
d = gmpy2.invert(e,phi)
m =[]
s=b''
with open('roll.txt','r') as f:
    for c in f.readlines():
        m+=long_to_bytes(pow(int(c), d, n))
    for i in range(0,len(m)):
        s+=long_to_bytes(m[i])
print(s)

