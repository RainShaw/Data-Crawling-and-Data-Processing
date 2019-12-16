from sklearn import datasets
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from numpy import dot
from numpy import exp

def import_dataset():
    dataset = datasets.load_breast_cancer()
    x = dataset.data
    y = dataset.target
    b = np.ones(len(x))
    x = np.insert(x,0,values=b,axis=1)
    n = len(x[0])                               # 特征数(包含theta0,对应x0=1)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=30)
    m = len(x_train)                                  # 样本数
    sc = StandardScaler()                       #数据标准化
    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)
    y_train = sc.fit_transform(y_train.reshape(-1,1))           #变为vector
    y_test =y_test.reshape(-1,1)
    return x_train, x_test, y_train, y_test, m, n

def logistic_regression(theta, x_train,y_train,m):
    z = []
    hypothesis = []
    for i in range(m):
        z.append(dot(x_train[i], theta))        #注意相乘顺序
    for example in z:
        hypothesis.append(1/(1+exp(-example[0])))
    delta = []
    delta.append(1/m*(hypothesis[0]-y_train[0])*x_train[0])
    for i in range(1, m):
        delta+=(1/m*(hypothesis[i]-y_train[i])*x_train[i])
    alpha = 0.01
    delta = np.array(delta)
    theta = theta - alpha*delta.reshape(-1,1)
    return theta

def test(theta,x_test,y_test):
    Err = []
    for i in range(len(y_test)):
        z = dot(x_test[i], theta)
        if z >= 0.0:
            z = 1.0
        else:
            z = 0.0
        error = z - y_test[i]
        Err.append(error)
    return Err

if __name__=='__main__':
    x_train, x_test, y_train, y_test, m, n = import_dataset()
    theta = np.zeros((n, 1))                                    # 初始化theta集合
    for i in range(500):
        theta = logistic_regression(theta, x_train, y_train, m)
    print('theta依次为:')
    for i in range(n):
        print('%.4f' % theta[i][0])
    error = test(theta,x_test,y_test)
    count = 0.0
    print('误差为:')
    for i in range(len(error)):
        if error[i] == 0.0:
            count+=1
    print('分类准确率为：%.2f' % (count/len(error)))