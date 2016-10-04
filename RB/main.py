# -*- coding: utf-8 -*-
import json, MeCab, sys, os, random
import re


def split_conversation(conversatioin):
    seped = re.split('すか|です|たか|した', conversation)
    return seped


def find_in_dic(dic, word):
    for d in dic:
        if d.find(word.encode("utf-8")) != -1:
	    return 0

    return 1   

def con(word):
    #No
    if word == u"ん":
        return 0
    

def note(conversation):
    m = MeCab.Tagger ("-Owakati")
    #encode_text = conversation.encode('utf-8')
    res = m.parseToNode(conversation)

    f = open("RB/data/symptom.txt")
    dic = f.readlines()
    f.close()

    box = []
    noun_box = []
    while res:
    	tmp = res.feature.decode('utf-8').split(",")
        print tmp[0], tmp[6]
        if tmp[0] == u'名詞':
	    if find_in_dic(dic, tmp[6]) == 0:
	        box.append(tmp[6])
	        noun_box.append(tmp[6])
        if tmp[0] == u'動詞' or tmp[0] == u'形容詞':
            box.append(tmp[6])
        if tmp[6].find(u"ない") != -1 or tmp[6].find(u"ん") != -1:
	    box.append(tmp[6])
        res = res.next



    dic_yes = []
    dic_no = []
    #文章単位で流すかどうかが問題
    for i in xrange(len(box)):
	#名刺以外はスキップ
	if not box[i] in noun_box:
	    continue
	for j in xrange(len(box)-i):
            if j > 10:
                break
            if con(box[j+i]) == 0:
                dic_no.append(box[i])
	    else:
		dic_yes.append(box[i])
	   

    dic_no = list(set(dic_no))
    dic_yes = list(set(dic_yes))

    for d in dic_no:
	print d
	dic_yes.remove(d)

    print '------------'
    for d in dic_yes:
	print d


if __name__ == '__main__':
    Qs = {
    "Q": "いつもより排便回数が多いですか",
    "Yes": "排便回数はいつもより多く、1日5回くらい",
    "No": "排便回数はいつもと変わらない",
    "Open": "排便回数は不明"
    }

    conversation = "くらっとするめまいということですが、今のご気分はいかがでしょうか。車椅子のままで良いのでお話を伺えますか大丈夫です「くらっとするめまい」は機能のいつ頃、何をしている時に、どのような症状をどこに感じたのか、詳しく教えてください。昨日の夜7時頃、晩ご飯の前に、椅子を座ってテレビのニュースを見て言いました。すると急に、ねの前が真っ暗になって、頭にくらっとるめまいを感じました。その時に、尿や便を漏らしていきませんでしたか。漏らしていませんでした。"

    se_conv =  split_conversation(conversation)
    note(conversation)
