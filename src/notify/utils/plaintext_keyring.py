# coding=utf-8
"""
Plaintext keyring module
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'
import os
import ConfigParser

class PlaintextKeyring(object):
    def __init__(self, filename = None):
        if filename is None:
            filename = os.path.expanduser('~')
            filename = os.path.join(filename, '.plaintext_keyring')
        self.filename = filename

    def get_password(self, service_name, username):
        config = ConfigParser.SafeConfigParser()
        config.read([self.filename])
        try:
            return config.get(service_name, username)
        except (ConfigParser.NoSectionError, ConfigParser.NoOptionError):
            return ""

    def set_password(self, service_name, username, password):
        config = ConfigParser.SafeConfigParser()
        config.read([self.filename])
        if not config.has_section(service_name):
            config.add_section(service_name)
        config.set(service_name, username, password)
        fo = open(self.filename, 'wb')
        config.write(fo)
        fo.close()
        # change permission of the file
        os.chmod(self.filename, 0600)

    def delete_password(self, service_name, username):
        config = ConfigParser.SafeConfigParser()
        config.read([self.filename])
        config.set(service_name, username, "")
        fo = open(self.filename, 'wb')
        config.write(fo)
        fo.close()
        # change permission of the file
        os.chmod(self.filename, 0600)
