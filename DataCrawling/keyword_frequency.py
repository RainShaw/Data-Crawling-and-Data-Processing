import jieba
import matplotlib
import matplotlib.pyplot as plt
import math


def splitWord(file):                                                             # 分词
    jieba.load_userdict('stop_words.txt')
    segment = jieba.lcut(file, cut_all =False)
    return segment


def stopwordslist(file_path):                                                   # 导入停用词表
    stopwords = [line.strip() for line in open(file_path, encoding='utf-8').readline()]
    return stopwords


def delstopwords(segment, stopwords, count):                                    # 去除停用词
    for word in segment:
        if word not in stopwords:
            if len(word) != 1:                                                  # 统计词频
                count[word] = count.get(word, 0) + 1


def fileslist(filepath):                                                        # 将各行作为一个文本
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line.strip('\n')                                                    # 去除每行包含的'\n'
    f.close()
    return lines

def count_keyword(word_dic, words_dic, files):                                  # TF-IDF

    """TF词频(Term Frequency)，IDF逆向文件频率(Inverse Document Frequency)。
    TF表示词条在文档d中出现的频率。IDF的主要思想是：如果包含词条t的文档越少，也
    就是n越小，IDF越大，则说明词条t具有很好的类别区分能力"""

    word_idf= {}
    word_tfidf = {}
    num_files = len(files)
    for word in word_dic:
        for words in words_dic:
            if word in words:
                if word in word_idf:
                    word_idf[word] += 1
                else:
                    word_idf[word] = 1
    for key, value in word_dic.items():
        if key != ' ':
            word_tfidf[key] = value * math.log(num_files / (word_idf[key] + 1))   # 计算tf-idf
    value_dic = sorted(word_tfidf.items(), key=lambda x: x[1], reverse=True)
    return value_dic


def drawPicture(count, num):
    x_axis = []
    y_axis = []
    order = sorted(count.items(), key = lambda x: x[1], reverse=True)           # 降序排序
    for l in order[:num]:
        x_axis.append(l[0])
        y_axis.append(l[1])
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']                         # 指定默认字体
    matplotlib.rcParams['axes.unicode_minus'] = False
    plt.bar(x_axis, y_axis)                                                     # 绘制结果图
    plt.title('关键词统计结果(基于TF-IDF)')
    plt.show()


if __name__ == '__main__':
    num = 10                                                                    # 统计前十
    count_key = {}
    value_list = {}
    word_count = []

    """这里使用清洗后的数据集文件"""

    lines = fileslist('file_path')
    for line in lines:
        words = splitWord(line)
        stopwords = stopwordslist('stop_words.txt')
        delstopwords(words, stopwords, count_key)
    word_count.append(count_key)
    for key in word_count:
        value_dic = count_keyword(key, count_key, lines)
        value_list.update(value_dic)
    drawPicture(value_list, num)