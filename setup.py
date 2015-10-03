setup_args = dict(
    name='tickle-me-email',
    version=1,
    author='Chris Lamb',
    author_email='chris@chris-lamb.co.uk',
    scripts=(
        'tickle-me-email',
    ),
)

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(**setup_args)
