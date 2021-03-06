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

# init.py
# Created by Disa Mhembere on 2016-12-05.
# Email: disa@jhu.edu

from include.config import config, BL_DEFAULT_CONFIG_FN
from dependencies import BL_DEFAULT_DEPS_FN
from dependencies import DependParser
from settings import *
import os

def init(projecthome, overwrite=True):
    """
    Initialize a blci project with the depenedency file and stubbed out blci
    configuration file

    **Positional Arguments:**

    projecthome:
        - The path to the root of the project

    **Optional Arguments:**

    overwrite:
        - Write over any old configuration file that may exist in `projecthome`.
            If `False` then the new configuration file will have the filename
            ``blci_\d+.yml``.
    """
    c = config(os.path.join(projecthome, BL_DEFAULT_CONFIG_FN), projecthome)

    # Build code dependencies
    dp = DependParser(c.get("read"), projecthome)
    abs_code_loc = \
            map(lambda x : os.path.join(projecthome, x),
                    c.get(BL_CODE_LOCATION))
    dp.readcode(abs_code_loc)
    dp.write(os.path.join(projecthome, BL_DEFAULT_DEPS_FN))

    # Build data dependencies
    c.build_data_dep_stub(overwrite)
    c.write(overwrite=overwrite)
