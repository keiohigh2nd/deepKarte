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
  #encode_text = text.encode('utf-8')
  #res = m.parse(encode_text)
  res = m.parse(text)
  return res.decode('utf-8')

def find_symptom(text):
  keywords = ["今日","たか"]
  if text.find(keywords[0]) != -1 and text.find(keywords[0]) != -1:
    return 1 
  else:
    return 0

def find_life(text):
  keywords = ["酒","たばこ","すか"]
  if text.find(keywords[0]) != -1 and text.find(keywords[1]) != -1:
    return 1 
  else:
    return 0

def find_history(text):
  keywords = ["今まで", "すか"]
  if text.find(keywords[0]) != -1 and text.find(keywords[1]) != -1:
    return 1
  else:
    return 0

def find_family(text):
  keywords = ["家族"]
  if text.find(keywords[0]) != -1:
    return 1
  else:
    return 0

def find_medication(text):
  keywords = ["薬"]
  if text.find(keywords[0]) != -1:
    return 1
  else:
    return 0

def find_alle(text):
  keywords = ["アレルギー"]
  if text.find(keywords[0]) != -1:
    return 1
  else:
    return 0


if __name__ == "__main__":
  param = sys.argv

  f = open(param[1], "r")
  texts = f.read()
  f.close()

  #Parsing won't help so fat
  m = MeCab.Tagger ("-Owakati")
  #print parse_text(texts, m)

  #for i in dialogue:
    #print i.encode('utf-8') + separater

  #Stop wordsで区切る方法
  num = len(texts)
  stop_words = "すか たか"
  start_words = "です"
 
  seped = re.split('すか|です|たか|した', texts)
  #seped = re.split('すか|たか', texts)
  m = MeCab.Tagger ("-Owakati")

  rand_id = random.randint(0,100)  
  #f = open("Speech/data/conversation_%s.txt"%rand_id, "w")
  
  symptom = "" 
  life = "" 
  family = "" 
  medication = "" 
  history = "" 
  alle = "" 
  others = ""
  for j in xrange(len(seped)):
    if find_symptom(seped[j]) == 1:
      print seped[j]
      print seped[j+1]
      symptom = seped[j+1]
      continue
    if find_life(seped[j]) == 1: 
      print seped[j]
      print seped[j+1]
      life = seped[j+1]
      continue
    if find_history(seped[j]) == 1: 
      print seped[j]
      print seped[j+1]
      history = seped[j+1]
      continue
    if find_family(seped[j]) == 1:
      print seped[j]
      print seped[j+1]
      family = seped[j+1]
      continue
    if find_medication(seped[j]) == 1:
      print seped[j]
      print seped[j+1]
      medication = seped[j+1]
      continue
    if find_alle(seped[j]) == 1:
      print seped[j]
      print seped[j+1]
      alle = seped[j+1]
      continue

    others += seped[j]+"ああ"  

  dict = {
	"symptom" : symptom,
	"life" : life,
	"history": history,
	"family": family,
	"alle": alle,
	"medication": medication,
	"others": others
  }
 
  ep = param[1].split("/")[-2]
  f = open("Speech/karte/karte_%s.json"%ep, "w")
  json.dump(dict, f, ensure_ascii=False)
