# 读写工具
import os

# 功能：读取目录下全部txt文件
# 输入：文件目录
# 返回：文章集合 dict(文件名, 文件内容)
def get_text(folderPath):
    mytxts = dict()
    fileList = os.listdir(folderPath)
    for file in fileList:
        with open(os.path.join(folderPath, file), 'r', encoding = 'utf-8') as f:
            atxt = f.read() # 读一个文件
            mytxts[file] = atxt # 将文件加入文件dict
    # print(mytxts)
    return mytxts

# 功能：读取txt并转为list
# 输入：txt文件目录
# 返回：词汇表 list(单词)
def get_vocab(filePath):
    set_all_words = list()
    with open(filePath, 'r', encoding = 'utf-8') as f:
        words = f.read()
        set_all_words = words.split('\t')
    return set_all_words

# 功能：读取txt并转为dict
# 输入：txt文件目录
# 返回：dict(文档名称, list(文档分词))
def get_split_texts(filePath):
    split_texts = dict()
    with open(filePath, 'r', encoding = 'utf-8') as f:
        line = f.readline()
        line = line[:-1] # 去掉换行符
        elems = line.split('\t')
        key = elems[0]
        value = elems[1:len(elems)]
        split_texts[key] = value
        while line:
            line = f.readline()
            line = line[:-1] # 去掉换行符
            elems = line.split('\t')
            key = elems[0]
            if key != '':
                value = elems[1:len(elems)]
                split_texts[key] = value
    # print(split_texts)
    return split_texts

# # 功能：读取txt并转换为list(dict)
# # 输入：txt文件目录
# # 返回：list(dict)
# def get_tfs_list(filePath):
#     tfs_list = list()
#     with open(filePath, 'r', encoding = 'utf-8') as f:
#         line = f.readline()
#         if line != '':
#             line = line[:-1]
#             elems = line.split('\t')
#             tfs = dict()
#             for i in elems:
#                 atf = i.split(',')
#                 tfs[atf[0]] = atf[1]
#             tfs_list.append(tfs)
#         while line:
#             line = f.readline()
#             if line != '':
#                 line = line[:-1]
#                 elems = line.split('\t')
#                 tfs = dict()
#                 for i in elems:
#                     atf = i.split(',')
#                     tfs[atf[0]] = atf[1]
#                 tfs_list.append(tfs)
#     return tfs_list


# 功能：将list写入txt
# 输入：词汇表 list(单词)
# 输出：vocabulary.txt
def write_vocab(alist, folderPath):
    file = os.path.join(folderPath, 'test_vocabulary.txt')
    alist = list(alist) # 将set转为list
    with open(file, 'w', encoding = 'utf-8') as f:
        s = alist[0]
        for word in alist[1:]:
            s = s + '\t' + word
        f.write(s)

# 功能：将dict写入txt
# 输入：记录表 dict(单词, list(文档分词))
# 输出：split_texts.txt
def write_split_text(adict, folderPath):
    file = os.path.join(folderPath, 'test_split_texts.txt')
    with open(file, 'w', encoding = 'utf-8') as f:
        for key in adict:
            s = key
            for i in adict[key]:
                if i != '\n':
                    s = s + '\t' + i
            s = s + '\n'
            f.write(s)

# # 功能：将list(dict)写入txt
# # 输入：全部文档词频集合list(dict(单词, 词频))
# # 输出：tfs.txt
# def write_tfs(tfs_list, folderPath):
#     file = os.path.join(folderPath, 'tfs.txt')
#     with open(file, 'w', encoding = 'utf-8') as f:
#         for atext_tfs in tfs_list:
#             s = str()
#             for key, value in atext_tfs.items():
#                 s = s + key + ',' + str(value) + '\t'
#             s = s[:-1] + '\n'
#             f.write(s)
