#!/usr/bin/env python
# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
import codecs, json, sys, re
import numpy as np


if __name__ == "__main__":
  param = sys.argv

  f = open(param[1], "r")
  data = json.load(f)
  print data["others"]
  others = re.split(u'ああ', data["others"]) 

  num_history = np.arange(len(others)) #for文章を回すために必要
  env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
  tmp = env.get_template('Speech_UI/text_box_index.html')
  #html = tmp.render(contents=["1", "2", "3"], prime=prime.decode("utf-8"), life=life.decode("utf-8"))
  html = tmp.render(contents=num_history, history=others, prime=data["symptom"], life=data["life"], alle=data["alle"], pharm=data["medication"], family=data["family"], past = data["history"] )

  f = codecs.open('Speech_UI/o_text_box_index.html', 'w', 'utf-8')
  f.write(html)
  f.close()


