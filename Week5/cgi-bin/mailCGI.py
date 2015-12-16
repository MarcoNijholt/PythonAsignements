#!C:\Python34\python.exe

# Import modules for CGI handling
import cgi, cgitb, smtplib

cgitb.enable()

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
email = form.getvalue('email')
body = form.getvalue('mailbody')
subject = form.getvalue('subject')

try:
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login("info@marconijholt.com", "<app specific gmail password here>")
    header = 'To:' + email + '\n' + 'From: ' + "info@marconijholt.com" + '\n' + 'Subject:' + subject + ' \n'
    msg = header + '\n '+ body +' \n\n'
    smtpserver.sendmail("info@marconijholt.com", email, msg)
    smtpserver.close()
except:
    print ("Content-type:text/html\r\n\r\n")
    print ("<html>")
    print ("<body>")
    print ("<p>Error sending email, please try again</p>")
    print ("</body>")
    print ("</html>")
else:
    print ("Content-type:text/html\r\n\r\n")
    print ("<html>")
    print ("<head>")
    print ("<title>Email Send!</title>")
    print ("</head>")
    print ("<body>")
    print ("<h2>Your email has been send</h2>")
    print ("</body>")
    print ("</html>")
