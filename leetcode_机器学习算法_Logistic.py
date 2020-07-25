import numpy as np


def sigmoid(x):
    return 1/(1+np.exp(-x))

#梯度下降法
def graAscent(dataMatrix, matLabel):
    """
    p=1/(1+e^wx)
    :param dataMatrix: m*n
    :param matLabel: m*1
    :return: w
    """
    m, n=np.shape(dataMatrix)
    matMatrix=np.mat(dataMatrix)
    w=np.ones((n,1))
    alpha=0.001
    num=500
    for i in range(num):
        error=sigmoid(matMatrix*w)-matLabel #p-y
        w=w-alpha*matMatrix.transpose()*error
    return w

#随机梯度下降
def stocGraAscent(dataMatrix, matLabel):
    m, n=np.shape(dataMatrix)
    matMatrix=np.mat(dataMatrix)
    w=np.ones((n,1))
    alpha=0.001
    num=20  #这里的这个迭代次数对于分类效果影响很大，很小时分类效果很差
    for i in range(num):
        for j in range(m):#每次只选取一个样本进行梯度更新
            error=sigmoid(matMatrix[j]*w)-matLabel[j]
            w=w-alpha*matMatrix[j].transpose()*error
    return w