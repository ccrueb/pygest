import smtplib
 
# Read config file
config = open('.config.txt', 'r')
email = config.readline().rstrip()
password = config.readline().rstrip()

# Send email
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
msg = "YOUR MESSAGE!"
server.sendmail(email, email, msg)
server.quit()