import jieba
import matplotlib
import matplotlib.pyplot as plt


def splitWord(file):
    jieba.load_userdict('stop_words.txt')                                     # 停用词表
    segment = jieba.lcut(file, cut_all =False)
    return segment


def stopwordslist(file_path):
    stopwords = [line.strip() for line in open(file_path, encoding='utf-8').readline()]
    return stopwords


def delstopwords(segment, stopwords, count):
    for word in segment:
        if word not in stopwords:
            if len(word) != 1:
                count[word] = count.get(word, 0) + 1


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
    plt.title('词频统计结果')
    plt.show()


if __name__ == '__main__':
    count = {}
    num = 10                                                                    # 统计前十

    """这里使用清洗后的数据集文件"""

    with open('file_path', 'r', encoding='utf-8') as f:
        for line in f:
            words = splitWord(line)
            stopwords = stopwordslist('stop_words.txt')
            delstopwords(words, stopwords, count)
        drawPicture(count, num)
    f.close()