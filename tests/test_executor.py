#!/usr/bin/env nosetests -v
# coding=utf-8
from nose.tools import *
from mock import MagicMock

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
