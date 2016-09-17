import MeCab

def run(filename):
  f = open(filename)
  texts = f.readlines()
  f.close()


  tagger = MeCab.Tagger("-Owakati")
  tmp = filename.split("/")[-1]
  f = open("text_summarization/train/NoQA_%s"%tmp, "w")
  for t in texts:
    line = t.strip("\r\n").split("\t")
    l0 = tagger.parse(line[0])
    f.write(l0)
    f.write("\t")
    l1 = tagger.parse(line[1])
    f.write(l1)
    f.write("\n")
  f.close()

if __name__ == "__main__":
  import sys
  argvs = sys.argv
  run(argvs[1])
