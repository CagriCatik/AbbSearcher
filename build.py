import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["tkinter", "csv"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Abkuerzungs_Suche",
    version="1.0",
    description="Suche nach Abkürzungen und Beschreibungen",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)],
)
