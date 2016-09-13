# coding: utf-8
import random
import save_changes
from flask import Flask, jsonify, render_template, request
from flask_bootstrap import Bootstrap
app = Flask(__name__) 
Bootstrap(app)

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a')
    b = request.args.get('b')
    c = request.args.get('c')
    d = request.args.get('d')
    e = request.args.get('e')
    f = request.args.get('f')
    g = request.args.get('g')
    save_changes.save(a,b,c,d,e,f,g)
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
