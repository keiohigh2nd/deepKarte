#coding:utf-8
import json

f = open('view/cumu.json', 'r')
texts = f.read()
f.close()

fh = open('view/space_cumulativeLineChart.html', 'r')
html = fh.readlines()
fh.close()


fo = open('view/done_cumulativeLineChart.html', 'w')
i,j = 0,0
N = len(html)

for h in html:
	#fo.write(h)
	if int(h.find("cumulativeTestData")) != -1:
		if j == 1:
			fo.write(h)
			fo.write("return [")
			fo.write(texts)
			fo.write("];")
			
		else:
			fo.write(h)
		j += 1
	else:
		fo.write(h)

fo.close()
		

