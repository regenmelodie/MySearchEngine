import Inverted_index
import WRTools

if __name__ == '__main__':
    filePath = r'./index.txt'
    invert_index = WRTools.get_index(filePath)
    print(invert_index.get('邀请赛')) # 如果当前key不存在，返回None