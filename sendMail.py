import smtplib
from email.mime.text import MIMEText

def sendMail_successfully(recipient):
    gmail_user = 'justin0010523@gmail.com'

    msg = MIMEText('Your paper has been submitted into repository successfully!')
    msg['Subject'] = 'Project testing!'
    msg['From'] = gmail_user
    msg['To'] = recipient

    smtpssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpssl.ehlo()
    smtpssl.login(gmail_user, 'ofregavbnnsyavom')
    smtpssl.send_message(msg)
    smtpssl.quit()
    return print('Email has been sent!')

def sendMail_unsuccessfully(recipient):
    gmail_user = 'justin0010523@gmail.com'

    msg = MIMEText('Your paper has been rejected!')
    msg['Subject'] = 'Project testing!'
    msg['From'] = gmail_user
    msg['To'] = recipient

    smtpssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpssl.ehlo()
    smtpssl.login(gmail_user, 'ofregavbnnsyavom')
    smtpssl.send_message(msg)
    smtpssl.quit()
    return print('Email has been sent!')