import WRTools
import Segmentation
import WRTools
import Compute

# 功能：过滤query中未出现在词汇表的词
# 输入：词汇表，问题分词
# 返回：过滤后的问题分词list
def filter_query(word_set, split_q):
    ans_q = list()
    for q in split_q:
        if q in word_set:
            ans_q.append(q)
    return ans_q

# 功能：调用Compute中的函数，处理查询文档q，计算q与文档的相似度
# 输入：词汇表，文章分词集，查询文档q
# 返回：查询文档q与文档的相似度dict(文档名称, 相似度)
def compute_treat(word_set, split_dict, q):
    split_q = Segmentation.seg_string(q) # 分词
    split_q = filter_query(word_set, split_q) # 过滤问题分词
    tf_q = Compute.computeTF(split_q) # 计算q的词频
    # print(tf_q)

    tfs_list = Compute.computeTF_all(split_dict) # 获得全部文档TF的dict(文件名, 词频)
    print('文档的tf计算已完成')

    idfs = Compute.computeIDF(word_set, tfs_list) # 计算反文档频率
    print('文档的idf计算已完成')
    tfidf_q = Compute.computeTFIDF(tf_q, idfs) # 计算q的tfidf
    print('q的tfidf计算已完成')

    tfidfs = Compute.computeTFIDF_all(tfs_list, idfs)
    print('文档的tfidf计算已完成')

    tfidfsq = list()
    tfidfsq.append(tfidf_q)
    for tfidf in tfidfs:
        tfidfsq.append(tfidf)
    text_name = split_dict.keys()
    # sc_list = Compute.inner_similar_calc(text_name, tfidfsq)
    sc_list = Compute.cosine_similar_calc(text_name, tfidfsq)
    print('相似度计算已完成')
    return sc_list


if __name__ == '__main__':    
    word_set = WRTools.get_vocab(r'./generate_data/test_vocabulary.txt') # 获得词汇表
    docu_set = WRTools.get_text(r'../../dataset/testnews')
    split_dict = WRTools.get_split_texts(r'./generate_data/test_split_texts.txt')
    q = "米克尔森休斯顿热身赛，" # 查询文档q
    sc_dict = compute_treat(word_set, split_dict, q) # 获得q与文档的相似度dict
    sc_dict_order = sorted(sc_dict.items(), key=lambda x:x[1], reverse=True)
    print('排序已完成')
    for i in range(0, 5):
        print(sc_dict_order[i][0])
    
    print(sc_dict)