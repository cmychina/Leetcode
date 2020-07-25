import numpy as np
import matplotlib.pyplot as plt

class Kmeans:
    def __init__(self,data,k):
        self.self.dataSet=data
        self.k=k
        
    def distEclud(self,x, y):
        return np.sqrt(np.sum((x - y) ** 2))
    
    # 为给定数据集构建一个包含K个随机质心的集合
    def randCent(self):
        m, n = self.dataSet.shape
        centroids = np.zeros((self.k, n))
        for i in range(self.k):
            index = int(np.random.uniform(0, m))
            centroids[i, :] = self.dataSet[index, :]
        return centroids

    # k均值聚类
    def KMeans(self):
        m = self.dataSet.shape[0]  # 行的数目
        # 第一列存样本属于哪一簇,第二列存样本的到簇的中心点的误差
        clusterAssment = np.mat(np.zeros((m, 2)))
        clusterChange = True

        # 第1步 初始化centroids
        centroids = self.randCent()
        while clusterChange:
            clusterChange = False
            # 遍历所有的样本（行数）
            for i in range(m):
                minDist = 100000.0
                minIndex = -1
                # 遍历所有的质心,找出最近的质心
                for j in range(self.k):
                    # 计算该样本到质心的欧式距离
                    distance = self.distEclud(centroids[j, :], self.dataSet[i, :])
                    if distance < minDist:
                        minDist = distance
                        minIndex = j
                # 第 3 步：更新每一行样本所属的簇
                if clusterAssment[i, 0] != minIndex:
                    clusterChange = True
                    clusterAssment[i, :] = minIndex, minDist ** 2
            # 第 4 步：更新质心
            for j in range(self.k):
                pointsInCluster = self.dataSet[np.nonzero(clusterAssment[:, 0].A == j)[0]]  # 获取簇类所有的点
                centroids[j, :] = np.mean(pointsInCluster, axis=0)  # 对矩阵的行求均值

        return centroids, clusterAssment