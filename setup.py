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
from pathlib import Path
from setuptools import setup, Extension, find_packages

here = Path(__file__).parent.resolve()

with open(here / "README.md", encoding="utf-8") as f:
    readme = f.read()

version = {}
with open(here / "tgcrypto" / "_version.py") as f:
    exec(f.read(), version)

extra_compile_args = []
extra_link_args = []

if sys.platform != 'win32':
    extra_compile_args.extend([
        '-O3',
        '-march=native',
        '-mtune=native',
        '-ffast-math',
        '-funroll-loops',
        '-finline-functions',
        '-flto',
        '-fomit-frame-pointer',
        '-DNDEBUG',
    ])
    extra_link_args.extend(['-flto'])
else:
    extra_compile_args.extend(['/O2', '/GL', '/DNDEBUG'])
    extra_link_args.extend(['/LTCG'])

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
