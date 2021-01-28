from smtplib import SMTP
import datetime

debuglevel = 0

smtp = SMTP()
smtp.set_debuglevel( debuglevel )
smtp.connect("email-smtp.us-east-2.amazonaws.com", 25 )
smtp.login( 'AKIA5WP7FIBIGAY2H5GM', 'BOX2WvzD2uzn6X4ug+Xx1+iXCYXdboYqyXKaxEUYkcmm' )


from_addr = "rashidhamid139@gmail.com"
to_addr = "rashid@cirruslabs.io"

subj = "hello"
date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )

message_text = "Hello\nThis is a mail from your server\n\nBye\n"

msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( from_addr, to_addr, subj, date, message_text )

print(msg)
smtp.sendmail(from_addr, to_addr, msg)
smtp.quit()