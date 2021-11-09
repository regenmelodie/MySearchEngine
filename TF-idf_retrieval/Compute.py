# 计算文档的词项权重TF-IDF
from ctypes import _SimpleCData
import math
from re import split
import pandas as pd
import Segmentation
import WRTools

# 功能：统计词项在文档中出现的次数（词频）
# 输入：词汇表，文档分词list
# 返回：文档词频dict(词汇, 在文档中的出现次数)
def computeTF(word_set, seg):
    tf = dict.fromkeys(word_set, 0)
    for word in seg:
        if word != '\n' and word != ' ':
            tf[word] += 1
    return tf

# 功能：统计全部文档的词频
# 输入：词汇表，全部文档分词dict(文件名, 文件分词内容)
# 返回：全部文档词频集合dict(文件名, 词频dict)
def computeTF_all(word_set, split_dict):
    tfs = dict()
    for text_name, alist in split_dict.items():
        tf = computeTF(word_set, alist)
        tfs[text_name] = tf
    return tfs

# 功能：计算反文档频率IDF
# 输入：全部文档词频集合list(dict)
# 返回：词项的反文档频率dict(词汇, 反文档频率)
def computeIDF(tf_list):
    idf = dict.fromkeys(tf_list[0], 0) # key：word
    N = len(tf_list) # 文档总数
    # print(N)
    for tf in tf_list: # 遍历文章的词频表
        for word, count in tf.items(): # 遍历当前文章的每一个词
            if count != 0: # 当前遍历的词在文章中出现
                idf[word] += 1 # 包含词项的文档的篇数df+1  
    for word, Ni in idf.items(): # 利用公式将df替换为反文档频率idf
        # print(Ni)
        idf[word] = math.log10(N/Ni)
    return idf

# 功能：计算文档的词项权重
# 输入：文档词频，反文档频率
# 返回：文档的词项权重dict(单词, 权重)
def computeTFIDF(tf, idfs):
    tfidf = dict()
    for word, tfval in tf.items():
        tfidf[word] = tfval * idfs[word]
    return tfidf

# 功能：计算全部文档的词项权重
# 输入：全部文档词频集合，反文档频率
# 返回：全部文档的词项权重集合dict(文件名, 文档的词项权重)
def computeTFIDF_all(tfs_dict, idfs):
    tfidfs = dict()
    for text_name, tf in tfs_dict.items():
        tfidfs[text_name] = computeTFIDF(tf, idfs)
    return tfidfs


if __name__ == '__main__':    
    word_set = WRTools.get_vocab(r'./generate_data/test_vocabulary.txt') # 获得词汇表
    docu_set = WRTools.get_text(r'../../dataset/testnews')
    split_dict = Segmentation.seg_text(docu_set) # 获得全部文章的分词集

    q = "快速的" # 查询文档q
    split_q = Segmentation.seg_string(q) # 分词
    tf_q = computeTF(word_set, split_q) # 计算q的词频
    
    tfs_dict = computeTF_all(word_set, split_dict) # 获得全部文章TF的dict(文件名, 词频)
    tfs_list = list()
    for tf in tfs_dict.values():
        tfs_list.append(tf)
    idfs = computeIDF(tfs_list) # 计算反文档频率
    print(idfs)
    tfidf_q = computeTFIDF(tf_q, idfs) # 计算q的tfidf

    tfidfs = computeTFIDF_all(tfs_dict, idfs)
    tfidfsq = list()
    for tfidf in tfidfs.values():
        tfidfsq.append(tfidf)
    tfidfsq.append(tfidf_q)
    ans = pd.DataFrame(tfidfsq)
    # print(ans)
    # print('Q和文档D1的相似度SC(Q, D1) :', (ans.loc[0,:]*ans.loc[3,:]).sum())
    # print('Q和文档D2的相似度SC(Q, D2) :', (ans.loc[1,:]*ans.loc[3,:]).sum())
    # print('Q和文档D3的相似度SC(Q, D3) :', (ans.loc[2,:]*ans.loc[3,:]).sum())