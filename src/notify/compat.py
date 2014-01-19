# coding=utf-8
"""
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'
try:
    import keyring
except ImportError:
    import os
    import textwrap
    import notify.utils.terminalsize as ts
    from notify.utils.plaintext_keyring import PlaintextKeyring
    from notify.conf import get_user_config_filename
    w = ts.get_terminal_size()[0] - 3
    if w > 70:
        w = 67
    print
    print "||"
    print "||", "~" * w
    print "||", "SECURITY WARNING".center(w)
    print "||", "~" * w
    print "||"
    for line in textwrap.wrap("'keyring' library is not installed. "
                              "notify will use plaintext way to store "
                              "authentication password.", width=w):
        print "||", line
    print "||"
    for line in textwrap.wrap("If you are going to use mail user agent which "
                              "require authentication, it is strongly "
                              "recommended to install 'keyring' with 'pip' "
                              "like :", width=w):
        print "||", line
    print "||" 
    print "||", "  $ pip install keyring"
    print "||"
    print
    filename = os.path.splitext(get_user_config_filename())[0]
    filename = filename + ".keyring"
    keyring = PlaintextKeyring(filename)

try:
    from io import StringIO
except ImportError:
    from StringIO import StringIO

try:
    from email.header import Header
    from email.mime.text import MIMEText
    from email.utils import formatdate
except ImportError:
    from email.Header import Header
    from email.MIMEText import MIMEText
    from email.Utils import formatdate
