
f = open("flask/templates/oindex.html")
lines = f.readlines()
f.close()

f = open("flask/templates/index.html", "w")

i = 0
for line in lines:
  if i == 4:
    print line
    f.write(line)
    f.write("var $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};")
    f.write("\n")
  else:
    f.write(line)
  i += 1
f.close()
