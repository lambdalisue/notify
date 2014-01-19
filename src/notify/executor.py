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
    def force_unicode(s, encoding='utf-8', strings_only=False, errors='strict'):
        """
        Similar to smart_unicode, except that lazy instances are resolved to
        strings, rather than kept as lazy objects.

        If strings_only is True, don't convert (some) non-string-like objects.
        """
        # Handle the common case first, saves 30-40% in performance when s
        # is an instance of unicode. This function gets called often in that
        # setting.
        if isinstance(s, unicode):
            return s
        try:
            if not isinstance(s, basestring,):
                if hasattr(s, '__unicode__'):
                    s = unicode(s)
                else:
                    try:
                        s = unicode(str(s), encoding, errors)
                    except UnicodeEncodeError:
                        if not isinstance(s, Exception):
                            raise
                        # If we get to here, the caller has passed in an Exception
                        # subclass populated with non-ASCII data without special
                        # handling to display as a string. We need to handle this
                        # without raising a further exception. We do an
                        # approximation to what the Exception's standard str()
                        # output should be.
                        s = ' '.join([force_unicode(arg, encoding, strings_only,
                                errors) for arg in s])
            elif not isinstance(s, unicode):
                # Note: We use .decode() here, instead of unicode(s, encoding,
                # errors), so that if s is a SafeString, it ends up being a
                # SafeUnicode at the end.
                s = s.decode(encoding, errors)
        except UnicodeDecodeError, e:
            if not isinstance(s, Exception):
                raise 
            else:
                # If we get to here, the caller has passed in an Exception
                # subclass populated with non-ASCII bytestring data without a
                # working unicode method. Try to handle this without raising a
                # further exception by individually forcing the exception args
                # to unicode.
                s = ' '.join([force_unicode(arg, encoding, strings_only,
                        errors) for arg in s])
        return s

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
