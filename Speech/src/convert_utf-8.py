#coding:utf-8
import json
import os,sys

def read_file(filename):
    file_path = param[1] + "/" + file
    if file_path.find("json") == -1:
        return ""
    print file_path
    f = open(file_path, 'r')
    jsonData = json.load(f)
    f.close()

    texts = ""
    try:
        num = len(jsonData["results"])
        for i in xrange(num):
            texts += jsonData["results"][i]["alternatives"][0]["transcript"]
        return texts
    except:
        f = open("Speech/data/ep_text/ep6_test1.wav.json", 'r')
        jsonData = json.load(f)
        f.close()
        num = len(jsonData["results"])
        for i in xrange(num):
            texts += jsonData["results"][i]["alternatives"][0]["transcript"]
        return texts


if __name__ == "__main__":
  param = sys.argv


  files = os.listdir(param[1])

  texts = ""
  for file in files:
      texts += read_file(file)

  print "-----"
  print texts
  print "-----"
  
  f = open("%s/scripts.txt"%param[1], "w")
  f.write(texts.encode("utf-8"))
  f.close()


