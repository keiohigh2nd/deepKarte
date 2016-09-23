import os, sys, time
sys.path.append('src')
sys.path.append('view')
import search
import bulk_data_for_sunburst, bulk_data_for_chart, bulk_data_for_sunburst
from selenium import webdriver

def sorted_ls(path):
    print path
    mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
    files = list(sorted(os.listdir(path), key=mtime, reverse=True))
    return path + "/" + files[0]

def generate_view():
    bulk_data_for_sunburst.run()
    bulk_data_for_chart.run()
    bulk_data_for_sunburst.run()

if __name__ == "__main__":
    argvs = sys.argv
    if len(argvs) < 1:
       print "You need decoder directory"

    driver = webdriver.Chrome("shellscript/chromedriver")
    #driver.get('file:///Users/keiohigh2nd/deepKarte/view/ATE.html')
    driver.get("file:///Users/keiohigh2nd/deepKarte/view/find_similar_patient.html")

    while True: 
         updated_file = sorted_ls(argvs[1])
         search.run(updated_file)  
         generate_view()
         time.sleep(5) # Let the user actually see something!
         driver.refresh()

