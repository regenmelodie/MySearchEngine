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

# 功能：读取txt并转为dict
# 输入：txt文件目录
# 返回：索引集合 dict(单词, list(出现该单词的文章))
def get_index(filePath):
    invert_index = dict()
    with open(filePath, 'r', encoding = 'utf-8') as f:
        line = f.readline()
        line = line[:-1] # 去掉换行符
        elems = line.split('\t')
        key = elems[0]
        value = elems[1:len(elems)]
        invert_index[key] = value
        while line:
            line = f.readline()
            line = line[:-1] # 去掉换行符
            elems = line.split('\t')
            key = elems[0]
            value = elems[1:len(elems)]
            invert_index[key] = value
    # print(invert_index)
    return invert_index

# 功能：读取txt并转为list
# 输入：txt文件目录
# 返回：词汇表 list(单词)
def get_vocab(filePath):
    set_all_words = list()
    with open(filePath, 'r', encoding = 'utf-8') as f:
        words = f.read()
        set_all_words = words.split('\t')
    return set_all_words


# 功能：将list写入txt
# 输入：词汇表 list(单词)
# 输出：vocabulary.txt
def write_vocab(alist, folderPath):
    file = os.path.join(folderPath, 'vocabulary.txt')
    alist = list(alist) # 将set转为list
    with open(file, 'w', encoding = 'utf-8') as f:
        s = alist[0]
        for word in alist[1:]:
            s = s + '\t' + word
        f.write(s)

# 功能：将dict写入txt
# 输入：记录表 dict(单词, list(出现该单词的文章))
# 输出：postinglist.txt
def write_index(adict, folderPath):
    file = os.path.join(folderPath, 'postinglist.txt')
    with open(file, 'w', encoding = 'utf-8') as f:
        for key in adict:
            s = key
            for i in iter(adict[key]):
                s = s + '\t' + i
            s = s + '\n'
            f.write(s)