import matplotlib.pyplot as plt
import numpy as np
from snownlp import SnowNLP
import matplotlib


def sentiment():

    """这里使用清洗后的数据集文件"""

    lines = open('file_name', 'r', encoding='utf-8').readlines()
    sentiments = []
    for line in lines:
        s = SnowNLP(line)
        sentiments.append(s.sentiments)
    return sentiments

def drawHist(sentiments):                                               # 绘制直方图
    plt.hist(sentiments, bins=np.arange(0, 1, 0.01), facecolor='k')
    plt.xlabel('Sentiments Probability')                                # x轴表示positive的概率
    plt.ylabel('Quantity')                                              # y轴表示数量
    plt.title('Analysis of Sentiments')
    plt.show()

def drawLine(sentiments):                                               # 绘制折线图
    result = []
    i = 0
    while i < len(sentiments):                                          # 控制值在[-0.5, 0.5]之间
        result.append(sentiments[i] - 0.5)
        i = i + 1

    plt.plot(np.arange(0, 10448, 1), result, 'k-')
    plt.xlabel('Number')
    plt.ylabel('Sentiment')
    plt.title('Analysis of Sentiments')
    plt.show()

def drawPie(sentiments):                                                # 绘制饼图
    positive = 0
    negative = 0
    neutral = 0
    i = 0
    while i < 1000:
        if sentiments[i] >= 0.55:
            positive += 1
        elif sentiments[i] <= 0.45:
            negative += 1
        else:
            neutral += 1
        i = i + 1
    pos = positive / 1000 * 100                                         # positive占比
    neg = negative / 1000 * 100                                         # negative占比
    neu = neutral / 1000 * 100                                          # neutral占比

    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False

    label_list = ["Positive", "Negative", "Neutral"]                    # 各部分标签
    size = [pos, neg, neu]                                              # 各部分大小
    color = ["red", "green", "blue"]                                    # 各部分颜色
    explode = [0.05, 0, 0]                                              # 各部分突出值
    plt.pie(size, explode=explode, colors=color, labels=label_list, labeldistance=1.1,
                                      autopct="%1.1f%%", shadow=False, startangle=90, pctdistance=0.6)
    plt.axis("equal")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    sentiments = sentiment()
    drawHist(sentiments)                                                # 绘制直方图
    drawLine(sentiments)                                                # 绘制折线图
    drawPie(sentiments)                                                 # 绘制饼图