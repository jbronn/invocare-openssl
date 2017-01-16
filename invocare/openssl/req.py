from invoke import task

from .passphrase import passphrase


@task(
    help={
        'key_file': 'The private key to use for the CSR.',
        'csr_file': 'The output path for the CSR file.',
    }
)
def openssl_req(
        ctx,
        key_file,
        csr_file,
        config_file=None,
        config_name=None,
        extensions=None,
        md_alg='sha256',
        noout=False,
        passin=None,
        subj=None,
        text=False,
):
    """
    A low level wrapper for executing the `openssl req` command.
    """
    req_command = [
        'openssl',
        'req',
        '-new',
        '-%s' % md_alg,
    ]

    if config_file:
        req_command.append('-config "%s"' % config_file)

    if subj:
        req_command.append('-subj "%s"' % subj)

    if extensions:
        req_command.append('-extensions %s' % extensions)

    if passin:
        req_command.append('-passin %s' % passphrase(passin))

    if noout:
        req_command.append('-noout')

    if text:
        req_command.append('-text')

    req_command.extend([
        '-key "%s"' % key_file,
        '-out "%s"' % csr_file,
    ])

    return ctx.run(' '.join(req_command))
