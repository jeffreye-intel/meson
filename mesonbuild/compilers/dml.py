
from __future__ import annotations

import os.path
import subprocess
import typing as T

from pkg_resources import Environment
from mesonbuild import coredata
from mesonbuild.compilers.compilers import Compiler
from mesonbuild.envconfig import MachineInfo
from mesonbuild.linkers.linkers import DynamicLinker
from mesonbuild.programs import ExternalProgram
from mesonbuild.utils.universal import EnvironmentException, MachineChoice, OptionKey

class DMLCompiler(Compiler):

    language = 'dml'

    def __init__(self, ccache: T.List[str], exelist: T.List[str], version: str, for_machine: MachineChoice, is_cross: bool,
                 info: 'MachineInfo', exe_wrapper: T.Optional['ExternalProgram'] = None,
                 linker: T.Optional['DynamicLinker'] = None,
                 full_version: T.Optional[str] = None):
        # If a child ObjCPP class has already set it, don't set it ourselves
        Compiler.__init__(self, ccache, exelist, version, for_machine, info,
                          is_cross=is_cross, linker=linker,
                          full_version=full_version)

    @staticmethod
    def get_display_language() -> str:
        return 'DML'

    def get_no_stdinc_args(self) -> T.List[str]:
        return ['']

    def get_options(self) -> 'coredata.MutableKeyedOptionDictType':
        opts = super().get_options()
        return opts

    def get_optimization_args(self, optimization_level: str) -> T.List[str]:
        return [] ## TODO: Does DML have optimization arguments?

    def get_output_args(self, outputname: str) -> T.List[str]:
        return [] ## TODO: what DML output args do we need?

    def sanity_check(self, work_dir: str, environment: 'Environment') -> None:
        source_name = os.path.join(work_dir, 'sanity.dml')
        with open(source_name, 'w', encoding='utf-8') as ofile:
            ofile.write(f'dml 1.4;  device test_device')
        pc = subprocess.Popen(self.exelist + [source_name], cwd=work_dir)
        pc.wait()
        if pc.returncode != 0:
            raise EnvironmentException('DMLC compiler %s can not compile DML to C/C++.' % self.name_string())

    def get_default_include_dirs(self) -> T.List[str]:
        return super().get_default_include_dirs()