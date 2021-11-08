# 读写工具
import os

# 功能：读取目录下全部txt文件
# 输入：文件目录
# 输出：文章集合 dict(文件名, 文件内容)
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
# 输出：索引集合 dict(单词, list(出现该单词的文章))
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

# 功能：将dict写入txt
# 输入：索引集合 dict(单词, list(出现该单词的文章))
# 输出：void
def write_dict(adict, folderPath):
    file = os.path.join(folderPath, 'index.txt')
    with open(file, 'w', encoding = 'utf-8') as f:
        for key in adict:
            s = key
            for i in iter(adict[key]):
                s = s + '\t' + i
            s = s + '\n'
            f.write(s)

