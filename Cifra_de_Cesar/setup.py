import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("Cifra_Cesar_PysimpleGUI.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = [],
        include_files = [],
        excludes = []
)




setup(
    name = "Cesar",
    version = "1.0",
    description = "Sifra de cesar",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
