# 分词并建立倒排索引
# 输入：文章目录
# 输出：倒排索引表index.txt
import jieba
from numpy import invert
import WRTools

# 功能：对所有文档做分词，获得分词集
# 输入：文章集合 dict(文件名, 文件内容)
# 输出：词向量集合
def segmentation(docu_set):
    all_words = list()
    for text in docu_set.values():
        cut = jieba.cut(text)
        all_words.extend(cut)
    set_all_words = set(all_words)
    # print(set_all_words)
    return set_all_words

# 功能：建立倒排索引
# 输入：文章集合，词向量集合
# 输出：索引集合 dict(单词, list(出现该单词的文章))
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
        # 删除空格的index
        if word == ' ':
            invert_index.pop(word)
    # print(invert_index)
    return invert_index
    

if __name__ == '__main__':
    folderPath = r'./testnews'
    docu_set = WRTools.get_text(folderPath)
    set_all_words = segmentation(docu_set)
    invert_index = inverted_index(docu_set, set_all_words)
    WRTools.write_dict(invert_index, './')