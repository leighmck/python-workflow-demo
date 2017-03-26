#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='python_workflow_demo',
    version='0.1.0',
    description="Workflow demo using Python and MQTT.",
    long_description=readme + '\n\n' + history,
    author="Leigh McKenzie",
    author_email='maccarav0@gmail.com',
    url='https://github.com/leighmck/python_workflow_demo',
    packages=[
        'python_workflow_demo',
    ],
    package_dir={'python_workflow_demo':
                 'python_workflow_demo'},
    include_package_data=True,
    install_requires=requirements,
    license="ISC license",
    zip_safe=False,
    keywords='python_workflow_demo',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
