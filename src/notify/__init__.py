__all__ = ('__version__', 'VERSION')
import os.path
from pkg_resources import get_distribution
from pkg_resources import DistributionNotFound
from tolerance import tolerate

DISTRIBUTION_NAME = 'notify'

# get version information from setup.py
try:
    _dist = get_distribution(DISTRIBUTION_NAME)
    if not __file__.startswith(os.path.join(_dist.location,
                                            DISTRIBUTION_NAME)):
        # not installed, but there is another version that *is*
        raise DistributionNotFound
except DistributionNotFound:
    __version__ = 'Please install this project with setup.py'
    VERSION = (0, 0, 0)
else:
    __version__ = _dist.version
    # make tuple version from string version for easy handling
    VERSION = tuple(map(tolerate(lambda x: x)(int), __version__.split('.')))
