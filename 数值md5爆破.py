from hashlib import md5

for i in range(10000000):
    if md5(str(i).encode('utf-8')).hexdigest()[:6] == '6d0bc1':
        print(i)

