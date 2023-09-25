import sys
from cx_Freeze import setup, Executable


# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["os", "re", "sys", "json"], 
    "includes": [
        "tkinter",
    ]
}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="Analisador de Frequência",
    version="0.1",
    description="Tópicos avançados em programação",
    author="Gabriel Carvalho",
    options={"build_exe": build_exe_options},
    executables=[Executable("app.py", base=base)],
)