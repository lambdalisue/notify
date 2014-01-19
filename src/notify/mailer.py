# coding=utf-8
"""
Mailer module
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'
import smtplib
from notify.compat import Header
from notify.compat import MIMEText
from notify.compat import formatdate

def console_debug(debug, output):
    if debug:
        print output

def create_message(from_addr, to_addr, subject, body, encoding=None):
    """
    Create message object for sending email

    Parameters
    ----------
    from_addr : string
        An email address used for 'From' attribute
    to_addr : string
        An email address used for 'To' attribute
    subject : string
        An email subject string
    body : string
        An email body string
    encoding : string
        An email encoding string (Default: utf8)

    Returns
    -------
    object
        An instance of email.mime.text.MIMEText
    """
    if encoding == "None":
        encoding = None
    msg = MIMEText(body, 'plain', encoding)
    msg['Subject'] = Header(subject, encoding)
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Date'] = formatdate()
    return msg

def send_email(msg, host='localhost', port=25,
         username=None, password=None,
         debug=False):
    """
    Send an email (via TLS when username and password are specified)

    Parameters
    ----------
    msg : object
        An instance of MIMEText. Create this with :func:`create_message`
        function.
    host : string
        A mail user agent host name (Default: localhost)
    port : int
        A mail user agent port number (Default: 25)
    username : string
        A username string used to login MUA via TLS authentication
    password : string
        A password string used to login MUA via TLS authentication
    debug : boolean
        True for displaying debug messages
    """
    console_debug(debug, "Create STMP instance...")
    s = smtplib.SMTP(host, port)
    if username and password:
        _console_debug(debug, "Identify ourseleves to the client...")
        s.ehlo()
        _console_debug(debug, "Start secure connection with tls encryption...")
        s.starttls()
        _console_debug(debug,
            "Re-identify ourselves as an encrypted connection...")
        s.ehlo()
        _console_debug(debug, "Login with specified username and password...")
        s.login(user, passwd)
    console_debug(debug, "Sending email from %s to %s..." % (
        msg['From'], msg['To']))
    s.sendmail(msg['From'], [msg['To']], msg.as_string())
    s.close()
