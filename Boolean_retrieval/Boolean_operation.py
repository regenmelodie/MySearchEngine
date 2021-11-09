# 布尔搜索模型Query的逻辑运算
import WRTools
import jieba

# 功能：求两列表交集
# 输入：list1, list2
# 返回：list = list1 ∩ list2
def intersect(list1, list2):
    answer_list = list()
    ptr1 = 0
    ptr2 = 0
    len1 = len(list1)
    len2 = len(list2)
    while ptr1 < len1 and ptr2 < len2:
        if list1[ptr1] == list2[ptr2]: # 两个posting list遇到一样的docID
            answer_list.append(list1[ptr1])
            ptr1 = ptr1 + 1
            ptr2 = ptr2 + 1
        elif list1[ptr1] < list2[ptr2]:
            ptr1 = ptr1 + 1
        else:
            ptr2 = ptr2 + 1
    return answer_list

# 功能：求两列表并集
# 输入：list1, list2
# 返回：list = list1 ∪ list2
def union(list1, list2):
    answer_list = list(set(list1 + list2))
    return answer_list

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


