import sys

from cx_Freeze import setup, Executable

base = 'Console'

build_exe_options = {"packages": ["PIL"]}

setup(
        name = "ワンクリック軽量",
        version = "1.0 GA",
        description = "ドラッグアンドドロップで軽量化ができます",
        options = {"build_exe": build_exe_options}, 
        executables = [Executable("ワンクリック軽量.py")]
	)