![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# Email
* Python provides the `smtplib` module to send emails.
* Provisions to send email, emails with attachments and HTML emails. 

## Sending Plain Text Email
```python
import smtplib

# Import other required modules
from email.mime.multipart import MIMEMultipart

# For configurations
import configparser
import os

# Load the configuration from file
config = configparser.ConfigParser()
config.read('C:/tinitiate/config.ini')

# Get the Gmail username and password from the configuration
gmail_user = config.get('Gmail', 'username')
gmail_password = config.get('Gmail', 'password')

# Create SENDER and RECEIVER
sender    = 'tinitiate.training@gmail.com'
receiver  = ['tinitiate@gmail.com', 'tinitiate.training@gmail.com']

# Create message object
msg = MIMEMultipart('alternative')

msg['From']    = sender 
msg['To'] = ", ".join(receiver)
msg['Subject'] = "This is a TINITIATE test EMAIL"

s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.ehlo()
s.login(gmail_user, gmail_password)

# sendmail() function requires 3 arguments: sender, recipient and message
s.sendmail(sender, receiver, msg.as_string())

# Close SMTP connection once email is sent
s.quit()
```

## Sending HTML Email
```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import configparser

# Load the configuration from file
config = configparser.ConfigParser()
config.read('C:/tinitiate/config.ini')

# Get the Gmail username and password from the configuration
gmail_user = config.get('Gmail', 'username')
gmail_password = config.get('Gmail', 'password')

# Create SENDER and RECEIVER
sender = 'tinitiate.training@gmail.com'
receiver = ['tinitiate@gmail.com', 'tinitiate.training@gmail.com']

# Create message object
msg = MIMEMultipart('alternative')
msg['From'] = sender 
msg['To'] = ", ".join(receiver)
msg['Subject'] = "This is a TINITIATE test EMAIL"

# Create the body of the message with plain-text and HTML
plain_text = "This is plain text"

# Create HTML text
html_text = """\
<html>
  <body>
    <h1>This is a TEST EMAIL FROM TINITIATE </h1>
    <p>
     Welcome to Python training from TINITATE.COM
    </p>
  </body>
</html>
"""

# CREATE MIME types for text/plain and text/html.
plain_message = MIMEText(plain_text, 'plain')
html_message = MIMEText(html_text, 'html')

# Attach them to the message
msg.attach(plain_message)
msg.attach(html_message)

s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.ehlo()
s.login(gmail_user, gmail_password)

# sendmail function requires 3 arguments: sender, recipient and message
s.sendmail(sender, receiver, msg.as_string())

# Close SMTP connection once email is sent
s.quit()
```

## Sending Email Attachments
```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import configparser
import os

data_dir ='C:/tinitiate/uploads/'
# Load the configuration from file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the Gmail username and password from the configuration
gmail_user = config.get('Gmail', 'username')
gmail_password = config.get('Gmail', 'password')

# Create SENDER and RECEIVER
attachment_sender = 'tinitiate.training@gmail.com'
attachment_receiver = ['tinitiate@gmail.com', 'tinitiate.training@gmail.com']

# Create message object
attachment_msg = MIMEMultipart()

attachment_msg['From']    = attachment_sender
attachment_msg['To']      =  ", ".join(attachment_receiver)
attachment_msg['Subject'] = 'Python Attachment test email'

# Files LIST
files = [data_dir+"myfile.txt",data_dir+"image1.gif",data_dir+"music1.mp3"]

for f in files:
  part = MIMEBase('application', "octet-stream")
  part.set_payload( open(f,"rb").read() )
  encoders.encode_base64(part)
  part.add_header('Content-Disposition','attachment; filename="{0}"'.format(os.path.basename(f)))
  attachment_msg.attach(part)

# Create an SMTP connection
s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.login(gmail_user, gmail_password)
s.ehlo()
s.sendmail(attachment_sender, attachment_receiver, attachment_msg.as_string())
s.quit()
```

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|