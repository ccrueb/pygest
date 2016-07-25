import smtplib
import os.path
import datetime
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

mydate = datetime.datetime.now()

# Check if config exists
if(not os.path.isfile('.config.txt')):
    email = raw_input("Enter your gmail account: ")
    password = raw_input("Enter your password: ")
    config = open('.config.txt', 'w')
    config.write(email+'\n'+password)
    config.close()
else:
    config = open('.config.txt', 'r')
    email = config.readline().rstrip()
    password = config.readline().rstrip()
    config.close()

# Send email
fromaddr = email
toaddr = email
msg = MIMEMultipart()
msg['From'] = "PyGest"
msg['To'] = toaddr
msg['Subject'] = "Daily PyGest: " + mydate.strftime("%b %d")
 
body = "YOUR MESSAGE HERE"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, password)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()