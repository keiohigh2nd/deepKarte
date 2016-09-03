#coding:utf-8
import json
import os,sys

if __name__ == "__main__":
  param = sys.argv


  files = os.listdir(param[1])

  texts = ""
  for file in files:
      file_path = param[1] + "/" + file
      print file_path
      if file_path.find("json") == -1:
          continue

      f = open(file_path, 'r')
      jsonData = json.load(f)
      f.close()

      num = len(jsonData["results"])
      for i in xrange(num):
          texts += jsonData["results"][i]["alternatives"][0]["transcript"]
  print texts
  
  f = open("%s/scripts.txt"%param[1], "w")
  f.write(texts.encode("utf-8"))
  f.close()


