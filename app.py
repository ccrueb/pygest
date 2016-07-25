import smtplib
import os.path

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
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
msg = "YOUR MESSAGE!"
server.sendmail(email, email, msg)
server.quit()