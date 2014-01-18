# coding=utf-8
"""
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'
import time
import datetime
import keyring
from notify.executor import call
from notify.executor import get_command_str
from notify.mailer import create_message
from notify.mailer import send_email

EMAIL_BODY = """
%(status)s: %(prog)s

Start: %(stdtime)s
End:   %(endtime)s
Time:  %(tdelta)s sec
Clock: %(cdelta)s sec

Output:

%(output)s
"""

def call_and_notificate(args, opts):
    """
    Execute specified arguments and send notification email

    Parameters
    ----------
    args : list
        A execution command/arguments list
    opts : object
        A option instance
    """
    # store starttime
    stctime = time.clock()
    stttime = time.time()
    stdtime = datetime.datetime.now()
    # call subprocess
    exit_code, output = call(args)
    # calculate delta
    cdelta = time.clock() - stctime
    tdelta = time.time() - stttime
    endtime = datetime.datetime.now()
    # create email body
    body = EMAIL_BODY % {
        'prog': get_command_str(args),
        'status': 'Success' if exit_code == 0 else 'Fail',
        'stdtime': stdtime,
        'endtime': endtime,
        'tdelta': tdelta,
        'cdelta': cdelta,
        'output': output,
    }
    # create email subject
    subject = opts.subject % {
        'prog': get_command_str(args),
        'status': 'success' if exit_code == 0 else 'fail',
    }
    # create email message
    msg = create_message(opts.from_addr,
                         opts.to_addr,
                         subject,
                         body,
                         opts.encoding)
    # obtain password from keyring
    password = keyring.get_password('notify', 'authentication')
    # send email
    send_email(msg, opts.host, opts.port, opts.username, password)
