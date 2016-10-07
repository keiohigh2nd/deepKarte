# -*- coding: utf-8 -*-
import json, MeCab, sys, os, random
import re


def split_conversation(conversatioin):
    seped = re.split('すか|です|たか|した', conversation)
    return seped


def find_in_dic(dic, word):
    for d in dic:
	#部分一致
        if d.find(word.encode("utf-8")) != -1:
	#完全一致
        #if d == word :
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
    im_box = []
    ta_box = []
    while res:
    	tmp = res.feature.decode('utf-8').split(",")
        box.append(tmp[6])
        if tmp[0] == u'名詞':
	    if find_in_dic(dic, tmp[6]) == 0:
	        #box.append(tmp[6])
	        im_box.append(tmp[6])
        if tmp[6] == u'た':
	    ta_box.append(tmp[6])

        #if tmp[0] == u'動詞' or tmp[0] == u'形容詞':
            #im_box.append(tmp[6])
        #if tmp[6].find(u"ない") != -1 or tmp[6].find(u"ん") != -1:
	    #im_box.append(tmp[6])
        res = res.next

    print conversation

    im_box = list(set(im_box))
    print "-----------"
    for i in im_box:
        print i

    memo = []
    conversation = conversation.decode("utf-8")
    for i in xrange(len(im_box)):
        start = conversation.find(im_box[i])
        #start = conversation.find(im_box[i].encode("utf-8"))
        for j in xrange(len(conversation)-start):
                #print conversation.decode("utf-8")[1:10]
                if j < 4:
		    continue
		if conversation[start+j] == u"た":
             	    memo.append(conversation[start:start+j+1])  
		    break


    memo = list(set(memo))
    f = open("RB/output/sum.txt", "w")
    for m in memo:
        if m:
            f.write(m.encode("utf-8"))
            f.write("\n")
    f.close()

if __name__ == '__main__':
    import sys
    argvs = sys.argv
    f = open(argvs[1])
    conversation = f.read()
    f.close()

    note(conversation)
