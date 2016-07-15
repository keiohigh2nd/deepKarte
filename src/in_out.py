# -*- coding: utf-8 -*-
import json

def read_json(filename):
        f = open(filename, 'r')
        jsonData = json.load(f,"utf-8")
        text = json.dumps(jsonData)
        f.close()
        return text, jsonData

def parse_text(text, m):
        encode_text = text.encode('utf-8')
        res = m.parse(encode_text)
        return res.decode('utf-8')



