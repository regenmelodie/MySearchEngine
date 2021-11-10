import WRTools
import Segmentation
import Compute
import pandas as pd

# 功能：过滤query中未出现在词汇表的词
# 输入：词汇表，问题分词
# 返回：过滤后的问题分词list
def filter_query(word_set, split_q):
    ans_q = list()
    for q in split_q:
        if q in word_set:
            ans_q.append(q)
    return ans_q


if __name__ == '__main__':    
    word_set = WRTools.get_vocab(r'./generate_data/test_vocabulary.txt') # 获得词汇表
    docu_set = WRTools.get_text(r'../../dataset/testnews')
    split_dict = Segmentation.seg_text(docu_set) # 获得全部文章的分词集

    q = "毕文静、邢傲伟两位体操世界冠军担当主持的派对活动" # 查询文档q
    split_q = Segmentation.seg_string(q) # 分词
    split_q = filter_query(word_set, split_q) # 过滤问题分词
    tf_q = Compute.computeTF(word_set, split_q) # 计算q的词频
    
    tfs_dict = Compute.computeTF_all(word_set, split_dict) # 获得全部文章TF的dict(文件名, 词频)
    tfs_list = list()
    for tf in tfs_dict.values():
        tfs_list.append(tf)
    idfs = Compute.computeIDF(tfs_list) # 计算反文档频率
    # print(idfs)
    tfidf_q = Compute.computeTFIDF(tf_q, idfs) # 计算q的tfidf

    tfidfs = Compute.computeTFIDF_all(tfs_dict, idfs)
    # print(tfidfs)
    tfidfsq = list()
    tfidfsq.append(tfidf_q)
    for tfidf in tfidfs.values():
        tfidfsq.append(tfidf)
    ans = pd.DataFrame(tfidfsq)
    # print('Q和文档D1的相似度SC(Q, D1) :', (ans.loc[1,:]*ans.loc[0,:]).sum())
    # print('Q和文档D2的相似度SC(Q, D2) :', (ans.loc[2,:]*ans.loc[0,:]).sum())
    # print('Q和文档D3的相似度SC(Q, D3) :', (ans.loc[3,:]*ans.loc[0,:]).sum())
    i = 1
    for key in tfidfs.keys():
        print(key, (ans.loc[i,:]*ans.loc[0,:]).sum())
        i = i + 1