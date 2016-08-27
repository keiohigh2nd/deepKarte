#coding:utf-8
import json
import sys

if __name__ == "__main__":
  param = sys.argv

  f = open(param[1], 'r')
  #f = open('test_wav.json', 'r')
  jsonData = json.load(f)
  f.close()

  num = len(jsonData["results"])
  for i in xrange(num):
  	print jsonData["results"][i]["alternatives"][0]["transcript"]
