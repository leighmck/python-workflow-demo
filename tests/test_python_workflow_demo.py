#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_python_workflow_demo
----------------------------------

Tests for `python_workflow_demo` module.
"""

import pytest


from python_workflow_demo import python_workflow_demo


@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument.
    """
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
