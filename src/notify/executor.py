# coding=utf-8
"""
A terminal command executor module
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'

import io
import sys
import subprocess

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
    b = io.BytesIO()
    p = subprocess.Popen(args,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    while p.returncode is None:
        stdout = p.communicate()[0]
        # output to stdout and buffer
        sys.stdout.write(stdout)
        b.write(stdout)
    # return exit_code and buffer
    return p.returncode, b.getvalue()

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
