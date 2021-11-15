# 建立倒排索引
# 输入：词汇表vocabulary.txt
# 输出：记录表postinglist.txt
from numpy import invert
import WRTools
import Segmentation

# 功能：建立倒排索引
# 输入：文章集合，词向量集合
# 返回：记录表 dict(单词, list(出现该单词的文章))
def inverted_index(segs, set_all_words):
    invert_index = dict()    
    # for word in set_all_words:
    #     print(word)
    #     temp = list()
    #     for text_name in segs.keys():
    #         if word in segs[text_name]:
    #             temp.append(text_name)
    #     invert_index[word] = temp
    for word in set_all_words:
        invert_index[word] = list()
    for text_name in segs.keys():
        print(text_name)
        for word in set_all_words:
            if word in segs[text_name]:
                invert_index[word].append(text_name)
    return invert_index
    

if __name__ == '__main__':
    docu_set = WRTools.get_text(r'../../dataset/testnews') # 获得文章集合
    segs = Segmentation.seg_text(docu_set) # 获得文章分词集合
    set_all_words = WRTools.get_vocab(r'./generate_data/test_vocabulary.txt') # 获得词向量集合
    invert_index = inverted_index(segs, set_all_words) # 获得记录表
    WRTools.write_index(invert_index, r'./generate_data')