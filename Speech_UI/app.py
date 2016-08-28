#!/usr/bin/env python
# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
import codecs


labels = [1, 2, 3]


env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
#ATE部分
tmpATE = env.get_template('Speech_UI/index.html')
htmlATE = tmpATE.render(contents=["1", "2", "3"])

f = codecs.open('Speech_UI/o_index.html', 'w', 'utf-8')
f.write(htmlATE)
f.close()


