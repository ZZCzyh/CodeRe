from gensim import corpora, models, similarities
import logging
import pymongo

tfidf = models.TfidfModel.load(r"E:\srtp\CodeRe\backends/models/tfidf.model")
corpus_tfidf = models.TfidfModel.load(r"E:\srtp\CodeRe\backends\models/corpus_tfidf.model")
dict_file = open(r'E:\srtp\CodeRe\backends\models/dict.txt', 'r')
dict = eval(dict_file.read())
dict_file.close()
index = similarities.MatrixSimilarity(corpus_tfidf)


def conn_mongo(conditions):
    myclient = pymongo.MongoClient("mongodb://zyh:pwd@192.168.1.102")
    mydb = myclient["python_dbs"]
    serial_re =[]
    #count = 0
    for ite in conditions:
        mycol = mydb[ite.split('.')[0]]
        doc = mycol.find({"Name": str(ite)})
        serial_re.append(doc[0]["Synopsis"])
        #for x in mycol.find({}, {"_id": 0, "Synopsis": 1, "Name": 1}):
            #if(x.get('Name')==ite):
               #documents.append(str(x.get("Synopsis")).split('.')[0])
                #break
                #serial_re[count] = x.get("Name")
                #count += 1
        #logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    return serial_re
def detail_conn_mongo(condition):
    myclient = pymongo.MongoClient("mongodb://zyh:pwd@192.168.1.102")
    mydb = myclient["python_dbs"]
    mycol = mydb[condition.split('.')[0]]
    doc = mycol.find({"Name": str(condition)})[0]
    docu={
        'name': doc['Name'],
        'type': doc['Type'],
        'synopsis': doc['Synopsis'],
        'parameters': ["null"],
        'returns': ["null"],
        'ancestor': "null",
        'parent': "null",
        'description_html': "null",
        'language': "python",
    }

    if 'Parameters'in doc.keys():
        if doc['Parameters']!=None:
            docu['parameters']=doc['Parameters']
    if 'Returns'in doc.keys():
        if doc['Returns']!=None:
            docu['returns'] = doc['Returns']
    if 'Ancestor'in doc.keys():
        docu['ancestor'] = doc['Ancestor']
    if 'Parent'in doc.keys():
        docu['parent'] = doc['Parent']
    if 'description_html'in doc.keys():
        docu['description_html'] = doc['description_html']
    return docu

def quickSort( list, start, end):
    if start > end:
        return
    i, j = start, end
    flag = list[start]
    while True:
        # 先从右往左找
        while j > i and list[j] >= flag:
            j = j - 1

        # 再从左往右找
        while i < j and list[i] <= flag:
            i += 1

        if i < j:
            list[i], list[j] = list[j], list[i]
        elif i == j:
            # 当左右相等时第一次递归结束
            list[start], list[i] = list[i], list[start]
            break
    quickSort(list, start, i - 1)
    quickSort(list, i + 1, end)


def data_process(conditions):
    #导入之前已经得到的tfidf模型,可以用它来转换向量（词袋整数计数）表示方法为新的表示方法（Tfidf 实数权重）
    # tfidf = models.TfidfModel.load(r"E:\srtp\CodeRe\backends/models/tfidf.model")
    #导入整个语料库的tfidf表示方法
    # corpus_tfidf = models.TfidfModel.load(r"E:\srtp\CodeRe\backends\models/corpus_tfidf.model")
    #创建索引
    #将要比较的文档转换为tfidf表示方法
    new_vec_tfidf = tfidf[conditions]
    #计算相似度，并返回top20
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
