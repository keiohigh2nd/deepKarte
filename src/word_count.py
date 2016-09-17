# -*- coding: utf-8 -*-
import nltk
from nltk.corpus.reader import *
from nltk.corpus.reader.util import *
from nltk.text import Text
from chasen import *

def run(filename):
  """
  f = open(filename)
  texts = f.read()
  f.close()
  """
  genpaku = ChasenCorpusReader('/path/to/jeita/corpus/', filename, encoding='utf-8')
  genpaku_vocab = set(w for w in genpaku.words() if re.match(ur"^[ぁ-んーァ-ンー\u4e00-\u9FFF]+$", w))
  genpaku_t = Text(genpaku.words())
  genpaku_wfd = FreqDist(genpaku_t)

  genpaku_wfd.tabulate(10)

if __name__ == "__main__":
  import sys
  argvs = sys.argv  
  run(argvs[1])
