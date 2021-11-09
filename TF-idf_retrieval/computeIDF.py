# 计算逆文档频率IDF
import math

# 功能：计算反文档频率IDF
# 输入：全部文档词频集合list(dict)
# 返回：词项的反文档频率dict(词汇, 反文档频率)
def computeIDF(tf_list):
    idf = dict.fromkeys(tf_list[0], 0) # key：word
    N = len(tf_list) # 文档总数
    for tf in tf_list: # 遍历文章的词频表
        for word, count in tf.items(): # 遍历当前文章的每一个词
            if count != 0: # 当前遍历的词在文章中出现
                idf[word] += 1 # 包含词项的文档的篇数df+1  
    for word, Ni in idf.items(): # 利用公式将df替换为反文档频率idf
        idf[word] = math.log10(N/Ni)
    return idf