__author__ = 'Alex'

#!/usr/bin/python

import smtplib
import sys

if __name__=='__main__':
   print "Enter smtp server address:"
   smtp_address = sys.stdin.readline().strip('\n')
   print "Enter smtp server port:"
   smtp_port = int(sys.stdin.readline().strip('\n'))
   print "Enter sender e-mail:"
   sender = sys.stdin.readline().strip('\n')
   print "Enter recipients (comma separated):"
   receivers = sys.stdin.readline().strip('\n').split(',')
   print "Enter password:"
   password = sys.stdin.readline().strip('\n')
   print "Enter message:"
   message = sys.stdin.readline().strip('\n')

   message = "From: %s\n" % sender +\
       "To: %s\n" % receivers[0] +\
       "Subject: Test message\n" +\
       "\n" +\
       message

   smtpObj = smtplib.SMTP(smtp_address, smtp_port)
   smtpObj.ehlo()
   smtpObj.starttls()
   smtpObj.ehlo()
   smtpObj.login(sender, password)
   smtpObj.sendmail(sender, receivers, message)
   print "Successfully sent email"