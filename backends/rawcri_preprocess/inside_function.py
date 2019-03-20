from nltk.corpus import wordnet as wn
from gensim import models
import nltk
import os

dictionary = models.TfidfModel.load(r"E:\srtp\CodeRe\backends\models\dictionary.model")


def pre_process(str):
    stoplist = set('for a of the and to in'.split())
    new_doc=[str]
    new_doc = [[word for word in doc.lower().split() if word not in stoplist] for doc in new_doc]
    print(new_doc)
    tags = []
    for tokens in new_doc:
        tags.append(nltk.pos_tag(tokens))
    # 存储有近义词的单词
    print(tags)
    sens = []
    for zz in tags[0]:
        new_doc = []
        if zz[1][0] == 'N' and zz[1][1] == 'N' or zz[1][0] == 'V':
            if len(wn.synsets(zz[0]))>0:
                synset = wn.synsets(zz[0])[0]
                for item in synset.lemma_names():
                    new_doc.append(item)
        if new_doc:
            for item in new_doc:
                sens.append(item)
        else:
            sens.append(zz[0])
    print(sens)
    new_vec = dictionary.doc2bow(' '.join(sens).lower().split())
    print(new_vec)
    return new_vec

if __name__ == '__main__':
    pre_process('in multilabel classification get the score')