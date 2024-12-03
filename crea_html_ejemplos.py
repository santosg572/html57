d1 = '''<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body> \n
'''

h1 = "<h1>My First Heading</h1>\n"

r1 = ' <p><a href="http://192.168.56.10/HTML_Examples/abbr.html"> abbr </a></p>\n'

d2 = '''
</body>
</html>
'''

filin = open("dir_html.txt", 'r')
datos = filin.readlines()
filin.close()

fil = open("html_ejemplos.html", 'w')

fil.write(d1)
fil.write(h1)

for ss in datos:
  ss = ss.replace('\n','')
  print(ss)
  rr = ' <p><a href="http://192.168.56.10/HTML_Examples/' + ss + '"> ' + ss + ' </a></p>\n'
  fil.write(rr)

fil.write(d2)

fil.close()



