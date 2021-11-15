# 布尔搜索模型Query的逻辑运算
import WRTools
import jieba
import math

# 功能：计算and操作的相似度（降序）
# 输入：键为keyword的文档名列表docs_list(查询词, 文档名列表)
# 返回：相似度list(tuple(文档名, 相似度))
def and_similar_calc(docs_list):
    doc_names = list() # 文档名列表
    ans = dict()
    for docs in docs_list:
        doc_names = doc_names + docs
    doc_names = list(set(doc_names)) # 去重
    n = len(docs_list)
    for name in doc_names:
        fz = 0 # 分子
        fm = n # 分母
        for docs in docs_list:
            if name not in docs:
                fz = fz + 1
        ans[name] = 1 - math.pow(fz / fm, 0.5)
    ans_order = sorted(ans.items(), key=lambda x:x[1], reverse=True)
    return ans_order


# 功能：计算or操作的相似度（降序）
# 输入：键为keyword的文档名列表docs_list(查询词, 文档名列表)
# 返回：相似度list(tuple(文档名, 相似度))
def or_similar_calc(docs_list):
    doc_names = list() # 文档名列表
    ans = dict()
    for docs in docs_list:
        doc_names = doc_names + docs
    doc_names = list(set(doc_names)) # 去重
    n = len(docs_list)
    for name in doc_names:
        fz = 0 # 分子
        fm = n # 分母
        for docs in docs_list:
            if name in docs:
                fz = fz + 1
        ans[name] = math.pow(fz / fm, 0.5)
    ans_order = sorted(ans.items(), key=lambda x:x[1], reverse=True)
    return ans_order

# 功能：筛选不含关键词的文档
# 输入：keyword, list1
# 返回：不含关键词的文档list
def noword(keyword, list1, mytxts):
    answer_list = list()
    for docID in list1:
        text = mytxts[docID]
        cut = jieba.cut(text)
        if keyword not in cut: # 文档不含该关键词
            answer_list.append(docID)
    return answer_list


