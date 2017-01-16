import os

from invoke import task

from .passphrase import passphrase


@task(
    help={
        'action': ("The CA action to take, one of 'sign', 'selfsign', "
                   "'revoke', and 'gencrl'."),
    }
)
def openssl_ca(
        ctx,
        action,
        batch=False,
        config_file=None,
        config_name=None,
        crl_reason='unspecified',
        days=None,
        in_file=None,
        out_file=None,
        extensions=None,
        md=None,
        notext=True,
        passin=None,
        verbose=False,
):
    """
    Executes `openssl ca` for signing, revocation, or CRL generation actions.
    """
    ca_command = [
        'openssl',
        'ca',
    ]

    if batch:
        ca_command.append('-batch')

    if config_file:
        ca_command.append('-config "%s"' % config_file)

    if config_name:
        ca_command.append('-name %s' % config_name)

    if extensions:
        ca_command.append('-extensions %s' % extensions)

    if days:
        ca_command.append('-days %s' % days)

    if md:
        ca_command.append('-md %s' % md)


    if notext:
        ca_command.append('-notext')

    # If the key file is encrypted, set up where passphrase is coming from.
    if passin:
        ca_command.append('-passin %s' % passphrase(passin))

    if verbose:
        ca_command.append('-verbose')
        
    if action in ('selfsign', 'sign'):
        if not os.path.isfile(in_file):
            raise Exception('Must provide an input CSR to sign.')

        if not out_file:
            raise Exception('Must provide an output path for the signed certificate.')

        if action == 'selfsign':
            ca_command.append('-selfsign')

        ca_command.extend([
            '-in "%s"' % in_file,
            '-out "%s"' % out_file,
        ])
    elif action == 'gencrl':
        ca_command.append('-gencrl')
        if out_file:
            ca_command.append('-out "%s"' % out_file)
    elif action == 'revoke':
        valid_reasons = (
            'unspecified', 'keyCompromise', 'CACompromise',
            'affiliationChanged', 'superseded',
            'cessationOfOperation', 'certificateHold', 'removeFromCRL',
        )
        if not all([crl_reason in valid_reasons, in_file]):
            raise Exception('Invalid CRL reason.')

        ca_command.extend([
            '-revoke "%s"' % in_file,
            '-crl_reason %s' % crl_reason,
        ])
    else:
        sys.stderr.write('Invalid CA action.\n')
        return

    return ctx.run(' '.join(ca_command))
