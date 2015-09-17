#!/usr/bin/env python

############## UNREAD TITLE SEARCH  ##############
## searches email titles and returns the summary of targetted search


import feedparser		# imports feedparser to parse XML feed
import subprocess
import smtplib
import socket
import time
from email.mime.text import MIMEText
import datetime
import urllib2

to = '5512211489@tmomail.net'
user = 'notifaine@gmail.com'
pwd = '***'

smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(user, pwd)
today = datetime.date.today()

newmails = feedparser.parse("https://" + user + ":" + pwd + "@mail.google.com/gmail/feed/atom").entries
for i in newmails:		#for loop itterates through newmails feed
   # print str(i.title)
    if str(i.title)=="bbb":
        print str(i.summary)		# uncomment to print out each title of unread emails
        msg = MIMEText('a message from python script')
        msg['Subject'] = 'you got some bbb'
        msg['From'] = user
        msg['To'] = to
        smtpserver.sendmail(user, [to], msg.as_string())
        smtpserver.quit()

    else:
        print str('no bbb')

time.sleep(60)
