# -*- encoding: utf-8 -*-
import sys
import codecs

if __name__ == "__main__":
        argvs = sys.argv
        argc = len(argvs)
        if (argc != 3):
                print 'Usage: # python %s Input_FileName Output_FileName' % argvs[0]
                quit()

        fin_name = argvs[1]
        fout_name = argvs[2]

        fin = codecs.open(fin_name, "r", "utf-8")
        fout = codecs.open(fout_name, "w", "utf-8")
        for line in fin:
                fout.write(line)
        fin.close()
        fout.close()
