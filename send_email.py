#Usually we import from liabraries that have been developed by other programmers, It makes our programming easier and more efficient.
#we dont need to download email message where it is already in libraries so we import emailmessage from email.message.
#ssl stands fir secure socket layer
#It helps to ensure that the data remains private and protected from unauthorized access#s.
#smtp stands for simple mail transfer protocol.
#email password is generated from google account where we can link our account with Vscode.py and get a password for this app.

from email.message import EmailMessage
import ssl
import smtplib
email_sender="dorjitshering952@gmail.com"
email_password="skzjhlixdvsmhbfu"
email_receiver="03230373.gcbs@rub.edu.bt"
#You can send your message to any gmail account users.
#Try using your email in email_receiver :)
subject = "Leave Application"
letter = """
   

To,
The module tutor,
Mrs.Kamal Archarya
Gedu College of Business Studies

Date: 28/9/23
        
Dear Sir,
With due respect,I want to say that I am not in a position to attend the class as i am suffering from fever and cold.
i am very honest and talented student where i haven't taken a single day off from my class for the last 3 months.
    
Therefor,kindly grant me leave to get
recover myself.
I shall be really thankful to you.

Thanking you,
        
    
Your Faithfully
Tshering Dorji(03230373)
BBI"c"
"""
#em is an object that i'm gonna use to write that Email message.
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(letter)
#to define the body we use set_content method().
context = ssl.create_default_context()
#we import ssl to keep an internet connection secure.
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
#We use smtplib to send email message
#So now we define the using email server as smtp.gmail.com and port 465
#while using with statment it ensures proper acquisition and release of resources, also helps in avoiding bugs and leaks by ensuring that code is completely executed.
#So we now run program to get an output.