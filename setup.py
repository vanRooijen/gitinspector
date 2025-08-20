# coding: utf-8
#
# Copyright © 2013 Ejwa Software. All rights reserved.
#
# This file is part of gitinspector.
# Licensed under the GNU GPL v3 or later.

import io
import os
import re
from glob import glob
from setuptools import setup, find_packages

def read(relpath):
    here = os.path.abspath(os.path.dirname(__file__))
    with io.open(os.path.join(here, relpath), "r", encoding="utf-8") as f:
        return f.read()

def get_version():
    m = re.search(r'^__version__\s*=\s*[\'"]([^\'"]+)[\'"]',
                  read("gitinspector/version.py"), re.M)
    if not m:
        raise RuntimeError("Cannot find __version__ in gitinspector/version.py")
    return m.group(1)

setup(
    name="gitinspector",
    version=get_version(),  # <-- no import, no side effects
    author="Ejwa Software",
    author_email="gitinspector@ejwa.se",
    description="A statistical analysis tool for git repositories.",
    license="GNU GPL v3",
    keywords="analysis analyzer git python statistics stats vc vcs timeline",
    url="https://github.com/ejwa/gitinspector",
    long_description=read("DESCRIPTION.txt"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Topic :: Software Development :: Version Control",
        "Topic :: Utilities",
    ],
    packages=find_packages(exclude=["tests"]),
    package_data={"": ["html/*", "translations/*"]},
    data_files=[("share/doc/gitinspector", glob("*.txt"))],
    entry_points={"console_scripts": ["gitinspector = gitinspector.gitinspector:main"]},
    zip_safe=False,
)

