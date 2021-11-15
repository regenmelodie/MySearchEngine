import WRTools
import Boolean_operation

# 功能：翻译query逻辑
# 输入：query字符串
# 返回：
def trans_query(query):
    print("trans_query")


if __name__ == '__main__':
    # invert_index = WRTools.get_index(r'./generate_data/postinglist.txt')
    # print(invert_index.get('断然拒绝')) # 如果当前key不存在，返回None
    docu_set = WRTools.get_text(r'../../dataset/testnews')
    invert_index = WRTools.get_index(r'./generate_data/test_postinglist.txt')
    keyword1 = "美国"
    keyword2 = "体育"
    list1 = invert_index.get(keyword1)
    list2 = invert_index.get(keyword2)
    ans_list = Boolean_operation.intersect(list1, list2)
    print(ans_list)
    ans_list = Boolean_operation.union(list1, list2)
    print(ans_list)
    ans_list = Boolean_operation.noword(keyword1, list2, docu_set)
    print(ans_list)