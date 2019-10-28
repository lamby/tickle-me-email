#!/usr/bin/env python3

from setuptools import setup

setup(
    name='tickle-me-email',
    version='4.3.0',
    url='https://chris-lamb.co.uk/projects/tickle-me-email',
    author='Chris Lamb',
    author_email='chris@chris-lamb.co.uk',
    description='Toolbox for implementing GTD-like behaviours in your IMAP inbox',
    scripts=(
        'tickle-me-email',
    ),
)
