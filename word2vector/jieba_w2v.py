# encoding=utf-8
import jieba
lines = '''曰细胞计数
淋巴细胞计数
单核细胞计数
中性粒细胞计数
嗜酸性细胞计数
嗜碱性细胞计数
淋巴细胞
单核细胞
中性粒细胞
嗜酸性细胞
嗜碱性细胞
红细胞计数
血红蛋白
红细胞压积
平均红细胞体积
平均血红蛋白含量
平均血红蛋白浓度
红细胞分布宽度
血小板压积
平均血小板体积
血小板分布宽度
'''
seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list))

s = jieba.cut_for_search(lines)  # 搜索引擎模式
#s = set(s)
s = list(s)
str_dict = {word: s.count(word) for word in set(s) if word != '\n' and word != ','}

print(str_dict)
