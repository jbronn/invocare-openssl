from setuptools import setup


_locals = {}
with open('invocare/openssl/_version.py') as fh:
    exec(fh.read(), None, _locals)
version = _locals['__version__']


setup(name='invocare-openssl',
      version=version,
      author='Justin Bronn',
      author_email='jbronn@gmail.com',
      description='OpenSSL Invocations',
      long_description='Implementions of invoke tasks for OpenSSL.',
      license='Apache License 2.0',
      url='https://github.com/jbronn/invocare-openssl',
      download_url='https://pypi.python.org/pypi/invocare-openssl/',
      install_requires=[
        'invocare>=0.1.0,<1.0.0',
      ],
      packages=['invocare.openssl'],
      zip_safe=False,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],
)
