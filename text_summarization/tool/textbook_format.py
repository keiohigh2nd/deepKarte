import json,sys,random

def generate_training_data(f_conversation):
  #Conversation
  f = open(f_conversation, "r")
  texts = f.read()
  f.close()

  print texts
  f = open("text_summarization/Raw_data/Formatted_Dataset_textbook.tsv", "w")

  #Traning Data for textsum 
  print texts[1]
  for line in texts:
	tmp = line.split(",")  
	print tmp[0]
	f.write(tmp[0])
	f.write(tmp[1])
  	f.write("\t")
  	f.write(tmp[2])
  f.write("\n")
  f.close()



if __name__ == "__main__":
  params = sys.argv
  generate_training_data(params[1])


