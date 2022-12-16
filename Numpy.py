##### Numpy #####

import numpy as np

array = [1,2,3,4,5,6,7,8,9,10]
array + 1

array = np.array([1,2,3,4,5,6,7,8,9,10])
print(type(array))


array2 = array + 1
array2

array2 + array
array2 * array

array.shape # 展现数据维度，一个逗号“,”表示一个维度，数字表示元素数目

sample_list = [1,2,3,4,5,6,7,8,9,10]
sample_list.shape # python的list没有shape属性，所以会报错，导入numpy后，list就变成了numpy的array

np.array([[1,2,3],[4,5,6]]) # 二维数组，注意双重中括号

sample_list = [1,2,3,4,5]
sample_array = np.array(sample_list)
sample_array.shape


sample_list = [1,2,3,4,5,'6']
sample_array = np.array(sample_list)
print(sample_array)

sample_list = [1,2,3,4,5,6.0]
sample_array = np.array(sample_list)
print(sample_array) # ndarray中的元素必须是同一类型，否则会自动转换为同一类型，int转换为float，float转换为string

type(sample_array) # 查看数据格式
sample_array.dtype # 查看数据类型
sample_array.size # 查看数据元素个数
sample_array.ndim # 查看数据维度

sample_array[1:3] # 切片，注意是左闭右开区间,从第二个元素开始到第三个元素
sample_array[-2:] # 从倒数第二个元素开始到最后

sample_array = np.array([[1,2,3],[4,5,6],[7,8,9]]) # 二维数组
sample_array[1,1] = 10 # 修改第二行第二列的元素

sample_array[1] # 取第二行
sample_array[:,1] # 取第二列，冒号表示所有行或者所有列，逗号前面表示行，逗号后面表示列

sample_array = np.arange(0,100,10) # 生成0到100的等差数列，步长为10
mask = np.array([1,0,1,0,1,0,1,0,1,0],dtype=bool) # 生成一个布尔型的掩码，1表示True，0表示False
sample_array[mask] # 通过掩码取出数组中的元素，掩码中为True的元素会被取出，为False的元素会被忽略

random_array = np.random.rand(10) # 生成10个随机数,均匀分布,[0,1)

mask = random_array > 0.5 # 生成一个掩码，大于0.5的为True，小于0.5的为False
mask

sample_array = np.array([10,20,30,40,50]) # 生成一个数组
np.where(sample_array > 30) # 返回大于30的元素的索引
sample_array[np.where(sample_array > 30)] # 返回大于30的元素

y = np.array([1,1,1,4])
x = np.array([1,1,1,2])
x == y

np.logical_and(x,y) # 逻辑与，两个都为True才为True
np.logical_or(x,y) # 逻辑或，两个都为False才为False

sample_array = np.array([1,2,3,4,5],dtype=np.float32)
sample_array.dtype

sample_array = np.array(['1','10','3.5','str'],dtype=np.object)
sample_array = np.array([1,2,3,4,5]) 
sample_array2 = np.asarray(sample_array,dtype=np.float32) # 将sample_array转换为float32类型

sample_array = np.array([[1,2,3],[4,10,6],[7,8,9]])
sample_array2 = sample_array
sample_array2[1,1] = 100

sample_array2 = sample_array.copy() # 深拷贝，sample_array2和sample_array是两个独立的数组
sample_array2[1,1] = 10000

sample_array = np.array([[1,2,3],[4,5,6]])
np.sum(sample_array) # 求和

np.sum(sample_array,axis=0) # 按列求和
np.sum(sample_array,axis=1) # 按行求和

sample_array.prod() # 求积
sample_array.prod(axis = 0) 
sample_array.prod(axis = 1) 
sample_array.min() # 求元素中的最小值

sample_array.min(axis = 0) # 求每一列的最小值
sample_array.min(axis = 1) # 求每一行的最小值

sample_array.mean() # 求均值
sample_array.mean(axis = 0) # 求每一列的均值
sample_array.mean(axis = 1) # 求每一行的均值

sample_array.std() # 求标准差
sample_array.std(axis = 0) # 求每一列的标准差
sample_array.std(axis = 1) # 求每一行的标准差

sample_array.var() # 求方差
sample_array.clip(2,4) # 将数组中的元素限制在2到4之间

sample_array = np.array([1.2,3.56,6.41])
sample_array.round() # 四舍五入

sample_array.round(decimals=1) # 小数点后保留一位

sample_array.argmin() # 求最小值的索引
sample_array.argmin(axis = 0) # 求每一列最小值的索引
sample_array.argmin(axis = 1) # 求每一行最小值的索引

x = np.array([1,2,3,4,5])
y = np.array([1,2,3,4,5])
np.multiply(x,y) # 对应元素相乘
np.dot(x,y) # 矩阵乘法

x.shape = 5,1 # 将x转换为5行1列的矩阵
np.dot(x,y) # 矩阵乘法

y.shape = 1,5 # 将y转换为1行5列的矩阵
np.dot(x,y) 
np.dot(y,x) 
