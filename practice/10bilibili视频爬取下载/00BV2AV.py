'''
Description: 「BV 号」转「av 号」参考：https://gist.github.com/abc1763613206/b8afbb88849835f064f74e652fdb16c5
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-06 10:32:34
LastEditTime: 2021-01-06 10:35:44
FilePath: /Spider/practice/10bilibili视频爬取下载/00BV2AV.py
'''
# 作者：mcfx
# 链接：https://www.zhihu.com/question/381784377/answer/1099438784
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

table='fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
tr={}
for i in range(58):
	tr[table[i]]=i
s=[11,10,3,8,4,6]
xor=177451812
add=8728348608

def dec(x):
	r=0
	for i in range(6):
		r+=tr[x[s[i]]]*58**i
	return (r-add)^xor

def enc(x):
	x=(x^xor)+add
	r=list('BV1  4 1 7  ')
	for i in range(6):
		r[s[i]]=table[x//58**i%58]
	return ''.join(r)

print(dec('BV17x411w7KC'))
print(dec('BV1Q541167Qg'))
print(dec('BV1mK4y1C7Bz'))
print(enc(170001))
print(enc(455017605))
print(enc(882584971))

