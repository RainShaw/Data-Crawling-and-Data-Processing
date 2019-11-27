import numpy as np
#Labels are(in order):
#Size(feet^2), Number of bedrooms, Number of floors, Age of rooms(years), Price(＄1000)
# 数据集
def Create_Dataset():
    dataset = [[2104, 5, 1, 45, 460],
               [1416, 3, 2, 40, 232],
               [1534, 3, 2, 30, 315],
               [852, 2, 1, 36, 178]]
    m = len(dataset)                                        #数据行数
    n = len(dataset[0]) - 1                                 #特征数
    theta = []
    for i in range(n+1):                                    #特征数(+1)
        theta.append(0)                                     #theta集
    return dataset, m, n, theta


#假设函数
def Hypothesis(theta, dataset, m):
    hypothesis_value = []                                   #假设函数值
    x = []                                                  #x集
    x0 = []
    x.append(x0)
    for i in range(n):
        x0.append(1.0)                                      #补充x0 = 1.0的集
        xn = [example[i] for example in dataset]            #各个特征集
        x.append(xn)
    theta = np.array(theta)
    for i in range(m):
        s = np.array([sample[i] for sample in x])            #声明引用Numpy
        s = s.reshape(-1, 1)                                 #x0-xn转为列向量
        hypothesis = np.dot(theta, s)                        #矩阵相乘得到假设函数值
        hypothesis_value.extend(hypothesis)                  #.dot得到的值仍未list
    return hypothesis_value                                  #返回假设函数值


#代价函数
def Cost_Function(dataset, m, theta):
    J = 0.0
    hypothesis_value = Hypothesis(theta, dataset, m)
    ym = [example[4] for example in dataset]            #获取y(实际值)的列表
    for i in range(m):
        J += (1/2*m)*((hypothesis_value[i] - ym[i])**2)  #代价函数
    return J


#梯度下降
def Gradient_Descent(theta, m, dataset, n):
    alpha = 0.000000435                                              #learning rate控制精度
    partial_derivative = []
    for j in range(n+1):
        partial_derivative.append(0)                                #初始化偏导数
    hypothesis_value = Hypothesis(theta, dataset, m)
    ym = [example[4] for example in dataset]
    for i in range(m):
        dataset[i].insert(0, 0)                                      #插入x0=1.0
    for j in range(n+1):                                              #特征数(加上x0),j为特征标签
        xm = [example[j] for example in dataset]                    #依次提取同一特征的所有数据
        for i in range(m):                                          #每个特征对应的数据数
            partial_derivative[j] += alpha*(1/m)*(hypothesis_value[i] - ym[i])*xm[i]    #对应某个theta的偏导数和
    for j in range(n+1):
        theta[j] = theta[j] - partial_derivative[j]
    return theta


if __name__ == '__main__':
    dataset, m, n, theta = Create_Dataset()
    for i in range(10000):                                              #迭代次数
        theta = Gradient_Descent(theta, m, dataset, n)
    for j in range(n+1):
        print('theta(%d): %f' % (j, theta[j]))
    data_x = []
    print('The value below to enter are Size(feet^2), Number of bedrooms, Number of floors, Age of rooms(years), Price(＄1000)')
    data_x.append(0)
    for j in range(n):
        print('Please enter the value of x(%d):'% j)
        x = input()
        data_x.append(int(x))
    data_x = np.array(data_x)
    data_x = data_x.reshape(-1, 1)
    theta = np.array(theta)
    y = np.dot(theta, data_x)
    print(y[0])