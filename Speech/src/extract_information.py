#coding:utf-8
import json
import sys

if __name__ == "__main__":
  param = sys.argv

  f = open('Speech/data/conversation_20.txt', 'r')
  lines = f.readlines()
  f.close()

  for line in lines:
    print line.strip("\n")
