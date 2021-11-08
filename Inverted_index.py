# 建立倒排索引
# 输入：词汇表vocabulary.txt
# 输出：记录表postinglist.txt
import jieba
from numpy import invert
import WRTools

# 功能：建立倒排索引
# 输入：文章集合，词向量集合
# 返回：记录表 dict(单词, list(出现该单词的文章))
def inverted_index(docu_set, set_all_words):
    invert_index = dict()
    for word in set_all_words:
        temp = list()
        for text_name in docu_set.keys():
            field = docu_set[text_name]
            split_field = jieba.cut(field) # 获得一篇文章的分词集
            if word in split_field:
                temp.append(text_name)
        invert_index[word] = temp
    # print(invert_index)
    return invert_index
    

if __name__ == '__main__':
    folderPath = r'../dataset/testnews'
    docu_set = WRTools.get_text(folderPath)
    filePath = r'./generate_data/vocabulary.txt'
    set_all_words = WRTools.get_vocab(filePath)
    invert_index = inverted_index(docu_set, set_all_words) # 获得记录表
    WRTools.write_index(invert_index, r'./generate_data')