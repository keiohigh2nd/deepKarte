#!/usr/bin/env python
# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
import codecs
import numpy as np


prime = "胸が痛い"
life = "お酒は毎日500ml"
history = [ "昔、心筋梗塞にかかったことがある".decode("utf-8"), "登坂時の突然の胸痛を主訴に3日前に緊急入院した．".decode("utf-8"), "学校の健康診断で心雑音を指摘され来院した．".decode("utf-8") ]
alle = "花粉、猫"
pharm = "ループ利尿薬、メルドバ"
family = "父は突然死、祖母が乳がん"
past = "特になし"

num_history = np.arange(len(history))
env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
tmp = env.get_template('Speech_UI/index.html')
#html = tmp.render(contents=["1", "2", "3"], prime=prime.decode("utf-8"), life=life.decode("utf-8"))
html = tmp.render(contents=num_history, history=history, prime=prime.decode("utf-8"), life=life.decode("utf-8"), alle=alle.decode("utf-8"), pharm=pharm.decode("utf-8"), family=family.decode("utf-8"), past = past.decode("utf-8") )

f = codecs.open('Speech_UI/o_index.html', 'w', 'utf-8')
f.write(html)
f.close()


