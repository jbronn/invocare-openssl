from invoke import task

from .passphrase import passphrase


@task
def openssl_genpkey(
        ctx,
        key_file,
        algorithm='RSA',
        cipher=None,
        pkeyopt=None,
        passwd=None,
):
    """
    Executes the `openssl genpkey` command for private key generation.
    """
    genpkey_command = [
        'openssl',
        'genpkey',
    ]

    if algorithm:
        genpkey_command.append('-algorithm %s' % algorithm)

    if cipher:
        genpkey_command.append('-%s' % cipher)

    if passwd:
        genpkey_command.append('-pass %s' % passphrase(passwd))

    if pkeyopt:
        genpkey_command.extend([
            '-pkeyopt %s:%s' % (option, value)
            for option, value in pkeyopt.items()
        ])

    genpkey_command.append('-out "%s"' % key_file)

    return ctx.run(' '.join(genpkey_command))
