
#import module
import smtplib


#create smtp session
s = smtplib.SMTP("smtp.gmail.com", 587)

#start TLS for Security
s.starttls()


#authenticate
s.login("your-email-here@gmail.com", "Very-Secure-password-here")

#Message to Send
message = "message you want to send"

#send the email to:
string = "email1@gmail.com,email2@gmail.com,email3@gmail.com"

s.sendmail("your-email-her@gmail.com",string.split(','), message)

#close session
s.quit()



