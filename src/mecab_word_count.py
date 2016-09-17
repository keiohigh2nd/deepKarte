# -*- coding: utf-8 -*-
from collections import Counter
import codecs, re
import json

import MeCab

def run(filename):
  # バッドノウハウ感あるけど、出力結果をリダイレクトしたいし
  import sys

  # codecsはunicodeを返す
  # 一行目に余計な記述があってだるいしテストコードだし面倒なので事前に消しておこう
  f = codecs.open(filename, 'r', "utf-8")
  #f = open(filename, 'r')
  texts = f.read()
  print texts
  f.close()
  # Mecabはstr型しか受け付けないのでエンコード

  tagger = MeCab.Tagger('-Ochasen')
  texts = texts.encode("utf-8")

  node = tagger.parseToNode(texts)

  counter = Counter()
  while node:
      word = node.surface.decode('utf-8')
      if re.match(ur"^[ぁ-んーァ-ンー\u4e00-\u9FFF]+$", word) != None:
      #if len(word) != 1:
        counter[word] += 1
      node = node.next

  f = open("text_summarization/data/jp_vocab", "w")
  for word, cnt in counter.most_common():
     f.write(word.encode("utf-8"))
     f.write(" ")
     f.write(str(cnt))
     f.write("\n")      
     print word, cnt
  f.close()      

if __name__ == "__main__":
  import sys
  argvs = sys.argv  
  run(argvs[1])
