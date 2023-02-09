
from __future__ import annotations

import os.path
import typing as T
from mesonbuild import coredata
from mesonbuild.compilers.compilers import Compiler
from mesonbuild.envconfig import MachineInfo
from mesonbuild.linkers.linkers import DynamicLinker
from mesonbuild.programs import ExternalProgram
from mesonbuild.utils.universal import MachineChoice, OptionKey


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
        key = OptionKey('std', machine=self.for_machine, lang=self.language)
        opts.update({
            key: coredata.UserComboOption(
                'C++ language standard to use',
                ['none'],
                'none',
            ),
        })
        return opts