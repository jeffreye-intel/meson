# Copyright 2023 Intel Corporation

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import subprocess
import re
import os
import unittest

from mesonbuild.mesonlib import (
    MachineChoice, is_osx
)
from mesonbuild.compilers import (
    detect_c_compiler
)


from run_tests import (
    get_fake_env
)

from .baseplatformtests import BasePlatformTests
from .helpers import *

class DMLTests(BasePlatformTests):

    def test_dml_init(self):
        testdir = os.path.join(self.dml_test_dir, '1 Simple')
        self.init(testdir)
        self.assertIn('dmlc', self.get_compdb()[0]['command'])
