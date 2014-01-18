#!/usr/bin/env python
# coding=utf-8
"""
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'
import os
from conf import create_default_config
from arguments import parse_arguments
from notifier import call_and_notificate

def main(args=None):
    import sys
    args = args or sys.argv
    config = create_default_config()
    args, opts = parse_arguments(args, config)

    if opts.setup:
        from wizard import setup_wizard
        setup_wizard(config)
    elif opts.check:
        from conf import get_user_config_filename
        call_and_notificate(['cat', get_user_config_filename()], opts)
    elif len(args) > 0:
        call_and_notificate(args, opts)

if __name__ == '__main__':
    main()
