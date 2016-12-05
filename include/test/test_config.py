#!/usr/bin/env python

# Copyright 2016 neurodata (http://neurodata.io/)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# test_dependencies.py
# Created by Disa Mhembere on 2016-11-28.
# Email: disa@jhu.edu

import argparse
import sys
import os
sys.path.append(os.path.abspath("../"))

from config import *

def test_valid():
    fn = "test-blci/blci.yml"
    c = config(fn, silent_fail=True)
    assert c.isvalid(), "Invalid configuration file '{}'".format(fn)

    for setting in c.getall():
        assert setting in BLCI_SETTINGS

def test_invalid():
    fn = "config/error.yml"
    c = config(fn, silent_fail=True)
    assert not c.isvalid(), "Invalid configuration file '{}'".format(fn)