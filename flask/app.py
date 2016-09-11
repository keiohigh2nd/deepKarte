# coding: utf-8
import random
from flask import Flask, jsonify, render_template, request
app = Flask(__name__) 

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a')
    b = request.args.get('b')
    print a
    print b
    tmp = random.randint(0,100)
    f = open("flask/learn/%s.txt"%tmp, "w")
    f.write(a.encode("utf-8"))
    f.close()
    return 0

@app.route('/')
def index():
    return render_template('index.html')

#ここがサーバーサイドからクライアントサイドへなにかを渡すときのポイントになります。

@app.route("/ate") 
def ate():
   message = 'sample_string'
   return render_template('ATE.html', message=message)

if __name__ == "__main__":
    app.run()
