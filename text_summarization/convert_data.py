import json,sys,random

def generate_training_data(f_conversation, f_abst):
  #Conversation
  f = open(f_conversation, "r")
  texts = f.read()
  f.close()

  #Abstract
  f = open(f_abst, "r")
  jsonData = json.load(f, "utf-8")
  f.close()

  #Traning Data for textsum 
  tmp = random.randint(0,100)
  f = open("text_summarization/train/sample_%s.txt"%tmp, "w")
  f.write(texts)
  f.write("\t")
  f.write(jsonData["history"].encode("utf-8"))
  f.write("\n")
  f.close() 

if __name__ == "__main__":
  params = sys.argv
  generate_training_data(params[1], params[2])
  
