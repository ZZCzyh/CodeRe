# -*- coding: utf-8 -*-
from gensim import corpora, models, similarities
import logging
from collections import defaultdict

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# 文档
documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]

def quickSort():
    return
def data_process (new_vec, documents):
    # 1.分词，去除停用词
    stoplist = set('for a of the and to in'.split())
    texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]
    # 2.创建字典（单词与编号之间的映射）
    dictionary = corpora.Dictionary(texts)
    # 3.建立语料库
    # 将每一篇文档转换为向量
    corpus = [dictionary.doc2bow(text) for text in texts]
    # 4.初始化一个tfidf模型,可以用它来转换向量（词袋整数计数）表示方法为新的表示方法（Tfidf 实数权重）
    tfidf = models.TfidfModel(corpus)
    # 5.将整个语料库转为tfidf表示方法
    corpus_tfidf = tfidf[corpus]
    # 6.将带有tfidf值的语料库转换到lsi空间并创建索引
    index = similarities.MatrixSimilarity(corpus_tfidf)
    new_vec_tfidf = tfidf[new_vec]  # 将要比较文档转换为tfidf表示方法
    # 7.相似度计算
    sims = index[new_vec_tfidf]
    result = {}
    array = []
    i = 0
    for item in sims:
        if item > 0.2:
            array.append(float(item))
            result[i] = item
        i += 1
    list1 = []  # 创建一个新的数组来存储无重复元素的数组
    for element in array:
        if (element not in list1):
            list1.append(element)
    # 8.使用快速排序获取相似度结果的最终排序
    quickSort(list1, 0, len(list1) - 1)
    reco = []
    count = 0
    for i in range(1, 15):
        if count <= 15:
            for key in result:
                if (result[key]) == list1[len(list1)-i]:
                    reco.append(dict[key])
                    count += 1
        else:
            break
    return reco