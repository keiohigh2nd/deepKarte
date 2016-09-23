#coding:utf-8
import json, sys

def run():
    json_file = "view/tsunburst.json"
    space_html = "view/space_sunburst.html"
    result_html = "view/done_sunburst.html"

    f = open(json_file, 'r')
    texts = f.read()
    f.close()

    fh = open(space_html, 'r')
    html = fh.readlines()
    fh.close()


    fo = open(result_html, 'w')
    i,j = 0,0
    N = len(html)

    for h in html:
        #fo.write(h)
        if int(h.find("getData")) != -1:
                if j == 1:
                        fo.write(h)
                        fo.write("return [")
                        fo.write(texts)
                        fo.write("];")
                        
                else:
                        fo.write(h)
                j += 1
        else:
                fo.write(h)

    fo.close()


if __name__ == '__main__':

    run()

    #json_file = sys.argv[1]
    #space_html = sys.argv[2]
    #result_html = sys.argv[3]

