# 计算文档的词项权重TF-IDF
from ctypes import _SimpleCData
import math
from re import M, split
import pandas as pd
import numpy as np

# 功能：统计词项在文档中出现的次数（词频）
# 输入：文档分词list
# 返回：文档词频dict(词汇, 在文档中的出现次数)
def computeTF(seg):
    tf = dict.fromkeys(list(set(seg)), 0)
    for word in seg:
        # if word != '\n' and word != ' ':
        if word != '\n':
            tf[word] += 1
    return tf

# 功能：统计全部文档的词频
# 输入：全部文档分词dict(文件名, 文件分词内容)
# 返回：全部文档词频集合list(dict)
def computeTF_all(split_dict):
    tfs = list()
    for alist in split_dict.values():
        tf = computeTF(alist)
        tfs.append(tf)
    return tfs

# 功能：计算反文档频率IDF
# 输入：全部文档词频集合list(dict)
# 返回：词项的反文档频率dict(词汇, 反文档频率)
def computeIDF(word_set, tf_list):
    # idf = dict.fromkeys(tf_list[0], 0) # key：words
    # print(idf)
    idf = dict.fromkeys(word_set, 0)
    N = len(tf_list) # 文档总数
    # print(N)
    for tf in tf_list: # 遍历文章的词频表
        # print(tf)
        for word in tf.keys(): # 遍历当前文章的每一个词
            if word != '':
                idf[word] += 1 # 包含词项的文档的篇数df+1
    for word, Ni in idf.items(): # 利用公式将df替换为反文档频率idf
        if Ni != 0:
            idf[word] = math.log10(N/Ni)
    return idf

# 功能：计算文档的词项权重
# 输入：文档词频，反文档频率
# 返回：文档的词项权重dict(单词, 权重)
def computeTFIDF(tf, idfs):
    tfidf = dict.fromkeys(idfs.keys())
    for word, tfval in tf.items():
        if word in tfidf.keys():
            tfidf[word] = tfval * idfs[word]
    return tfidf

# 功能：计算全部文档的词项权重
# 输入：全部文档词频集合，反文档频率
# 返回：全部文档的词项权重集合list文档的词项权重
def computeTFIDF_all(tfs_list, idfs):
    tfidfs = list()
    for tf in tfs_list:
        tfidfs.append(computeTFIDF(tf, idfs))
    return tfidfs

# 功能：内积计算q与文档的相似度
# 输入：文档名称，文章和问题结合的TF-IDF列表
# 返回：相似度dict(文档名称, 相似度)
def inner_similar_calc(text_name, tfidfsq):
    sc_dict = dict()
    ans = pd.DataFrame(tfidfsq)
    # print('Q和文档Di的相似度SC(Q, Di) :', (ans.loc[i,:]*ans.loc[0,:]).sum())
    # 位置0是query，text从1开始
    for key, i in zip(text_name, range(1, len(tfidfsq))):
        sc_dict[key] = (ans.loc[i,:]*ans.loc[0,:]).sum()
    return sc_dict

# 功能：余弦计算q与文档的相似度
# 输入：文档名称，文章和问题结合的TF-IDF列表
# 返回：相似度dict(文档名称, 相似度)
def cosine_similar_calc(text_name, tfidfsq):
    sc_dict = dict()
    ans = pd.DataFrame(tfidfsq)
    # print(ans)
    for key, i in zip(text_name, range(1, len(tfidfsq))):
        fz = (ans.loc[i,:]*ans.loc[0,:]).sum()
        di = 0
        q = 0
        for dk2 in ans.loc[i].tolist():
            if np.isnan(dk2):
                dk2 = 0
            di = di + math.pow(dk2, 2)
        for qk2 in ans.loc[0].tolist():
            if np.isnan(qk2):
                qk2 = 0
            q = q + math.pow(qk2, 2)
        sc_dict[key] = fz / math.pow(di * q, 0.5)
    return sc_dict