# -*- coding: utf-8 -*-
# Copyright 2021 Twitter, Inc.
# Licensed under the MIT License
# https://opensource.org/licenses/MIT
import re
from setuptools import setup, find_packages

def parse_version(str_):
    """
    Parses the program's version from a python variable declaration.
    """
    v = re.findall(r"\d+.\d+.\d+", str_)
    if v:
        return v[0]
    else:
        print("cannot parse string {}".format(str_))
        raise KeyError

# Our version is stored here.
with open("./searchtweets/_version.py") as f:
    _version_line = [line for line in f.readlines()
                     if line.startswith("VERSION")][0].strip()
    VERSION = parse_version(_version_line)

setup(name='searchtweets-v2',
      description="Wrapper for Twitter API v2 search endpoints (both 'search Tweets' and 'count Tweets' endpoints).",
      url='https://github.com/twitterdev/search-tweets-python',
      author='Fiona Pigott, Jeff Kolb, Josh Montague, Aaron Gonzales, Jim Moffitt',
      long_description=open('README.rst', 'r', encoding="utf-8").read(),
      author_email='dev-support@twitter.com',
      license='MIT',
      version=VERSION,
      python_requires='>=3.3',
      install_requires=["requests", "pyyaml", "python-dateutil"],
      packages=find_packages(),
      scripts=["scripts/search_tweets.py", "scripts/poll_tweets.py"],
     )
