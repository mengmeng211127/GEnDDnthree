import numpy as np
import pandas as pd


##lncRNA与疾病合并后的特征向量以及标签。
##合并后总共有12874个样本，特征就是维度，
##f_r读取lncRNA的特征
f_r = pd.read_csv('./data2/rna_16feature.csv',header=0,index_col=0).values
f_d = pd.read_csv('./data2/disease_16feature.csv',header=0,index_col=0).values
# f_r = pd.read_csv('./data2/rna_feature.csv',header=0,index_col=0).values
# f_d = pd.read_csv('./data2/disease_feature.csv',header=0,index_col=0).values
all_associations = pd.read_csv('./data2' + '/pair.txt', sep=' ', names=['r', 'd', 'label'])

# label = pd.read_excel('./data1/lncRNADisease-lncRNA-disease associations matrix.xls',header=0,index_col=0)
# label.to_csv("./data1/label.csv",header=None,index=None)
dataset = []
##shape[0]：表示矩阵的行数  ##shape[1]：表示矩阵的列数
##切记在python中位置都是从0开始的。所以iloc[i, 0]也就是读取第i行，第一列；iloc[i, 1]读取第i行，第二列；iloc[i, 2]读取第i行，第三列
##iloc[;1]读取第二列所有的行；iloc[1;]读取第二行所有的列
##对关联矩阵的每行进行循环迭代，
for i in range(int(all_associations.shape[0])):
    ##将第i行、第 0 列的值赋给变量 r
    r = all_associations.iloc[i, 0]
    ##将第 i 行、第 1 列的值赋给变量 c
    c = all_associations.iloc[i, 1]
    ##将第 i 行、第 2 列的值赋给变量 label
    label = all_associations.iloc[i, 2]
    ##将f_r[r]、f_d[c]和label 水平堆叠（按列拼接）成一个新的数组，并将其添加到 dataset 列表中
    dataset.append(np.hstack((f_r[r], f_d[c], label)))
all_dataset = pd.DataFrame(dataset)

all_dataset.to_csv("./data2/data16.csv",header=None,index=None)

print(all_dataset.shape)

print("Fnished!")