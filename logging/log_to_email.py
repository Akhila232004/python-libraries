# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Log to Email
#  Author       : Team Tinitiate
# ==============================================================================



import logging
import smtplib
from logging.handlers import SMTPHandler

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Set up email handler
smtp_handler = SMTPHandler(
    mailhost='smtp.example.com',
    fromaddr='sender@example.com',
    toaddrs=['recipient@example.com'],
    subject='Error occurred!',
    credentials=('username', 'password'),
    secure=(),
)
smtp_handler.setLevel(logging.ERROR)
logger.addHandler(smtp_handler)

# Test the logger
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
