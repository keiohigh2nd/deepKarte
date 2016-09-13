import random,json

def save(a,b,c,d,e,f,g):
  dict = {
		"prime": a.encode("utf-8"),
		"life": b.encode("utf-8"),
		"past": c.encode("utf-8"),
		"family": d.encode("utf-8"),
		"alle": e.encode("utf-8"),
		"pharm": f.encode("utf-8"),
		"history": g.encode("utf-8")
  }
  tmp = random.randint(0,100)
  f = open("flask/learn/%s.txt"%tmp, "w")
  json.dump(dict, f, ensure_ascii=False)


