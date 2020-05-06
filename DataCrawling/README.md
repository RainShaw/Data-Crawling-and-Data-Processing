# Contents

## 	Data testing project

@Li Xiaoyu
@Tong Zhiyuan
@Zhang Weiming

### 		[1. Word Frequency](https://github.com/RainShaw/Machine_Learning-Deep_Learning/blob/master/DataCrawling/word_frequency.py)

​				  基于jieba和停用词表'stop_words.txt'对文本数据进行分词处理，并根据word frequency进行			排序，绘制柱状图。

### 		[2. Key-Word Frequency](https://github.com/RainShaw/Machine_Learning-Deep_Learning/blob/master/DataCrawling/keyword_frequency.py)

​				 由于word frequency在一定程度上不能准确反映文本的key-word(例如以主题关键词为检索目			标的数据集)，因此统计key-word frequency对分析很有必要。这里基于TF-IDF方法计算每个word			的权重值，再根据频率进行排序，绘制柱状图

### 		[3. Word Cloud](https://github.com/RainShaw/Machine_Learning-Deep_Learning/blob/master/DataCrawling/wordcloud.py)

​				 基于分词的结果进行词云绘制，出现频率越高，占比越大。

### 		[4. Sentiment Analysis](https://github.com/RainShaw/Machine_Learning-Deep_Learning/blob/master/DataCrawling/sentiment_analyse.py)

​				 基于SnowNLP对文本进行情感分析，计算各词汇的positive概率值，这里进行了三分类   			(positive, negative, neutral)，并根据统计结果绘制直方图(Hist)，折线图(Line)和饼图(Pie)。