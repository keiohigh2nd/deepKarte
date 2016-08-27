#coding:utf-8
import json, MeCab
import sys, os

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

  print texts

  #Parsing won't help so fat
  #m = MeCab.Tagger ("-Owakati")
  #print parse_text(texts, m)


  separater = "すか"
  dialogue = texts.split(separater.decode('utf-8'))
  for i in dialogue:
    print i.encode('utf-8') + separater

  #Stop wordsで区切る方法
  num = len(texts)
  stop_words = ["すか","たか"]
  for i in xrange(num):
    try:
      tmp = texts[i] + texts[i+1]
    except:
      pass 

