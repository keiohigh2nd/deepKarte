#!/usr/bin/env python
# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
import codecs, json, sys, re
import numpy as np

def guess_autoescape(template_name):
    if template_name is None or '.' not in template_name:
        return False
    ext = template_name.rsplit('.', 1)[1]
    return ext in ('html', 'htm', 'xml')

if __name__ == "__main__":
  param = sys.argv

  f = open(param[1], "r")
  texts = f.read()
  f.close()
  
  env = Environment(loader=FileSystemLoader('./', encoding='utf8'), autoescape=guess_autoescape,extensions=['jinja2.ext.autoescape'])
  tmp = env.get_template('flask/templates/space_index.html')
  #html = tmp.render(contents=["1", "2", "3"], prime=prime.decode("utf-8"), life=life.decode("utf-8"))
  html = tmp.render(history=texts.decode("utf-8") )

  f = codecs.open('flask/templates/oindex.html', 'w', 'utf-8')
  f.write(html)
  f.close()


