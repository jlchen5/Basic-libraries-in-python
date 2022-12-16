##### Matplotlib #####

import matplotlib.pyplot as plt # 导入matplotlib.pyplot模块
%matplotlib inline # 在jupyter notebook中显示图像，魔法函数，不是python语法，只在jupyter notebook中使用

plt.plot([1,2,3,4,5],[1,4,9,16,25]) # 画图
plt.xlabel('xlabel',fontsize = 16) # x轴标签设置为xlabel，字体大小为16
plt.ylabel('ylabel',fontsize = 16) 


plt.plot([1,2,3,4,5],[1,4,9,16,25],'-.') # 画图，线条为虚点线
plt.xlabel('xlabel',fontsize = 16) # x轴标签设置为xlabel，字体大小为16
plt.ylabel('ylabel',fontsize = 16)

plt.plot([1,2,3,4,5],[1,4,9,16,25],'-.',color = 'r') # 画图，线条为红色虚点线

sample_array = np.arange(0,10,0.5) # 生成0到10，步长为0.5的数组
plt.plot(sample_array,sample_array,'r--') # 画图，线条为红色虚线
plt.plot(sample_array,sample_array**2,'bs') # 画图，线条为蓝色方块
plt.plot(sample_array,sample_array**3,'go') # 画图，线条为绿色圆点

x = np.linspace(-10,10) # 生成-10到10的等差数列
y = np.sin(x) # 计算x的正弦值
plt.plot(x,y,linewidth = 3.0) 
plt.plot(x,y,color='b',linestyle=':',marker='o',markerfacecolor='r',markersize=10) # 画图，线条为蓝色，线型为虚线，点为红色圆点，点的大小为10

line = plt.plot(x,y)
plt.plot(line,color='r',linewidth=3.0,alpha=0.5) # 画图，线条为红色，线宽为3.0，透明度为0.5

plt.subplot(221) # 2行2列的第一个子图
plt.subplot(212) # 2行1列的第二个子图

plt.subplot(121) # 1行2列的第一个子图
plt.plot(x,y,color = 'r')
plt.subplot(122) # 1行2列的第二个子图
plt.plot(x,y,color = 'b')

plt.subplot(321) # 3行2列的第一个子图
plt.plot(x,y,color = 'r')
plt.subplot(324) # 3行2列的第四个子图
plt.plot(x,y,color = 'b')


plt.plot(x,y,color = 'b',linestyle=':',marker='o',markerfacecolor='r',markersize=10) # 画图，线条为蓝色，线型为虚线，点为红色圆点，点的大小为10
plt.xlabel(' x:---' )
plt.ylabel(' y:---' )
plt.title('sample plot:---')
plt.text(0,0,' sample text') # 在坐标(0,0)处添加文本
plot.grid(True) # 添加网格
plot.annotate('sample annotation',xy=(-5,0),xytext=(-2,0.3),arrowprops=dict(facecolor='red',shrink=0.05,headwidth=20,headlength=20)) # xy为箭头尖端的坐标，xytext为注释文本的坐标，arrowprops为箭头的属性

x = range(10)
y = range(10)
fig = plt.gca() # 获取当前的坐标轴
plt.plot(x,y)
fig.axes.get_xaxis().set_visible(False) # 隐藏x轴
fig.axes.get_yaxis().set_visible(False) # 隐藏y轴

import math
x = np.random.normal(loc = 0.0,scale = 1.0,size = 300) 
width = 0.5
bins = np.arange(math.floor(x.min())-width,math.ceil(x.max())+width,width) # 生成等差数列
ax = plt.subplot(111) # 1行1列的第一个子图

ax.spines['top'].set_visible(False) # 隐藏上边框
ax.spines['right'].set_visible(False) # 隐藏右边框
plt.tick_params(bottom='off',top='off',right='off',left='off') # 隐藏刻度
plt.grid() # 添加网格
plt.hist(x,alpha=0.5,bins=bins) # 画直方图，透明度为0.5，bins为等差数列

x = range(10)
y = range(10)
labels = ['sample plot' for i in range(10)]
fig,ax = plt.subplots()
plt.plot(x,y)
plt.title('sample plot')
ax.set_xticklabels(labels,rotation=45,horizonalalignment='right') # 设置x轴刻度标签，旋转45度，水平对齐方式为右对齐

x = np.arange(10)

for i in range(1,4):
    plt.plot(x,i*x**2,label = ' Grooup %d' %i)  # for循环画图，label为图例
plt.legend(loc='best') # 显示图例，loc为图例的位置

print(help(plt.legend)) # 查看legend的帮助文档

fig = plt.figure()
ax = plt.subplot(111)

x = np.arange(10)
for i in range(1,4):
    plt.plot(x,i*x**2,label = ' Grooup %d' %i)  # for循环画图，label为图例
ax.legend(loc='upper center',bbox_to_anchor=(0.5,1.15),ncol=3)

plt.style.available

x = np.linspace(-10,10) # 生成等差数列，从-10到10，默认个数为50
y = np.sin(x)
plt.plot(x,y)

plt.style.use('dark_background') # 设置背景为黑色
plt.plot(x,y)

plt.style.use('bmh') # 设置背景为灰色
plt.plot(x,y)

plt.style.use('ggplot') # 设置背景为灰色
plt.plot(x,y)


np.random.seed(0)
x = np.arange(5) # 生成等差数列，从0到4，默认个数为5
y = np.random.randint(-5,5,5) # 生成随机整数，从-5到5，个数为5
fig,axes = plt.subplots(ncols = 2)
v_bars = axes[0].bar(x,y,color = 'red') # 画垂直柱状图
h_bars = axes[1].barh(x,y,color = 'red') # 画水平柱状图
axes[0].axhline(0,color='grey',linewidth=2) # 画水平线，颜色为灰色，线宽为2
axes[1].axvline(0,color='grey',linewidth=2) # 画垂直线，颜色为灰色，线宽为2
plt.show()

mean_values = [1,2,3]
variance = [0.2,0.4,0.5]
bar_label = ['bar1','bar2','bar3']
x_pos = list(range(len(bar_label))) 
plt.bar(x_pos,mean_values,yerr=variance,alpha=0.3) # 画柱状图，yerr为误差线，alpha为透明度
max_y = max(zip(mean_values,variance)) # 获取最大值，zip函数将两个列表合并为元组
plt.ylim([0,(max_y[0]+max_y[1])*1.2]) 
plt.ylabel('variable y')
plt.xticks(x_pos,bar_label) # 设置x轴刻度标签
plt.show()


data = range(200,225,5)
bar_labels = ['a','b','c','d','e']
fig = plt.figure(figsize=(10,8)) # 设置画布大小
y_pos = np.arange(len(data)) # 生成等差数列，从0到4，默认个数为5
plt.yticks(y_pos,bar_labels,fontsize=16) # 设置y轴刻度标签，字体大小为16
bars = plt.barh(y_pos,data,alpha=0.5,color='green') # 画水平柱状图，透明度为0.5，颜色为绿色
plt.vlines(min(data),-1,len(data)+0.5,linestyles='dashed') # 画垂直线，颜色为灰色，线宽为2
for b,d in zip(bars,data):
    plt.text(b.get_width()+b.get_width()*0.05,b.get_y()+b.get_height()/2,'{0:.2%}'.format(d/min(data)))
plt.show()


pattern = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')
mean_value = range(1,len(pattern)+1)
x_pos = list(range(len(mean_value)))
bars = plt.bar(x_pos,mean_value,color='white')
for bar,pattern in zip(bars,patterns):
    bar.set_hatch(pattern) # 设置柱状图的填充样式
plt.show()



data = range(200,225,5) # 生成等差数列，从200到225，步长为5
bar_labels = ['a','b','c','d','e']
fig = plt.figure(figsize=(10,8)) # 设置画布大小
y_pos = np.arange(len(data)) # 生成等差数列，从0到4，默认个数为5
plt.yticks(y_pos,bar_labels,fontsize=16) # 设置y轴刻度标签，字体大小为16
bars = plt.barh(y_pos,data,alpha=0.5,color='green') # 画水平柱状图，透明度为0.5，颜色为绿色
plt.vlines(min(data),-1,len(data)+0.5,linestyles='dashed') # 画垂直线，颜色为灰色，线宽为2
for b,d in zip(bars,data):
    plt.text(b.get_width()+b.get_width()*0.05,b.get_y()+b.get_height()/2,'{0:.2%}'.format(d/min(data)))
plt.show()


print(help(plt.boxplot))



fig,axes = plt.subplots(ncols=1,nrows=2,figsize=(12,5)) # 设置画布大小
sample_data = [np.random.normal(0,std,100) for std in range(6,10)] # 生成正态分布数据
axes[0].violinplot(sample_data,showmeans=False,showmedians=True) # 画小提琴图，不显示均值，显示中位数
axes[0].set_title('violin plot') # 设置标题
axes[1].boxplot(sample_data)
axes[1].set_title('box plot') # 设置标题

for ax in axes: # 将axes中的元素赋值给ax
    ax.yaxis.grid(True) # 设置y轴网格线
    ax.set_xticks([y+1 for y in range(len(sample_data))]) # 设置x轴刻度
    ax.set.xticklabels(['x1','x2','x3','x4']) # 设置x轴刻度标签
plt.show()


data = np.random.normal(0,20,1000) # 生成正态分布数据
bins = np.arange(-100,100,5) # 生成等差数列，从-100到100，步长为5
plt.hist(data,bins=bins) # 画直方图
plt.xlim([min(data)-5,max(data)+5]) # 设置x轴范围
plt.show()


import random
data1 = [random.gauss(15,10) for i in range(500)] # random.gauss()生成正态分布数据，for循环生成500个数据
data2 = [random.gauss(5,5) for i in range(500)]
bins = np.arange(-50,50,2.5)
plt.hist(data1,bins=bins,label='class 1',alpha=0.3) # 画直方图，透明度为0.3
plt.hist(data2,bins=bins,label='class 2',alpha=0.3)
plt.legend(loc='best')
plt.show()

N = 1000
x = np.random.randn(N)
y = np.random.randn(N)
plt.scatter(x,y,alpha=0.3)
plt.grid(Ture)
plt.show()



impoer matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax =  fig.add_subplot(111,projection='3d')
plt.show()

np.random.seed(1)
def randrange(n,vmin,vmax):
    return (vmax-vmin)*np.random.rand(n)+vmin
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
n = 100
for c,m,zlow,zhigh in [('r','o',-50,-25),('b','x',-30,-5)]:
    xs = randrange(n,23,32)
    ys = randrange(n,0,100)
    zs = randrange(n,int(zlow),int(zhigh))
    ax.scatter(xs,ys,zs,c=c,marker=m)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
for c,z in zip (['r','g','b','y'],[30,20,10,0]):
    xs = np.arange(20)
    ys = np.random.rand(20)
    cs = [c]*len(xs)
    ax.bar(xs,ys,zs=z,zdir='y',color=cs,alpha=0.5)
plt.show()
