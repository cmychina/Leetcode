import numpy as np
# 距离函数定义
def l1_distance(a, b):
    return np.sum(np.abs(a - b), axis=1)

def l2_distance(a, b):
    ans=[np.sqrt((i-b)**2) for i in a]
    return ans

# 分类器实现
class kNN(object):

    def __init__(self, n_neighbors=1, dist_func=l2_distance):
        self.n_neighbors = n_neighbors
        self.dist_func = dist_func

    # 训练模型的方法
    def fit(self, x, y):
        self.x_train = x
        self.y_train = y

    # 模型预测
    def predict(self, x):

        y_pred = np.zeros((x.shape[0], 1))
        for i, x_test in enumerate(x):
            # x_test和所有训练数据计算距离
            #print(self.x_train,x_test)
            distances = self.dist_func(self.x_train, x_test)
            #print(distances)
            # 对得到的距离按照由近到远排序
            nn_indexes = np.argsort(distances)[:self.n_neighbors]
            # 选取其中最近的k个点，统计类别出现频率最高的那个，赋给y_predict[i]
            y_res = self.y_train[nn_indexes].ravel().tolist()
            y_pred[i] = np.argmax(np.bincount(y_res))
        return y_pred

x=np.array([1,2,3,4,1,2,3,4,6,7,8,9,10])
y=np.array([1,1,1,1,1,1,1,1,0,0,0,0,0])
x_test=np.array([1,10,2,5])
knn=kNN()
knn.fit(x,y)
print(knn.predict(x_test))
