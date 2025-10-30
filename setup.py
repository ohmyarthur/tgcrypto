#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.
#
#  Modified by ohmyarthur <https://github.com/ohmyarthur>

import sys
import os
import platform
from pathlib import Path
from setuptools import setup, Extension

here = Path(__file__).parent.resolve()

with open(here / "README.md", encoding="utf-8") as f:
    readme = f.read()

version = {}
with open(here / "tgcrypto" / "_version.py") as f:
    exec(f.read(), version)


def get_compile_args():
    """Get platform-specific compiler arguments that work in CI environments."""
    extra_compile_args = []
    extra_link_args = []
    
    if sys.platform == 'win32':
        extra_compile_args.extend(['/O2', '/GL', '/DNDEBUG'])
        extra_link_args.extend(['/LTCG'])
    else:
        extra_compile_args.extend([
            '-O3',
            '-ffast-math',
            '-funroll-loops',
            '-finline-functions',
            '-fomit-frame-pointer',
            '-DNDEBUG',
        ])
        
        if os.environ.get('CIBUILDWHEEL', '0') != '1' or os.environ.get('ENABLE_LTO', '0') == '1':
            extra_compile_args.append('-flto')
            extra_link_args.append('-flto')
        
        machine = platform.machine().lower()
        is_ci = os.environ.get('CI', 'false').lower() == 'true' or os.environ.get('CIBUILDWHEEL', '0') == '1'
        
        if is_ci:
            if sys.platform == 'darwin':
                arch = os.environ.get('ARCHFLAGS', '')
                if 'arm64' in arch or machine in ('arm64', 'aarch64'):
                    extra_compile_args.extend(['-mcpu=apple-m1'])
                elif 'x86_64' in arch or machine in ('x86_64', 'amd64'):
                    extra_compile_args.extend(['-march=x86-64', '-mtune=generic'])
            elif machine in ('x86_64', 'amd64'):
                extra_compile_args.extend(['-march=x86-64', '-mtune=generic'])
            elif machine in ('aarch64', 'arm64'):
                extra_compile_args.extend(['-march=armv8-a'])
        else:
            if sys.platform == 'darwin' and machine == 'arm64':
                extra_compile_args.extend(['-mcpu=apple-m1'])
            else:
                extra_compile_args.extend(['-march=native', '-mtune=native'])
    
    return extra_compile_args, extra_link_args


extra_compile_args, extra_link_args = get_compile_args()

setup(
    ext_modules=[
        Extension(
            "tgcrypto.tgcrypto",
            sources=[
                "tgcrypto/tgcrypto.c",
                "tgcrypto/aes256.c",
                "tgcrypto/ige256.c",
                "tgcrypto/ctr256.c",
                "tgcrypto/cbc256.c"
            ],
            extra_compile_args=extra_compile_args,
            extra_link_args=extra_link_args,
        )
    ]
)