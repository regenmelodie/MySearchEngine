# 计算词频TF

# 功能：统计词项在文档中出现的次数（词频）
# 输入：词汇表，文档分词list
# 返回：文档词频dict(词汇, 在文档中的出现次数)
def computeTF (word_set, seg):
    tf = dict.fromkeys(word_set, 0)
    for word in seg:
        tf[word] += 1
    return tf