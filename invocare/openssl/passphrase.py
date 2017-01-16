import os


def passphrase(arg):
    if arg == 'stdin':
        return 'stdin'
    elif os.path.isfile(arg):
        return 'file:"%s"' % arg
    elif arg in os.environ:
        return 'env:%s' % arg
    else:
        return 'pass:"%s"'
