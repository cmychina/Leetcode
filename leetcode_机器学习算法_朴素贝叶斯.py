"""
p(y=ci|x)=p(x|y=ci)p(y)/p(x)
argmax{p(y=ci|x)}=argmax {p(x|y=ci)p(y)}=argmax {p(x1|y=ci)p(x1|y=ci)p(x3|y=ci)..p(xn|y=ci)p(y=ci)}
=argmax {log(p(x1|y=ci))+log(p(x2|y=ci))+log(p(x3|y=ci))..+log(p(xn|y=ci))+log(p(y=ci))}
"""

import numpy as np
import pandas as pd
def Bayes(data,label='label'):
    columns=data.columns
    labels=data[label].unique()
    N=len(labels)
    D=data.shape[0]
    #p(y=ci)
    pc=np.empty(shape=(N,1))
    #p(x|y=ci)
    p_xc=[]
    features=[data[i].unique() for i in columns]
    for i in range(N):
        df=data[data[label]==labels[i]]
        Dc=len(df)
        pc[i]=np.array([(Dc+1)/(D+N)])#拉普拉斯平滑
        p_c=[]
        for j in range(len(features)):
            values=features[j]
            Ni=len(values)
            c_attr=[]
            for value in values:
                Dc_xi=df[df[columns[j]]==value].index.size
                c_attr.append((Dc_xi+1)/(Dc+Ni))
            p_c.append(c_attr)
        p_xc.append(p_c)
    return p_xc, pc, N, features, labels

#预测一个样本
def predict(x, p_xc, pc, N, features, labels):
    result=[]
    for i in range(N):
        res=1
        #每个类别ci的先验分布p(x|y=ci)=p(x1|y=ci)p(x2|y=ci)..p(xn|y=ci)
        c=p_xc[i]
        for j in range(len(c)):
            feature_j=c[j]
            for k in range(len(feature_j)):
                if x[j]==features[j][k]:
                    res*=feature_j[k]
                    #res+=np.log2(feature_j[k])
        result.append(pc[i][0]*res)

    max_c=0
    max_index=-1
    for i in range(len(result)):
        if result[i]>max_c:
            max_c=result[i]
            max_index=i
    return result, labels[max_index]


class NaiveBayes:

    def __init__(self):
        self.model = {}  # key 为类别名 val 为字典PClass表示该类的该类，PFeature:{}对应对于各个特征的概率

    def calEntropy(self, y):  # 计算熵
        valRate = y.value_counts().apply(lambda x: x / y.size)  # 频次汇总 得到各个特征对应的概率
        valEntropy = np.inner(valRate, np.log2(valRate)) * -1 #np.inner数组内积
        return valEntropy

    def fit(self, xTrain, yTrain):

        xTrain = pd.concat([xTrain, yTrain], axis=1)
        self.model = self.buildNaiveBayes(xTrain)
        return self.model

    def buildNaiveBayes(self, xTrain):
        yTrain = xTrain.iloc[:, -1]

        yTrainCounts = yTrain.value_counts()  # 频次汇总 得到各个特征对应的概率

        yTrainCounts = yTrainCounts.apply(lambda x: (x + 1) / (yTrain.size + yTrainCounts.size))  # 使用了拉普拉斯平滑
        retModel = {}
        for nameClass, val in yTrainCounts.items():
            retModel[nameClass] = {'PClass': val, 'PFeature': {}}

        propNamesAll = xTrain.columns[:-1]
        allPropByFeature = {}
        for nameFeature in propNamesAll:
            allPropByFeature[nameFeature] = list(xTrain[nameFeature].value_counts().index)
        # print(allPropByFeature)
        for nameClass, group in xTrain.groupby(xTrain.columns[-1]):
            for nameFeature in propNamesAll:
                eachClassPFeature = {}
                propDatas = group[nameFeature]
                propClassSummary = propDatas.value_counts()  # 频次汇总 得到各个特征对应的概率
                for propName in allPropByFeature[nameFeature]:
                    if not propClassSummary.get(propName):
                        propClassSummary[propName] = 0  # 如果有属性灭有，那么自动补0
                Ni = len(allPropByFeature[nameFeature])
                propClassSummary = propClassSummary.apply(lambda x: (x + 1) / (propDatas.size + Ni))  # 使用了拉普拉斯平滑
                for nameFeatureProp, valP in propClassSummary.items():
                    eachClassPFeature[nameFeatureProp] = valP
                retModel[nameClass]['PFeature'][nameFeature] = eachClassPFeature

        return retModel

    def predictBySeries(self, data):
        curMaxRate = None
        curClassSelect = None
        for nameClass, infoModel in self.model.items():
            rate = 0
            rate += np.log(infoModel['PClass'])
            PFeature = infoModel['PFeature']

            for nameFeature, val in data.items():
                propsRate = PFeature.get(nameFeature)
                if not propsRate:
                    continue
                rate += np.log(propsRate.get(val, 0))  # 使用log加法避免很小的小数连续乘，接近零
            if curMaxRate == None or rate > curMaxRate:
                curMaxRate = rate
                curClassSelect = nameClass

        return curClassSelect

    def predict(self, data):
        if isinstance(data, pd.Series):
            return self.predictBySeries(data)
        return data.apply(lambda d: self.predictBySeries(d), axis=1)

