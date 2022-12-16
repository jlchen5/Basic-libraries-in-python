##### Pandas #####

import pandas as pd

df = pd.read_csv('data.csv') 
df.head() # 查看前5行数据
df.tail() # 查看后5行数据

df.info() # 查看数据信息，df是Pandas中的DataFrame对象
df.index() # 查看索引
df.columns() # 查看列名
df.dtypes # 查看数据类型
df.values

age = df['Age'] # 选择Age列
age[:5] # 查看前5个值
age.values[:5] # 查看前5个值，

df = df.set_index('Name') # 将Name列设置为索引
df.head()

age = df['Age'] # 选择Age列
age['Allen, Mr. William Henry'] # 选择索引为Allen, Mr. William Henry的值

df[['Age','Fare']][:5] # 选择Age和Fare两列，查看前5行数据

df.iloc[0] # 选择第一行数据
df.iloc[0:5] # 选择前5行数据
df.iloc[[0,3,6,24],0:2] # 选择第1、4、7、25行，第1、2列的数据

df = df.set_index('Name') # 将Name列设置为索引
df.loc['Allen, Mr. William Henry'] # 选择索引为Allen, Mr. William Henry的行数据
df.loc['Allen, Mr. William Henry','Age'] # 选择索引为Allen, Mr. William Henry的行数据，Age列的值
df.loc['Allen, Mr. William Henry':'Heikkinen, Miss. Laina',:] # 选择索引为Allen, Mr. William Henry到Heikkinen, Miss. Laina的行数据
df.loc['Allen, Mr. William Henry','Age'] = 1000 # 将索引为Allen, Mr. William Henry的行数据，Age列的值修改为1000

df['Fare'] > 40 # 选择Fare列大于40的数据
df[df['Fare'] > 40][:5] # 选择Fare列大于40的数据，查看前5行数据
df[df['Sex'] == 'male'][:5] # 选择Sex列为male的数据，查看前5行数据
df.loc[df['Sex'] == 'male','Age'].mean() 
(df['Age'] > 70).sum() # 选择Age列大于70的数据，统计个数



# 创建dataframe
data = {'country':['Brazil','Russia','India','China','South Africa'],'popilation':[200.4,143.5,1252,1357,52.98]}
df.data = pd.DataFrame(data)
df.data

pd.get_option('display.max_rows') 
pd.set_option('display.max_rows',10) # 设置最大显示行数为10
pd.Series(index = range(0,100)) # 创建Series对象，索引为0-99

pd.get_option('display.max_columns')
pd.set_option('display.max_columns',30) # 设置最大显示列数为30
pd.DataFrame(columns=range(0,30))
 
# Series对象是dataframe中的一列，即dataframe是由Service对象组成的
data = [10,11,12]
index = ['a','b','c']
s = pd.Series(data=data,index=index)
s



s.loc['b'] # 选择索引为b的值
s.iloc[1] # 选择索引为1的值
s1 = s.copy() # 复制s
s1['a'] = 100 # 修改s1中索引为a的值
s1.replace(to_replace = 100,value = 101, inplace = True) # 将s1中的100替换为101, inplace=True表示替换原数据
s1.index
s1.index = ['a','b','c'] # 修改索引
s1.rename(index = {'a':'A'},inplace=True) # 将索引a修改为A

data = [100,110]
index = ['h','k']
s2 = pd.Series(data=data,index=index)
s3 = s1.append(s2) # 将s1和s2合并
s3['j'] = 500

del s1['A'] # 删除索引为A的值
s1.drop(['b','d'],inplace=True) # 删除索引为b和d的值


age = age + 10 
df = pd.DataFrame([[1,2,3],[4,5,6]],index = ['a','b'],columns=['A','B','C'])
df.sum()
df.sum(axis=1) # 按行求和
df.describe() # 查看数据的描述性统计信息

df = pd.read_csv('data.csv')
df.cov() # 查看协方差
df.corr() # 查看相关系数
df['Sex'].value_counts() # 查看Sex列的值的个数
df['Sex'].value_counts(ascending=True) # 查看Sex列的值的个数，按升序排列
df['Age'].value_counts(ascending=True,bins=5) # 查看Age列的值的个数，按升序排列，分为5组


ages = [15,18,20,21,22,34,41,52,63,79]
bins = [10,40,80]
bins_res = pd.cut(ages,bins) # 将ages按bins分组
bins_res.labels # 查看分组结果
pd.value_counts(bins_res) # 查看分组结果的个数
pd.cut(ages,[10,30,50,80])
group_names = ['Youth','Middle','Old']
pd.value_counts(pd.cut(ages,[10,20,50,80],labels=group_names)) 


# merge函数

left = pd.DataFrame({'key':['K0','K1','K2','K3'],'A':['A0','A1','A2','A3'],'B':['B0','B1','B2','B3']})
right = pd.DataFrame({'key':['K0','K1','K2','K3'],'C':['C0','C1','C2','C3'],'D':['D0','D1','D2','D3']})
res = pd.merge(left,right,on='key') # 将left和right按key列合并


left = pd.DataFrame({'key1':['K0','K1','K2','K3'],'key2':['K0','K1','K2','K3'],'A':['A0','A1','A2','A3'],'B':['B0','B1','B2','B3']})
righe = pd.DataFrame({'key1':['K0','K1','K2','K3'],'key2':['K0','K1','K2','K4'],'C':['C0','C1','C2','C3'],'D':['D0','D1','D2','D3']})
res = pd.merge(left,right,on=['key1','key2']) # 将left和right按key1和key2列合并
res = pd.merge(left,right,on=['key1','key2'],how='outer') # 将left和right按key1和key2列合并，how='outer'表示合并后的数据集包含所有的key1和key2的值
res = pd.merge(left,right,on=['key1','key2'],how='outer',indicator = Ture) # indicator=True表示显示合并方式
res = merge(left,right,how = 'left') # how='left'表示合并后的数据集包含left中所有的key1和key2的值，以left为主

data = pd.DataFrame({'k1':['one']*3+['two']*4,'k2':[3,2,1,3,3,4,4]})
data.drop_duplicates() # 删除重复的行
data.drop_duplicates(subset='k1') # 删除重复的行，以k1列为标准

df = pd.DataFrame({'data1':np.random.randn(5),'data2':np.random.randn(5)})
df2 = df.assign(ration = df['data1']/df['data2']) # 在df中添加一列ration，值为data1/data2
df = pd.DataFrame([range(3),[0,np.nan,0],[0,0,np.nan],range(3)] 

df.isnull() # 查看df中的值是否为空
df.isnull().any() # 查看df中的值是否为空，any()表示只要有一个为空就返回True
df.isnull().any(axis=1) # 查看df中的值是否为空，any()表示只要有一个为空就返回True，axis=1表示按行查看
df.fillna(5) # 将df中的空值用5填充


# apply()函数
data = pd.DataFrame({'food':['A1','A2','B1','B2','B3','C1','C2'],'data':[1,2,3,4,5,6,7]})
def food_map(series):
    if series['food'] == 'A1':
        return 'A'
    elif series['food'] == 'A2':
        return 'A'
    elif series['food'] == 'B1':
        return 'B'
    elif series['food'] == 'B2':
        return 'B'
    elif series['food'] == 'B3':
        return 'B'
    elif series['food'] == 'C1':
        return 'C'
    elif series['food'] == 'C2':
        return 'C'
data['food_map'] = data.apply(food_map,axis = 'columns') # 将food列的值映射到food_map列中

def nan_count(columns):
    columns_null = pd.isnull(columns)
    null = columns[columns_null]
    return len(null)
columns_null_count = titanic.apply(nan_count) # 统计每一列的空值个数


def is_minor(row):
    if row['age'] < 18:
        return Ture
    else:
        return False
minors = titanic.apply(is_minor,axis = '1') # 统计每一行的age是否小于18



%matplotlib inline
df = pd.DataFrame(np.random.randn(10,4).cumsum(0),columns=['A','B','C','D'],index=np.arange(0,100,10))
df.plot()

import matplotlib.pyplot as plt
fig.axes = plt.subplots(2,1)
data = pd.Series(np.random.rand(16),index=list('abcdefghijklmnop'))
data.plot(ax = axes[0],kind='bar')
data.plot(ax = axes[1],kind='barh')

df = pd.DataFrame(np.random.rand(6,4),index=['one','two','three','four','five','six'],columns=pd.Index(['A','B','C','D'],name='Genus'))
df.plot(kind='bar')
macro = pd.read_csv('macrodata.csv') # 读取数据
data.plot.scatter('quarter','realgdp')
