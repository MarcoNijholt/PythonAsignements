__author__ = 'marco'
#!C:\Python34\python.exe
import cgitb
cgitb.enable()
print ('Status: 200 OK')
print ('Content-type: text/html')
print ()

print ('<HTML><HEAD><TITLE>Python Sample CGI</TITLE></HEAD>')
print ('<BODY>')
print ('<H1>This is a header</H1>')

print ('<p>') #this is a comment
print ('See this is just like most other HTML')
print ('<br>')
print ('</BODY>')
