VERSION = (0, 1, 7, 'alpha', '')

def get_version():
    """ Adapted from:
     https://djangopatterns.readthedocs.io/en/latest/app_construction/version_reporting.html
     """
    version = f'{VERSION[0]}.{VERSION[1]}'
    if VERSION[2]:
        version = f'{version}.{VERSION[2]}'
    if VERSION[3:] == ('alpha', 0):
        version = f'{version} pre-alpha'
    else:
        if VERSION[3] != 'final':
            version = f'{version} {VERSION[3]} {VERSION[4]}'
    return version

__version__ = get_version()
