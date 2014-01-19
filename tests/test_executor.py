#!/usr/bin/env python
# coding=utf-8
from nose.tools import *
from mock import MagicMock

from notify.executor import call
from notify.executor import get_command_str

def test_command_str_type1():
    """
    get_command_str
    """
    args = ['echo', 'foo', 'bar', 'hoge']
    eq_(get_command_str(args),
        "echo foo bar hoge")

def test_command_str_type2():
    """
    get_command_str with space contains arguments
    """
    args = ['echo', 'foo bar', 'bar', 'hoge']
    eq_(get_command_str(args),
        "echo \"foo bar\" bar hoge")

def test_command_str_type3():
    """
    get_command_str with space and double quotation contains arguments
    """
    args = ['echo', 'foo "bar" hoge', 'bar', 'hoge']
    eq_(get_command_str(args),
        "echo 'foo \"bar\" hoge' bar hoge")

def test_command_str_type4():
    """
    get_command_str with space and single quotation contains arguments
    """
    args = ['echo', 'foo \'bar\' hoge', 'bar', 'hoge']
    eq_(get_command_str(args),
        "echo \"foo 'bar' hoge\" bar hoge")

def test_call():
    import os
    args = ['python', os.path.abspath(__file__), 'subprocess']
    exit_code, output = call(args)
    eq_(output, "0\n1\n2\n3\n4\n")

def run_subprocess():
    import sys
    import time
    for i in range(0, 5):
        sys.stdout.write("%s\n" % str(i))
        sys.stdout.flush()
        time.sleep(0.1)

def run_nose():
    import nose
    import nose.config
    conf = nose.config.Config()
    conf.verbosity = 2
    nose.run(config=conf)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'subprocess':
        run_subprocess()
    else:
        run_nose()
