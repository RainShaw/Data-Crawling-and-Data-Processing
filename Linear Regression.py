#数据集
def Create_Dataset():
    dataset = [[1, 0.5],
               [2, 1],
               [4, 2],
               [0, 0]]
    m = len(dataset)
    return dataset,m


#假设函数
def Hypothesis(theta0,theta1,dataset):
    hypothesis_value=[]                                             #假设函数值
    xm = [example[0] for example in dataset]                        #获取x的列表
    for x in xm:
        hypothesis = theta0 + theta1*x                              #计算对应的值
        hypothesis_value.append(hypothesis)
    return hypothesis_value


#代价函数
def Cost_Function(dataset,m,theta0,theta1):
    J = 0.0
    hypothesis_value = Hypothesis(theta0,theta1,dataset)
    ym = [example[1] for example in dataset]                        #获取y的列表
    for i in range(m):
        J += (1/2*m)*((hypothesis_value[i] - ym[i])**2)             #代价函数
    return J


#梯度下降
def Gradient_Descent(theta0,theta1,m,dataset):
    alpha = 0.01                                                    #learning rate
    partial_derivative_sum0 = partial_derivative_sum1 = 0.0         #偏导数
    hypothesis_value = Hypothesis(theta0, theta1, dataset)
    xm = [example[0] for example in dataset]
    ym = [example[1] for example in dataset]
    for i in range(m):
         partial_derivative_sum0 += alpha*(1/m)*(hypothesis_value[i] - ym[i])   #theta0的偏导数和
         partial_derivative_sum1 += alpha*(1/m)*(hypothesis_value[i] - ym[i])*xm[i] #theta1的偏导数和
    theta0 = theta0 - partial_derivative_sum0                       #theta0下降
    theta1 = theta1 - partial_derivative_sum1                       #theta1下降
    return theta0, theta1


#预测函数
def Prediction(theta0,theta1,x):
    y = theta0 + theta1 * x
    return y


if __name__ == '__main__':
    dataset, m = Create_Dataset()
    theta0 = 0.0
    theta1 = 0.0
    for i in range(5000):                                              #迭代次数
        theta0, theta1 = Gradient_Descent(theta0,theta1,m,dataset)
    print('y = %f + %f * x' % (theta0, theta1))
    print('Please enter the value of x:')
    x = input()
    y = Prediction(theta0,theta1,int(x))
    print(y)