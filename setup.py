#!/usr/bin/env python
# Copyright (c) 2013 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(
    name='hacking',
    author='OpenStack',
    author_email='openstack-dev@lists.openstack.org',
    description='OpenStack Hacking Guideline Enforcement',
    long_description=read('README.rst'),
    url='http://github.com/mfrobben/hacking',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: OpenStack',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    packages=['hacking'],
    install_requires=[
        'setuptools',
        'six'
    ],
    entry_points={
        'flake8.extension': [
            'H101 = hacking.core:hacking_todo_format',
            'H102 = hacking.core:hacking_has_license',
            'H103 = hacking.core:hacking_has_correct_license',
            'H104 = hacking.core:hacking_has_only_comments',
            'H201 = hacking.core:hacking_except_format',
            'H202 = hacking.core:hacking_except_format_assert',
            'H231 = hacking.core:hacking_python3x_except_compatible',
            'H232 = hacking.core:hacking_python3x_octal_literals',
            'H233 = hacking.core:hacking_python3x_print_function',
            'H234 = hacking.core:hacking_no_assert_equals',
            'H235 = hacking.core:hacking_no_assert_underscore',
            'H301 = hacking.core:hacking_import_rules',
            'H306 = hacking.core:hacking_import_alphabetical',
            'H401 = hacking.core:hacking_docstring_start_space',
            'H402 = hacking.core:hacking_docstring_one_line',
            'H403 = hacking.core:hacking_docstring_multiline_end',
            'H404 = hacking.core:hacking_docstring_multiline_start',
            'H405 = hacking.core:hacking_docstring_summary',
            'H501 = hacking.core:hacking_no_locals',
            'H903 = hacking.core:hacking_no_cr',
            'H700 = hacking.core:hacking_localization_strings',
            'H801 = hacking.core:OnceGitCheckCommitTitleBug',
            'H802 = hacking.core:OnceGitCheckCommitTitleLength',
            'H803 = hacking.core:OnceGitCheckCommitTitlePeriodEnding',
            'H901 = hacking.core:hacking_is_not',
            'H902 = hacking.core:hacking_not_in'
        ],
    },
)
