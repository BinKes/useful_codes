#exchange the values of two variables交换两个变量的数值，不需要额外的空间
a=2
b=3
c=4
d=5
e=a,b
a,b=b,a
d,c=c,d/c
#交换数值,相当于执行：(a,b)= (b,a),(d,c)=(c,d/c)先计算右边元组的数值，如何将对应位置的计算结果赋值给左边的变量

print(a,b,c,d)
print(type(e))

'''
outputs:
3 2 1.25 4
<class 'tuple'>
'''