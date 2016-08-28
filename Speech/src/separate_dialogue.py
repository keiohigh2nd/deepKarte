#coding:utf-8
import json, MeCab
import sys, os, random
import re

def return_texts(filename):
  f = open("Speech/data/%s"%filename, 'r')
  jsonData = json.load(f)
  f.close()

  num = len(jsonData["results"])
  tmp = ""
  for i in xrange(num):
        tmp += jsonData["results"][i]["alternatives"][0]["transcript"] 
  return tmp

def parse_text(text, m):
        encode_text = text.encode('utf-8')
        res = m.parse(encode_text)
        return res.decode('utf-8')


if __name__ == "__main__":
  param = sys.argv

  files = os.listdir("Speech/data")

  texts = ""
  for file in files:
    if int(file.find("json")) != -1:
      texts += return_texts(file)

  #Parsing won't help so fat
  #m = MeCab.Tagger ("-Owakati")
  #print parse_text(texts, m)


  separater = "すか"
  dialogue = texts.split(separater.decode('utf-8'))
  #for i in dialogue:
    #print i.encode('utf-8') + separater

  #Stop wordsで区切る方法
  num = len(texts)
  stop_words = "すか たか"
  start_words = "です"
 
  seped = re.split(u'すか|です|たか', texts)
  m = MeCab.Tagger ("-Owakati")

  rand_id = random.randint(0,100)  
  f = open("Speech/data/conversation_%s.txt"%rand_id, "w")
  for j in seped:
    f.write(j.encode("utf-8"))
    f.write("\n")
  f.close()

