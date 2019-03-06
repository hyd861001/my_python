#!/usr/bin/env python3
# -*- coding: utf-8 -*-
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
    
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
    
    
names = ['Michael', 'Bob', 'Tracy']
for n in names:
    print(n)  

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)  

l=list(range(100))
for x in l:
    sum = sum + x
print(sum) 

sum = 0
n = 99
while n>0:
    sum = sum + n
    n = n - 2
print(sum)

sum = 0
n = 99
while 1:
	  if n < 10:
	  	break
	  sum = sum + n
	  n = n - 2
print(sum)


n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)