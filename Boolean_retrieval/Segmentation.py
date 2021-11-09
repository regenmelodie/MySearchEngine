# 分词
# 输入：文章目录
# 输出：词汇表vocabulary.txt
import jieba
import WRTools

# 功能：对所有文档做分词，获得每篇文章的分词结果
# 输入：文章集合 dict(文件名, 文件内容)
# 返回：文章分词集合 dict(文件名, 分词集)
def seg_text(docu_set):
    segs = dict() # 每篇文章的分词集
    for text_name in docu_set.keys():
        field = docu_set[text_name]
        split_field = jieba.cut(field) # 获得一篇文章的分词集
        set_split_field = set(split_field)
        set_split_field.remove('\n')
        set_split_field.remove(' ')
        segs[text_name] = list(set_split_field)
    return segs

# 功能：对所有文档做分词，获得词汇表
# 输入：文章集合 dict(文件名, 文件内容)
# 返回：词向量集合
def segmentation(docu_set):
    all_words = list()
    for text in docu_set.values():
        cut = jieba.cut(text)
        all_words.extend(cut)
    set_all_words = set(all_words)
    set_all_words.remove('\n')
    set_all_words.remove(' ')
    # print(set_all_words)
    print(len(list(set_all_words)))
    return set_all_words

if __name__ == '__main__':
    docu_set = WRTools.get_text(r'../../dataset/news')
    set_all_words = segmentation(docu_set) # 获得词汇表
    WRTools.write_vocab(set_all_words, r'./generate_data')