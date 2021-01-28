import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text  import MIMEText

#AWS configuration.
host        =   "email-smtp.us-east-2.amazonaws.com"
username    =   "AKIA5WP7FIBIGAY2H5GM"
password    =   "BOX2WvzD2uzn6X4ug+Xx1+iXCYXdboYqyXKaxEUYkcmm"
port        =   465

def email( f ):
    def f2( subject ):
        msg = MIMEMultipart( 'alternate' )
        msg['Subject'] = subject
        msg['From']     = "rashidhamid139@gmail.com"
        msg['To']       = "rashid@cirruslabs.io"


        text = f()

        mime_text = MIMEText( text, 'plain' )
        msg.attach( mime_text )

        s   = smtplib.SMTP( host, port )
        s.starttls()
        s.login(username, password)
        s.send_message( msg )
        s.quit()

    return f2


@email
def foo():
    return "Hello WOrld"

foo( 'My Test')


