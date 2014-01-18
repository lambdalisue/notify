#!/usr/bin/env nosetests -v
# coding=utf-8
import os
import platform
from nose.tools import *
from mock import MagicMock

from notify.conf import get_user_config_filename

def setup_environment():
    import copy
    setup_environment.original_environ = copy.deepcopy(os.environ)
    setup_environment.original_exists = os.path.exists
    setup_environment.original_system = platform.system

def teardown_environment():
    os.environ = setup_environment.original_environ
    os.path.exists = setup_environment.original_exists
    platform.system = setup_environment.original_system

@with_setup(setup_environment, teardown_environment)
def test_get_user_config_filename_windows():
    """get_user_config_filename in Windows"""
    # prepare environment
    os.environ['APPDATA'] = r"C:/Users/Test/AppData"
    platform.system = MagicMock(return_value='Windows')

    eq_(get_user_config_filename('Test1'),
        r"C:/Users/Test/AppData/Test1/Test1.cfg")
    eq_(get_user_config_filename('Test2'),
        r"C:/Users/Test/AppData/Test2/Test2.cfg")

@with_setup(setup_environment, teardown_environment)
def test_get_user_config_filename_linux_freedesktop():
    """
    get_user_config_filename in Linux (freedesktop.org)
    """
    # prepare environment
    os.path.exists = lambda x: True
    os.environ['USER'] = "TestUser"
    os.environ['HOME'] = "/home/TestUser"
    platform.system = MagicMock(return_value='Linux')

    eq_(get_user_config_filename('Test1'),
        r"/home/TestUser/.config/Test1/Test1.cfg")
    eq_(get_user_config_filename('Test2'),
        r"/home/TestUser/.config/Test2/Test2.cfg")

@with_setup(setup_environment, teardown_environment)
def test_get_user_config_filename_linux_with_xdg_config_home():
    """
    get_user_config_filename in Linux (with XDG_CONFIG_HOME)
    """
    # prepare environment
    os.path.exists = lambda x: True
    os.environ['USER'] = "TestUser"
    os.environ['HOME'] = "/home/TestUser"
    os.environ['XDG_CONFIG_HOME'] = "~/.test_config"
    platform.system = MagicMock(return_value='Linux')

    eq_(get_user_config_filename('Test1'),
        r"/home/TestUser/.test_config/Test1/Test1.cfg")
    eq_(get_user_config_filename('Test2'),
        r"/home/TestUser/.test_config/Test2/Test2.cfg")

@with_setup(setup_environment, teardown_environment)
def test_get_user_config_filename_linux_non_freedesktop():
    """
    get_user_config_filename in Linux (non freedesktop.org)
    """
    # prepare environment
    os.path.exists = lambda x: False
    os.environ['USER'] = "TestUser"
    os.environ['HOME'] = "/home/TestUser"
    platform.system = MagicMock(return_value='Linux')

    eq_(get_user_config_filename('Test1'),
        r"/home/TestUser/.Test1.cfg")
    eq_(get_user_config_filename('Test2'),
        r"/home/TestUser/.Test2.cfg")

@with_setup(setup_environment, teardown_environment)
def test_get_user_config_filename_darwin():
    """
    get_user_config_filename in Darwin
    """
    # prepare environment
    os.environ['USER'] = "TestUser"
    os.environ['HOME'] = "/home/TestUser"
    platform.system = MagicMock(return_value='Darwin')

    eq_(get_user_config_filename('Test1'),
        r"/home/TestUser/.Test1.cfg")
    eq_(get_user_config_filename('Test2'),
        r"/home/TestUser/.Test2.cfg")

@with_setup(setup_environment, teardown_environment)
def test_get_user_config_filename_unknown():
    """
    get_user_config_filename in Unknown
    """
    # prepare environment
    os.environ['USER'] = "TestUser"
    os.environ['HOME'] = "/home/TestUser"
    platform.system = MagicMock(return_value='Unknown')

    eq_(get_user_config_filename('Test1'),
        r"/home/TestUser/Test1.cfg")
    eq_(get_user_config_filename('Test2'),
        r"/home/TestUser/Test2.cfg")
