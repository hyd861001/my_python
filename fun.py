#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#函数调用
print('-100的绝对值',abs(-100))
print('[1,2,3,4]中的最大值',max([1,2,3,4]))
print('[1,2,3,4]中的最小值',min([1,2,3,4]))
print('字符串\'12\'转为整形：',int('12'))
print('浮点数12.3转为整形',int(12.3))
print('字符串\'12.3\'转为浮点形：',float('12.3'))
print('浮点数12.3转为字符串',str(12.3))
print('整数100转为字符串',str(100))
print('1转为bool型',bool(1))
print('-1转为bool型',bool(-1))
print('0转为bool型',bool(0))
print('1.234转为bool型',bool(1.234))
print('空格\' \'转为bool型',bool(' '))
print('\'\'转为bool型',bool(''))
print('\'aa \'转为bool型',bool('aa'))
print('十进制数123转换为十六进制：',hex(123))

#定义函数
import math
#空函数
def nop():
	pass
#求和函数1
def fun_sum(n):
	x = list(range(n+1))
	sum_n = 0
	for i in x:
		sum_n = sum_n + i
	nop()
	return sum_n
#求和函数2
def fun_sum_1(n):
	x = n
	sum_n = 0
	while x > 0:
		sum_n = sum_n + x
		x = x - 1
	return sum_n
def move(x,y,step,angle = 0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx,ny

def quadratic(a,b,c):
	if b*b-4*a*c < 0 :
		print('无解！！！')
		return
	else:
		x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
		x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
	return x1,x2
	
 	
print(fun_sum(10))
print(fun_sum_1(10))
print(move(1,2,100,math.pi/3))
print(quadratic(1,2,1))
print(quadratic(1,1,1))


#参数缺省
def power(x,n = 2):
  s = 1
  if not isinstance(x,(int,float)):
  	raise TypeError('x应为整型或浮点型')
  	return 
  if not isinstance(n,int):
  	raise TypeError('n应为整型')
  	return
  while n > 0:
  	s = s * x
  	n = n - 1
  return s
print(power(5))
print(power(1.414,2))

#可变参数 自动将参数整合成一个tuple
def calc1(numbers):
	s = 0
	for n in numbers:
		s = s + n * n
	return s
def calc(*numbers):
	s = 0 
	for n in numbers:
		s = s + n * n
	return s
nums = [1,2,3,4,5,6,7]
print(calc1([1,2,3,4]))
print(calc(1,2,3,4,100))
print(calc(*nums))

#关键字参数，可以输入0个和任意个带参数名的参数，这些参数自动组成一个dict
def kk(**xx):
	print(xx)
l1=[1,2,3]
d1={'1':123,'2':'sdadd'}
kk(**d1)
kk(dsd='fasdf',sdf='sdfsf')

#关键字参数的名字不受限制，可以随意，如果要限制关键字的名字可以命名关键字 通过 * 号隔开，
def person(name,age,*,city='beijing',job):
	print(name,age,city,job)

person('hyd',100,city='beijing',job='coder')

#递归函数
def fact(n):
	if n == 1:
		return 1
	else:
		k = n * fact(n - 1)
	return k
	
print(fact(5))
print(fact(20))
	
#尾递归：为了防止函数溢出，return时不返回表达式,python也没有对尾递归做优化
def fact_n(n):
	return fact_w(n,1)
def fact_w(n,m):
	if n == 1:
		return m
	return fact_w(n-1,n * m)



print(fact_n(1000))
