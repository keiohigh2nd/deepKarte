# -*- coding: utf-8 -*-
def hasKanji(s):
  #Returns True if string s contains a Kanji, False if not.
  kanji = []
  for c in s:
   if (((ord(c)&0xff00) == 0x3000) or (0x4e00 <= ((ord(c)&0xff00) <=0x9f00))):
	continue
   else:
	print c
     	kanji.append(c)
  return kanji

if __name__ == "__main__":
	pass
