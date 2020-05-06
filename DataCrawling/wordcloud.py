import jieba
import re
from wordcloud import WordCloud


# 数据处理（分词）
r ='[， 。 \ % 、 ； 1234567890n @ # > <]'

"""这里使用清洗后的数据集文件"""

file = open('file_path', 'r', encoding='utf-8').read()
file = re.sub(r, '', file)                          # 去除部分无效字符
cut = jieba.lcut(file)
words = ' '.join(cut)

# 生成词云
wordcloud = WordCloud(font_path="simkai.ttf", background_color="white", width=800, height=660).generate(words)

"""自定义图片保存路径"""

wordcloud.to_file('picture_path')