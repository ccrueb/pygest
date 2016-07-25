import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("email", "pass")
 
msg = "YOUR MESSAGE!"
server.sendmail("email", "email", msg)
server.quit()