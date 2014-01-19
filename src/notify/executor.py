# coding=utf-8
"""
A terminal command executor module
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'
import sys
import subprocess
from notify.compat import StringIO

if sys.version_info >= (3, 0):
    # i'm not sure the encoding should be utf-8 or not
    force_unicode = lambda x: str(x, 'utf-8')
else:
    force_unicode = unicode

def call(args):
    """
    Call terminal command and return exit_code and stdout

    Parameters
    ----------
    args : list
        A command and arguments list

    Returns
    -------
    list : [exit_code, stdout]
        exit_code indicate the exit code of the command and stdout indicate the
        output of the command
    """
    b = StringIO()
    p = subprocess.Popen(args,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
    # old python has bug in p.stdout, so the following little
    # hack is required.
    for stdout in iter(p.stdout.readline, ''):
        if len(stdout) == 0:
            break
        stdout = force_unicode(stdout)
        b.write(stdout)
        sys.stdout.write(stdout)
        sys.stdout.flush()
    buf = b.getvalue()
    p.stdout.close()
    return p.returncode or 0, buf

def get_command_str(args):
    """
    Get terminal command string from list of command and arguments

    Parameters
    ----------
    args : list
        A command and arguments list

    Returns
    -------
    str
        A string indicate terminal command
    """
    single_quote = "'"
    double_quote = '"'
    for i, value in enumerate(args):
        if " " in value and double_quote not in value:
            args[i] = '"%s"' % value
        elif " " in value and single_quote not in value:
            args[i] = "'%s'" % value
    return " ".join(args)
