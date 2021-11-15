import WRTools
import Boolean_operation

# 功能：查找含有keyword的文档
# 输入：keyword列表，索引dict
# 返回：键为keyword的文档名列表list(list)
def get_list(key_list, invert_index):
    ans = list()
    for keyword in key_list:
        ans.append(invert_index.get(keyword))
    return ans

if __name__ == '__main__':
    # invert_index = WRTools.get_index(r'./generate_data/postinglist.txt')
    # print(invert_index.get('断然拒绝')) # 如果当前key不存在，返回None

    docu_set = WRTools.get_text(r'../../dataset/testnews')
    invert_index = WRTools.get_index(r'./generate_data/test_postinglist.txt')
    keyword1 = "口号"
    keyword2 = "教练"
    keyword3 = "李树斌"
    key_list = [keyword1, keyword2, keyword3]
    docs_list = get_list(key_list, invert_index)
    # ans_list = Boolean_operation.and_similar_calc(docs_list)
    ans_list = Boolean_operation.or_similar_calc(docs_list)
    print(ans_list)

    for i in range(0, 5):
        if i >= len(ans_list):
            break
        print(ans_list[i][0])
    